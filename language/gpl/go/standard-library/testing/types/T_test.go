package main

import (
	"errors"
	"os"
	"strconv"
	"testing"
)

func Add(a, b int) int {
	return a + b
}

func Divide(a, b int) (int, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

// t.Errorf
func TestAdd(t *testing.T) {
	result := Add(1, 1)

	if result != 2 {
		t.Errorf("Expected 2, but got %d", result)
	}
}

// t.Error: logs and marks the test failed, but keeps running
func TestError(t *testing.T) {
	if Add(2, 2) != 4 {
		t.Error("Add(2, 2) should be 4")
	}
}

// t.Fatal / t.Fatalf: logs, marks failed and stops the test immediately
func TestFatal(t *testing.T) {
	result, err := Divide(10, 2)
	if err != nil {
		t.Fatalf("unexpected error: %v", err)
	}
	if result != 5 {
		t.Errorf("Divide(10, 2) = %d, want 5", result)
	}
}

// t.Run: Table-driven test with Subtests
func TestAddTable(t *testing.T) {
	tests := []struct {
		name string
		a, b int
		want int
	}{
		{"positives", 1, 2, 3},
		{"negatives", -1, -2, -3},
		{"zero", 0, 0, 0},
		{"mixed", -1, 1, 0},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Add(tt.a, tt.b); got != tt.want {
				t.Errorf("Add(%d, %d) = %d, want %d", tt.a, tt.b, got, tt.want)
			}
		})
	}
}

// Error cases
func TestDivideByZero(t *testing.T) {
	_, err := Divide(1, 0)
	if err == nil {
		t.Fatal("expected an error, got nil")
	}
}

// t.Helper: reports failures at the caller's line instead of inside the helper
func assertEqual(t *testing.T, got, want int) {
	t.Helper()
	if got != want {
		t.Errorf("got %d, want %d", got, want)
	}
}

func TestHelper(t *testing.T) {
	assertEqual(t, Add(1, 2), 3)
}

// t.Log / t.Logf: only shown on failure or with `go test -v`
func TestLog(t *testing.T) {
	t.Log("computing Add(3, 4)")
	assertEqual(t, Add(3, 4), 7)
}

// t.Skip: skips the test, e.g. for slow tests under `go test -short`
func TestSlow(t *testing.T) {
	if testing.Short() {
		t.Skip("skipping slow test in short mode")
	}
	assertEqual(t, Add(100, 200), 300)
}

// t.Parallel: runs the test concurrently with other parallel tests
func TestParallel(t *testing.T) {
	for _, n := range []int{1, 2, 3} {
		t.Run("n="+strconv.Itoa(n), func(t *testing.T) {
			t.Parallel()
			assertEqual(t, Add(n, n), 2*n)
		})
	}
}

// t.Cleanup: runs after the test (and its subtests) finish, in LIFO order
func TestCleanup(t *testing.T) {
	f, err := os.CreateTemp("", "example")
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() { os.Remove(f.Name()) })

	if _, err := f.WriteString("hello"); err != nil {
		t.Fatal(err)
	}
}

// t.TempDir: directory removed automatically when the test ends
func TestTempDir(t *testing.T) {
	dir := t.TempDir()
	if err := os.WriteFile(dir+"/a.txt", []byte("hi"), 0o644); err != nil {
		t.Fatal(err)
	}
}

// t.Setenv: sets an env var and restores it after the test
func TestSetenv(t *testing.T) {
	t.Setenv("APP_ENV", "test")
	if got := os.Getenv("APP_ENV"); got != "test" {
		t.Errorf("APP_ENV = %q, want %q", got, "test")
	}
}
