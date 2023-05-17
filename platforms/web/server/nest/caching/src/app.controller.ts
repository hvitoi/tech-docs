import { Controller, Get, Body } from '@nestjs/common';
import { AppService, User } from './app.service';

interface Response {
  data: string | User;
  loadsFrom: string;
}
@Controller()
export class AppController {
  constructor(private appService: AppService) {}

  @Get('getString')
  async getString(@Body() { name }: { name: string }): Promise<Response> {
    const res = await this.appService.getString(name);
    return res;
  }

  @Get('getObject')
  async getObject(@Body() { name }: { name: string }): Promise<Response> {
    const res = await this.appService.getObject(name);
    return res;
  }

  @Get('deleteCache')
  async deleteCache(): Promise<void> {
    await this.appService.resetCache();
  }
}
