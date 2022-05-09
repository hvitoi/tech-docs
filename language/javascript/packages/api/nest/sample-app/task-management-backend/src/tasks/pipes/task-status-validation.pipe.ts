import {
  ArgumentMetadata,
  BadRequestException,
  PipeTransform,
} from '@nestjs/common';
import { TaskStatus } from '../task-status.enum';

// Every custom pipe must implement the PipeTransform class
export class TaskStatusValidationPipe implements PipeTransform {
  readonly allowedStatuses = [
    TaskStatus.OPEN,
    TaskStatus.IN_PROGRESS,
    TaskStatus.DONE,
  ];

  // transform() must be implemented for any pipe
  transform(value: any, metadata: ArgumentMetadata) {
    // Transform always receive value and metadata parameters
    // Metadata is optional. In this example it is not being used

    // Transform the status!
    value = value.toUpperCase();

    // Validate the status
    if (!this.isStatusValid(value)) {
      throw new BadRequestException(`"${value}" is an invalid status`);
    }

    // Return the value is validation is ok
    return value;
  }

  // Validate the value
  private isStatusValid(status: any) {
    const index = this.allowedStatuses.indexOf(status);
    return index !== -1;
  }
}
