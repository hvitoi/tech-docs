// const grpc = require("grpc");
// const path = require("path");
import grpc from "grpc";
import path from "path";

import { ListAll, AddTask, MarkAsDone } from "./services.js";

// load proto file
const TaskDefinition = grpc.load(path.resolve("./task.proto"));

// create gRPC server
const server = new grpc.Server();
server.addService(TaskDefinition.APITaskList.service, {
  ListAll,
  AddTask,
  MarkAsDone,
});
server.bind("0.0.0.0:50031", grpc.ServerCredentials.createInsecure());
server.start;
