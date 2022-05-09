import grpc from "grpc";
import path from "path";

// load proto file
const TaskDefinition = grpc.load(path.resolve("./task.proto"));

// create gRPC client
const client = new TaskDefinition.APITaskList(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

/**
 * invoke services
 */

// ListAll
client.ListAll({}, (err, taskList) => {
  if (err) throw err;
  console.log(taskList);
});

// AddTask
const newTask = {
  id: 2,
  description: "aaa",
  date: "02/03/2022",
  done: false,
};
client.AddTask(newTask, (err, task) => {
  if (err) throw err;
  console.log(task);
});

// MarkAsDone
client.MarkAsDone({ id: 2 }, (err, task) => {
  if (err) throw err;
  console.log(task);
});
