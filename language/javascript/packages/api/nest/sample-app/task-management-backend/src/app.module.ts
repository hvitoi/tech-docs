import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { typeOrmConfig } from './config/typeorm.config';
import { TasksModule } from './tasks/tasks.module';
import { AuthModule } from './auth/auth.module';

// App module is the root module
@Module({
  imports: [TypeOrmModule.forRoot(typeOrmConfig), TasksModule, AuthModule],
})
export class AppModule {}
