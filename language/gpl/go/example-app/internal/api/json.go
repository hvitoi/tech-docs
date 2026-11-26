package api

import (
	"encoding/json"
	"errors"
	"fmt"
	"log/slog"
	"net/http"
)

const maxBodyBytes = 1 << 20 // 1 MB

// Validator is implemented by request types that can check their own fields.
// It returns a map of field name to problem; an empty map means valid.
type Validator interface {
	Valid() map[string]string
}

func writeJSON(w http.ResponseWriter, status int, v any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	if err := json.NewEncoder(w).Encode(v); err != nil {
		slog.Error("encode response", "err", err)
	}
}

type errorResponse struct {
	Error  string            `json:"error"`
	Fields map[string]string `json:"fields,omitempty"`
}

func writeError(w http.ResponseWriter, status int, msg string) {
	writeJSON(w, status, errorResponse{Error: msg})
}

// decodeValid decodes a JSON body into T and validates it.
// On failure it writes the error response itself and returns false.
func decodeValid[T Validator](w http.ResponseWriter, r *http.Request) (T, bool) {
	var v T
	r.Body = http.MaxBytesReader(w, r.Body, maxBodyBytes)

	dec := json.NewDecoder(r.Body)
	dec.DisallowUnknownFields()
	if err := dec.Decode(&v); err != nil {
		var maxErr *http.MaxBytesError
		if errors.As(err, &maxErr) {
			writeError(w, http.StatusRequestEntityTooLarge, "request body too large")
		} else {
			writeError(w, http.StatusBadRequest, fmt.Sprintf("invalid JSON: %v", err))
		}
		return v, false
	}

	if problems := v.Valid(); len(problems) > 0 {
		writeJSON(w, http.StatusUnprocessableEntity, errorResponse{Error: "validation failed", Fields: problems})
		return v, false
	}
	return v, true
}
