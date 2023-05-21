import { CACHE_MANAGER, Inject, Injectable } from '@nestjs/common';
import { Cache, MultiCache } from 'cache-manager';

export interface User {
  name: string;
  email: string;
}

@Injectable()
export class AppService {
  constructor(@Inject(CACHE_MANAGER) private cacheManager: MultiCache) {}

  async getString(name): Promise<any> {
    // Cached value
    const cachedValue = await this.cacheManager.get('my-string');
    if (cachedValue) {
      return {
        data: cachedValue,
        loadsFrom: 'cache',
      };
    }

    // Fresh value
    const value = name;
    await this.cacheManager.set('my-string', value, { ttl: 300 });
    return {
      data: value,
      loadsFrom: 'fresh',
    };
  }

  async getObject(name): Promise<any> {
    // Cached value
    const cachedValue = await this.cacheManager.get<User>('my-object');
    if (cachedValue) {
      return {
        data: cachedValue,
        loadsFrom: 'cache',
      };
    }

    // Fresh value
    const value: User = {
      name: name,
      email: name + '@' + name + '.com',
    };
    await this.cacheManager.set('my-object', value, { ttl: 300 });
    return {
      data: value,
      loadsFrom: 'fresh',
    };
  }

  async resetCache() {
    await this.cacheManager.del('my-string');
    await this.cacheManager.del('my-object');
    //await this.cacheManager.reset(); // Clear all keys
  }
}
