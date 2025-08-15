import { TaskList } from "./messages.js";

// services (with same name as in .proto file)
function ListAll(req, cb) {
  return cb(null, TaskList);
}

function AddTask(req, cb) {
  const { id, description, date } = req.request;
  TaskList.push({ id, description, date, done: false });

  return cb(null, TaskList.at(-1));
}

function MarkAsDone(req, cb) {
  const { index, doneTask } = TaskList.find((task, index) => {
    if (task.id === req.request.id) {
      return { index, task };
    }
  });

  if (!doneTask) {
    return cb(new Error("do not exist"), null);
  }

  doneTask.done = true;
  TaskList[index] = doneTask;
  return cb(null, doneTask);
}

export { ListAll, AddTask, MarkAsDone };
