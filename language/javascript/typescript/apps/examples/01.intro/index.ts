import axios from 'axios';

const url = 'https://jsonplaceholder.typicode.com/todos/1';

// Todo represents a TYPE of a value: an object that has these specific properties
interface Todo {
  id: number;
  title: string;
  completed: boolean;
}

axios.get(url).then((res) => {
  const todo = res.data as Todo; // Object of type todo

  const id = todo.id;
  const title = todo.title;
  const completed = todo.completed;

  logTodo(id, title, completed);
});

const logTodo = (id: number, title: string, completed: boolean) => {
  console.log(`
    ${id}
    ${title}
    ${completed}
  `);
};
