# NestJS

- Delete:
  - app.controller.spec.ts
  - app.controller.ts
  - app.service.ts
  - Remove controllers and providers lines from app.module.ts
- Run `npm run start:dev`

- Files:
  - tslinrc.js: Linting configuration file
  - tsconfig.json: How to compile the code
  - tsconfig.build.json: How to compile for production.
  - package.json: Dependencies

## CLI

```shell
# Create new project
nest new "project-name" # Create boilerplate
nest new  "nestjs-task-management"
```

```shell
# Create a module
nest generate "module" "module-name" # g for generate

# Create a controller in a module
nest generate "controller" "controller-name" --no-spec # Additionally add the schematics to the module.ts (imports)

# Create a service in a module
nest generate "service" "service-name" --no-spec # Created as a provider decorated with @Injectable
```

## NestJS modules

- Each application has at least one module (the root module)
- Root module is the starting point of the application
- Modules are `a way to organize componentes by a closely related set of capabilities`
- One folder per module containing the module's components
- Modules are singletons, therefore a module can be imported by multiple other modules
- A module is defined by annotating a class with a `@Module` decorator

```typescript
@Module({
  providers: [ForumService],
  controllers: [ForumController],
  imports: [PostModule, CommentModule, AuthModule],
  exports: [ForumService]
})
export class ForumModule {}
```

## NestJS controllers

- Handle incoming requests and return responses to the client
- `@Controller` decorator

```typescript
@Controller('/tasks')
export class TasksController {
  @Get()
  getAllTasks() {
    // do stuff
    return ...;
  }

  @Post()
  createTask() {
    // do stuff
    return ...;
  }

}
```

- Handlers are the HTTP methods within the controller class

## NestJS Providers

- Can be injected into constructors with `@Injectable` decorator
- `Services are providers`! But not all providers are services
- Services are singletons when wrapped with `@Injectable`. (Same instance will be shared across the application )

## Dependency injection

- Any component can inject a provider that is decorated with `@Injectable`
- We define the dependencies in the constructor of the class

```typescript
import { TasksService } from './tasks.service';

@Controller('/tasks')
export class TasksController {
  constructor(private tasksService: TasksService) {} // Inject the dependency

  @Get()
  async getAllTasks() {
    return await this.tasksService.getAllTasks();
  }
}
```

## Data Transfer Object (DTO)

- A DTO is an object that defines how the data will be sent over the network
- Does not have any behavior except for storage, retrieval, serialization and deserialization of its own data
- Increase the performance
- Useful for data validation
- It's NOT a model definition
- Can be defined using an `interface` or `class`. For NestJS it's recommended using classes

## NestJS Pipes

- Pipes operate on the arguments to be processed by a route handler, just before the handler is called
- Pipes can perform data transformation or data validation
- Pipes can throw exceptions
- Pipes can be asynchronous
- Pipes are middlewares!
- Pipes are annotated with `@Injectable` decoration
- Pipes must implement the `PipeTranform` generic interface (every pipe must have `transform()` method)
  - `transform()` accept `value` and `metadata`
  - Whatever is passed to `transform()` will be passed to the router handler
- Pipes consuming:

  - `Handler-level pipes`: at the handler level using `@UsePipes`. Can be used with DTOs

  ```typescript
  @Post()
  @UsePipes(SomePipe)
  createTask(
    @Body('description') description
  ) {
    // ...
  }
  ```

  - `Parameter-level pipes`: Only specific parameters will be processed

  ```typescript
  @Post()
  createTask(
    @Body('description', SomePipe) description
  ) {
    // ...
  }
  ```

- `Global pipes`: Defined at the application level, applied to any incoming request

  ```typescript
  async function bootstrap() {
    const app = await NestFactory.create(ApplicationModule);
    app.useGlobalPipes(SomePipe);
    await app.listen(3000);
  }
  bootstrap();
  ```

### Pipes packages

- `npm install class-validator`: Class validator decorators. E.g., @IsNotEmpty(), @IsOptional(), @IsIn()
- `npm install class-transformer`

## Object Relational Mapping (ORM)

- Technique to query and manipulate from a database using OOP
- Communication with the DB using their preferred language instead of SQL
- Pros: less repetition, abstraction, no need for SQL, inheritance easy to achieve
- Cons: less performance
- `npm i typeorm`: ORM library for TS
- TypeORM uses `entities` as the unit for manipulation
  - <https://github.com/typeorm/typeorm/blob/master/docs/entities.md>
- TypeORM uses `repositories` as the unit for the connection between the model (entity) and its correspondent in the DB

  - <http://typeorm.delightful.studio/classes/_repository_repository_.repository.html>

- Deploy a Postgres server

```sh
docker run \
  --name my-postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 \
  -d \
  postgres:13.1
# A database 'taskmanagement' must be created!
```

```typescript
// typeorm
const tasks = await Task.find({ status: 'DONE', user: 'Ashley' });

// sql
let tasks;
db.query(
  `SELECT * FROM tasks WHERE status = 'DONE' AND user = 'Ashley'`,
  (err, res) => {
    if (err) throw new Error('Could not retrieve tasks!');
    tasks = res.rows;
  }
);
```

```shell
npm i @nestjs/typeorm # bridge to nestjs to integrate with nestjs
npm i typeorm # actual typeorm module
npm i pg # database driver for postgres
```

- TypeORM configuration in NestJS

```typescript
import { TypeOrmModuleOptions } from '@nestjs/typeorm';

export const typeOrmConfig: TypeOrmModuleOptions = {
  type: 'postgres',
  host: 'localhost',
  port: 5432,
  username: 'postgres',
  password: 'postgres',
  database: 'taskmanagement',
  entities: [__dirname + '/../**/*.entity.{js,ts}'],
  synchronize: true
};
```

- Import module in app.module.ts

```typescript
import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { typeOrmConfig } from './config/typeorm.config';

// App module is the root module
@Module({
  imports: [TypeOrmModule.forRoot(typeOrmConfig)]
})
export class AppModule {}
```

## JWT (Json web token)

- **Header**: metadata about the token (type, hashing alg, etc)
- **Payload**: Contains claims
- **Signature**: the encoded header and payload, signed against a secret

- The validate() method must be defined in the JWT Strategy!

## Logger

```typescript
private logger = new Logger('TasksController'); // Set the context here

// Verbose
this.logger.verbose(
  `User "${user.username}" retrieving all tasks. Filters: ${JSON.stringify(
    filterDto,
  )}.`,
);

// Error
this.logger.error(
  `Failed to get tasks for user "${user.username}", DTO: ${JSON.stringify(
    filterDto,
  )}`,
  err.stack, // 2nd parameter is the error from the catch block
);

// Debug
this.logger.debug(
  `Generated JWT token with payload ${JSON.stringify(payload)} `,
);
```

## Environemnt variables

```sh
# Define envs on the fly
PORT=3001 npm run start:dev
```

## Testing

```typescript
class FriendsList {
  friends = [];

  addFriend(name) {
    this.friends.push(name);
    this.announceFriendship(name);
  }

  announceFriendship(name) {
    global.console.log(`${name} is now a friend!`);
  }

  removeFriend(name) {
    const idx = this.friends.indexOf(name);

    if (idx === -1) {
      throw new Error('Friend not found');
    }

    this.friends.splice(idx, 1);
  }
}

describe('FriendsList', () => {
  let friendsList;

  beforeEach(() => {
    friendsList = new FriendsList();
  });

  it('initializes friends list', () => {
    expect(friendsList.friends.length).toEqual(0);
  });

  it('adds a friend to the list', () => {
    friendsList.addFriend('Henrique');
    expect(friendsList.friends.length).toEqual(1);
  });

  it('announces friendship', () => {
    friendsList.announceFriendship = jest.fn(); // Mock the function
    expect(friendsList.announceFriendship).not.toHaveBeenCalled();
    friendsList.addFriend('Henrique');
    expect(friendsList.announceFriendship).toHaveBeenCalled();
    expect(friendsList.announceFriendship).toHaveBeenCalledTimes(1);
    expect(friendsList.announceFriendship).toHaveBeenCalledWith('Henrique');
  });

  describe('removeFriend', () => {
    it('removes a friend from the list', () => {
      friendsList.addFriend('Henrique');
      expect(friendsList.friends[0]).toEqual('Henrique');
      friendsList.removeFriend('Henrique');
      expect(friendsList.friends[0]).toBeUndefined();
    });

    it('throws an error as friend does not exist', () => {
      expect(() => friendsList.removeFriend('Henrique')).toThrow();
      expect(() => friendsList.removeFriend('Henrique')).toThrow(Error);
      expect(() => friendsList.removeFriend('Henrique')).toThrow(
        new Error('Friend not found')
      );
    });
  });
});
```

### Mocks

```typescript
jest.fn().mockResolvedValue(true); // Promise response
jest.fn().mockRejectedValue({ code: '23505' }); // Throw response with  code error
jest.fn().mockReturnValue({ save }); // no async
```

### Expects

```typescript
expect(fn).toHaveBeenCalled();
expect(fn).not.toHaveBeenCalled();
expect(fn).toHaveBeenCalledWith(params);
expect(result).toEqual('x');
expect(result).toMatchObject({ x: 'blabla', y: 'bleble' });
expect(fn).rejects.toThrow(); // Throw error (any)
expect(fn).rejects.toThrow(NotFoundException);
expect(fn).resolves.not.toThrow(); // resolves successfully
```

### Handle exception

```typescript
test('should return a exception when doesnt create a user', async () => {
  const user = TestUtil.giveMeAValidUse();
  mockRepository.save.mockReturnValue(null);
  mockRepository.create.mockReturnValue(user);

  await service.createUser(user).catch((e) => {
    expect(e).toBeInstanceOf(InternalServerErrorException);
    expect(e).toMatchObject({ message: 'Erro to create user' });
  });
  expect(mockRepository.create).toBeCalledTimes(1);
  expect(mockRepository.save).toBeCalledTimes(1);
});
```
