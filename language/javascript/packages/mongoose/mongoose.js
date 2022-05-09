const mongoose = require("mongoose");

// USER MODEL
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    unique: true,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
});
userSchema.virtual("tasks", {
  // Setup a virtual property that fetches tasks from 'tasks' that were created by the current user
  ref: "Task",
  localField: "_id", // This equivalent to a JOIN in SQL... INNER JOIN Task ON Task.owner = User._id
  foreignField: "owner",
});
const User = mongoose.model("User", userSchema);

// TASK MODEL
const taskSchema = new mongoose.Schema({
  description: {
    type: String,
    required: true,
  },
  completed: {
    type: Boolean,
    default: false,
  },
  owner: {
    type: mongoose.Schema.Types.ObjectId,
    required: true,
    ref: "User", // Create reference of the 'owner' property with the User model
  },
});
const Task = mongoose.model("Task", taskSchema);

// JOIN USER AND TASK MODELS
const main = async () => {
  // Populate Task instance with User properties
  const task = await Task.findById("5eace26a6502d80d894820e5");
  await task.populate("owner").execPopulate();
  console.log(task.owner);

  // Populate User instance with Task properties
  const user = await User.findById("5eacde274c3b5c0abd03da03");
  await user.populate("tasks").execPopulate(); // The virtual property 'tasks' is not shown by default when showing up 'user'
  console.log(user.tasks);
};
main();
