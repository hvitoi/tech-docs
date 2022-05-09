import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from '../auth/user.entity';
import { CreateTaskDto } from './dto/create-task.dto';
import { GetTasksFilterDto } from './dto/get-tasks-filter.dto';
import { TaskStatus } from './task-status.enum';
import { Task } from './task.entity';
import { TaskRepository } from './task.repository';

@Injectable()
export class TasksService {
  constructor(
    // The repository must be injected in the constructor of the service
    @InjectRepository(TaskRepository)
    private taskRepository: TaskRepository,
  ) {}

  async getTasks(filterDto: GetTasksFilterDto, user: User): Promise<Task[]> {
    return this.taskRepository.getTasks(filterDto, user);
  }

  // GetTasksWithFilters(filterDto: GetTasksFilterDto): Task[] {
  //   const { status, search } = filterDto;
  //   // Copy the array of all tasks
  //   let tasks = this.getAllTasks();
  //   // If there is status in the query
  //   if (status) {
  //     tasks = tasks.filter((task) => task.status === status);
  //   }
  //   // If there is search in the query
  //   if (search) {
  //     tasks = tasks.filter((task) => {
  //       if (task.title.includes(search) || task.description.includes(search))
  //         return true; // If the title or the description has the keyword of the search, then include the task
  //     });
  //   }
  //   // Return the filtered array
  //   return tasks;
  // }
  async getTaskById(id: number, user: User): Promise<Task> {
    const task = await this.taskRepository.findOne({
      where: { id, userId: user.id },
    }); // Where clauses in TypeORM
    //const task = this.tasks.find((task) => task.id === id); // From array
    if (!task) {
      throw new NotFoundException(`Task with ID "${id}" not found`); // Error Classes built-in. NotFoundExpection() throws generic message
    }
    // 404 is returned even if the task exists but belongs to another user
    return task;
  }

  async createTask(createTaskDto: CreateTaskDto, user: User): Promise<Task> {
    // Create task from the repository custom method
    return this.taskRepository.createTask(createTaskDto, user);

    // Create task with array db
    //   const task: Task = {
    //     id: uuidv4(),
    //     title,
    //     description,
    //     status: TaskStatus.OPEN,
    //   };
    //   // Push task
    //   this.tasks.push(task);
    //   return task;
  }

  async deleteTask(id: number, user: User): Promise<void> {
    // the delete method is already implemented by typeorm
    const result = await this.taskRepository.delete({ id, userId: user.id }); // the taskRepository.remove() method takes as parameter the object (or array of objects) itself. The delete() takes the id
    //console.log(result); // DeleteResult { raw: [], affected: 1 }
    if (result.affected === 0) {
      throw new NotFoundException(`Task with ID "${id}" not found`);
    }
    //   this.tasks = this.tasks.filter((task) => task.id !== foundTask.id); // Filter only the tasks that doesn't have the id
  }

  async updateTaskStatus(
    id: number,
    status: TaskStatus,
    user: User,
  ): Promise<Task> {
    const task = await this.getTaskById(id, user);
    task.status = status;
    await task.save();
    return task;
  }
}
