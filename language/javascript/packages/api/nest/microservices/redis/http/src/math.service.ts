import { Injectable } from '@nestjs/common';
import { MicroserviceOptions } from '@nestjs/common/interfaces/microservices/microservice-configuration.interface';
import {
  ClientProxyFactory,
  Transport,
  ClientProxy,
} from '@nestjs/microservices';

@Injectable()
export class MathService {
  private client: ClientProxy;

  constructor() {
    this.client = ClientProxyFactory.create({
      transport: Transport.REDIS,
      options: {
        url: 'redis://10.129.174.219:32555',
      },
    });
  }

  public accumulate(data: number[]) {
    // send<ReturnType,ParamType>(pattern, param)
    return this.client.send<number, number[]>('add', data);
  }
}
