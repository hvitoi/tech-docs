package task

import (
	"cmp"
	"errors"
	"slices"
	"sync"
	"time"
)

var ErrNotFound = errors.New("task not found")

type Task struct {
	ID        int       `json:"id"`
	Title     string    `json:"title"`
	Done      bool      `json:"done"`
	CreatedAt time.Time `json:"created_at"`
}

// Store is an in-memory, concurrency-safe task store. Handlers run on
// separate goroutines, so access must be guarded by a mutex.
type Store struct {
	mu     sync.RWMutex
	tasks  map[int]Task
	nextID int
}

func NewStore() *Store {
	return &Store{tasks: make(map[int]Task), nextID: 1}
}

func (s *Store) List() []Task {
	s.mu.RLock()
	defer s.mu.RUnlock()

	tasks := make([]Task, 0, len(s.tasks))
	for _, t := range s.tasks {
		tasks = append(tasks, t)
	}
	slices.SortFunc(tasks, func(a, b Task) int { return cmp.Compare(a.ID, b.ID) })
	return tasks
}

func (s *Store) Get(id int) (Task, error) {
	s.mu.RLock()
	defer s.mu.RUnlock()

	t, ok := s.tasks[id]
	if !ok {
		return Task{}, ErrNotFound
	}
	return t, nil
}

func (s *Store) Create(title string, done bool) Task {
	s.mu.Lock()
	defer s.mu.Unlock()

	t := Task{ID: s.nextID, Title: title, Done: done, CreatedAt: time.Now().UTC()}
	s.tasks[t.ID] = t
	s.nextID++
	return t
}

func (s *Store) Update(id int, title string, done bool) (Task, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	t, ok := s.tasks[id]
	if !ok {
		return Task{}, ErrNotFound
	}
	t.Title = title
	t.Done = done
	s.tasks[id] = t
	return t, nil
}

func (s *Store) Delete(id int) error {
	s.mu.Lock()
	defer s.mu.Unlock()

	if _, ok := s.tasks[id]; !ok {
		return ErrNotFound
	}
	delete(s.tasks, id)
	return nil
}
