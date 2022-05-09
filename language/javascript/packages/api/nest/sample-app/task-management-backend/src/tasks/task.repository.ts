import { Task } from './task.entity';
import { EntityRepository, Repository } from 'typeorm';
import { CreateTaskDto } from './dto/create-task.dto';
import { TaskStatus } from './task-status.enum';
import { GetTasksFilterDto } from './dto/get-tasks-filter.dto';
import { User } from '../auth/user.entity';
import { InternalServerErrorException, Logger } from '@nestjs/common';

// The TaskRepository imports the task entity with its properties
@EntityRepository(Task)
export class TaskRepository extends Repository<Task> {
  private logger = new Logger('TaskRepository');
  async getTasks(filterDto: GetTasksFilterDto, user: User): Promise<Task[]> {
    const { status, search } = filterDto;

    // Manual query builder from repository
    const query = this.createQueryBuilder('task'); //keyword

    // Filter only task from a specific user
    query.where('task.userId = :userId', { userId: user.id });

    // Status filter
    if (status) {
      query.andWhere('task.status = :status', { status }); // Where clause for SQL. andWhere (different from where) does not override the previous where clause
    }

    // Search filter
    if (search) {
      query.andWhere(
        'task.title LIKE :search OR task.description LIKE :search',
        { search: `%${search}%` }, // %keyword% for LIKE statement in SQL
      );
    }

    // Query!!
    try {
      const tasks = await query.getMany(); // get all with the filters
      return tasks;
    } catch (err) {
      this.logger.error(
        `Failed to get tasks for user "${user.username}", DTO: ${JSON.stringify(
          filterDto,
        )}`,
        err.stack,
      );
      throw new InternalServerErrorException();
    }
  }

  async createTask(createTaskDto: CreateTaskDto, user: User): Promise<Task> {
    // Create task directly from the entity
    const task = new Task();

    // Extract the keys you care about from the DTO
    const { title, description } = createTaskDto;

    // Assign properties
    task.title = title;
    task.description = description;
    task.status = TaskStatus.OPEN;
    task.user = user;

    // Save
    try {
      await task.save();
      delete task.user; // Delete the user prop before the return. It's not deleted from the database!
      return task;
    } catch (err) {
      this.logger.error(
        `Failed to create a task for user "${user.username}". Data: ${createTaskDto}.`,
        err.stack,
      );
      throw new InternalServerErrorException();
    }
  }
}
