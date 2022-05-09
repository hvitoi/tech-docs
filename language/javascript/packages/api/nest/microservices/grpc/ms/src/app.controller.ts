import { Controller, Logger } from '@nestjs/common';
import { MathService } from './math.service';
import { GrpcMethod } from '@nestjs/microservices';

interface INumberArray { 
  data: number[]; // Matches the interface in the proto file!
}
interface ISumOfNumberArray { 
  sum: number; // Matches the interface in the proto file!
} 

@Controller()
export class AppController {
  private logger = new Logger('AppController');

  constructor(private mathService: MathService) {}

  @GrpcMethod('AppController', 'Accumulate') // Mapping to the proto file (Service AppController that has a method Accumulate).
  //@GrpcMethod() // If the names in proto file match the controller and service (like this case). The arguments don't need to be passed
  accumulate(numberArray: INumberArray, metadata: any): ISumOfNumberArray { 
    this.logger.log('Adding ' + numberArray.data.toString());
    return { sum: this.mathService.accumulate(numberArray.data) };
  }
}
