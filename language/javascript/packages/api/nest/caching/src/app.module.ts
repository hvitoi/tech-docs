import { Module, CacheModule, CacheModuleOptions } from '@nestjs/common';
import * as redisStore from 'cache-manager-redis-store';
import { AppController } from './app.controller';
import { AppService } from './app.service';

const redisCacheOptions: CacheModuleOptions = {
  store: redisStore,
  host: '10.129.174.219',
  port: '32555',
};

const localCacheOptions: CacheModuleOptions = {
  store: 'memory',
};

@Module({
  imports: [CacheModule.register([localCacheOptions, redisCacheOptions])],
  // imports: [
  //   CacheModule.registerAsync({
  //     useFactory: () => {
  //       return localCacheOptions;
  //     },
  //   }),
  // ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
