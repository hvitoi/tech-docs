package api

import (
	"errors"
	"net/http"
	"strconv"
	"strings"

	"example-app/internal/task"
)

type taskRequest struct {
	Title string `json:"title"`
	Done  bool   `json:"done"`
}

func (req taskRequest) Valid() map[string]string {
	problems := make(map[string]string)
	title := strings.TrimSpace(req.Title)
	switch {
	case title == "":
		problems["title"] = "is required"
	case len(title) > 100:
		problems["title"] = "must be at most 100 characters"
	}
	return problems
}

func handleHealth() http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		writeJSON(w, http.StatusOK, map[string]string{"status": "ok"})
	}
}

func handleListTasks(store *task.Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		tasks := store.List()

		// Optional filter: GET /tasks?done=true
		if v := r.URL.Query().Get("done"); v != "" {
			done, err := strconv.ParseBool(v)
			if err != nil {
				writeError(w, http.StatusBadRequest, "query param 'done' must be a boolean")
				return
			}
			filtered := make([]task.Task, 0, len(tasks))
			for _, t := range tasks {
				if t.Done == done {
					filtered = append(filtered, t)
				}
			}
			tasks = filtered
		}

		writeJSON(w, http.StatusOK, tasks)
	}
}

func handleGetTask(store *task.Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		id, ok := pathID(w, r)
		if !ok {
			return
		}
		t, err := store.Get(id)
		if err != nil {
			writeStoreError(w, err)
			return
		}
		writeJSON(w, http.StatusOK, t)
	}
}

func handleCreateTask(store *task.Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		req, ok := decodeValid[taskRequest](w, r)
		if !ok {
			return
		}
		t := store.Create(strings.TrimSpace(req.Title), req.Done)
		w.Header().Set("Location", "/tasks/"+strconv.Itoa(t.ID))
		writeJSON(w, http.StatusCreated, t)
	}
}

func handleUpdateTask(store *task.Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		id, ok := pathID(w, r)
		if !ok {
			return
		}
		req, ok := decodeValid[taskRequest](w, r)
		if !ok {
			return
		}
		t, err := store.Update(id, strings.TrimSpace(req.Title), req.Done)
		if err != nil {
			writeStoreError(w, err)
			return
		}
		writeJSON(w, http.StatusOK, t)
	}
}

func handleDeleteTask(store *task.Store) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		id, ok := pathID(w, r)
		if !ok {
			return
		}
		if err := store.Delete(id); err != nil {
			writeStoreError(w, err)
			return
		}
		w.WriteHeader(http.StatusNoContent)
	}
}

func pathID(w http.ResponseWriter, r *http.Request) (int, bool) {
	id, err := strconv.Atoi(r.PathValue("id"))
	if err != nil || id < 1 {
		writeError(w, http.StatusBadRequest, "id must be a positive integer")
		return 0, false
	}
	return id, true
}

func writeStoreError(w http.ResponseWriter, err error) {
	if errors.Is(err, task.ErrNotFound) {
		writeError(w, http.StatusNotFound, err.Error())
		return
	}
	writeError(w, http.StatusInternalServerError, "internal server error")
}
