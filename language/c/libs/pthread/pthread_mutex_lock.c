#include <pthread.h>

pthread_mutex_t my_mutex; // create a lock object globally

void my_function() {
  pthread_mutex_lock(&my_mutex);

  // do something

  pthread_mutex_unlock(&my_mutex);
}

int main() {
  pthread_mutex_init(&my_mutex);
  my_function(); // locks the mutex while the function is being executed
}
