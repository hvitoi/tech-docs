import { IsIn, IsNotEmpty, IsOptional } from 'class-validator';
import { TaskStatus } from '../task-status.enum';

export class GetTasksFilterDto {
  @IsOptional()
  @IsIn([TaskStatus.OPEN, TaskStatus.IN_PROGRESS, TaskStatus.DONE]) // Check if the status is in the array provided
  status: TaskStatus;

  @IsOptional()
  @IsNotEmpty()
  search: string;
}
