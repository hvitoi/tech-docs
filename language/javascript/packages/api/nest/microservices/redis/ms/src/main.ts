import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { Logger } from '@nestjs/common';
import { Transport } from '@nestjs/microservices';
import { MicroserviceOptions } from '@nestjs/common/interfaces/microservices/microservice-configuration.interface';

// Create a logger instance
const logger = new Logger('Main');

// Create the microservice options object
const microserviceOptions: MicroserviceOptions = {
  transport: Transport.REDIS,
  options: {
    url: 'redis://10.129.174.219:32555',
  },
};

async function bootstrap() {
  const app = await NestFactory.createMicroservice(
    AppModule,
    microserviceOptions,
  );
  app.listen(() => {
    logger.log('Microservice is listening...');
  });
}
bootstrap();
