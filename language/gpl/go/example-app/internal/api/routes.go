package api

import (
	"log/slog"
	"net/http"

	"example-app/internal/task"
)

// NewHandler builds the router with all routes and global middleware.
func NewHandler(logger *slog.Logger, store *task.Store) http.Handler {
	mux := http.NewServeMux()

	mux.Handle("GET /health", handleHealth())

	mux.Handle("GET /tasks", handleListTasks(store))
	mux.Handle("POST /tasks", handleCreateTask(store))
	mux.Handle("GET /tasks/{id}", handleGetTask(store))
	mux.Handle("PUT /tasks/{id}", handleUpdateTask(store))
	mux.Handle("DELETE /tasks/{id}", handleDeleteTask(store))

	return chain(mux,
		requestID,
		logging(logger),
		recoverer(logger),
	)
}
