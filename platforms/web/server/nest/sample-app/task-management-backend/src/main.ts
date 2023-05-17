import { NestFactory } from '@nestjs/core';
import { Logger } from '@nestjs/common';
import { AppModule } from './app.module';
import * as config from 'config';

async function bootstrap() {
  //Environment variables
  const serverConfig = config.get('server');

  // Setup
  const logger = new Logger('bootstrap');
  const app = await NestFactory.create(AppModule);

  // Cors
  if (process.env.NODE_ENV === 'development') {
    app.enableCors();
  }

  // Listen
  const port = process.env.PORT || serverConfig.port;
  await app.listen(port);
  logger.log(`Application listening on port ${port}`);
}
bootstrap();
