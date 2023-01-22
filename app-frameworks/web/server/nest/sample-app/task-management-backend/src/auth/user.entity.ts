import {
  BaseEntity,
  Column,
  Entity,
  OneToMany,
  PrimaryGeneratedColumn,
  Unique,
} from 'typeorm';
import * as bcrypt from 'bcrypt';
import { Task } from '../tasks/task.entity';

@Entity()
@Unique(['username']) // config for the table (entity)
export class User extends BaseEntity {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  username: string;

  @Column()
  password: string;

  @Column()
  salt: string;

  // One user can have many tasks
  // (task [the entity task]) => task.user [match with the field user from task]
  @OneToMany((type) => Task, (task) => task.user, { eager: true }) // eager true: whenever we reatrieve the user, we CAN access user.tasks immediately
  tasks: Task[];

  async validatePassword(providedPassword: string): Promise<boolean> {
    const providedPasswordHash = await bcrypt.hash(providedPassword, this.salt);
    return providedPasswordHash == this.password;
  }
}
