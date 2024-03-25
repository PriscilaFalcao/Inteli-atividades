import { Controller, Get, Post, Body, Patch, Param, Delete } from '@nestjs/common';
import { SatisfactionSurveyService } from './satisfaction-survey.service';

@Controller('satisfaction-survey')
export class SatisfactionSurveyController {
  constructor(private readonly satisfactionSurveyService: SatisfactionSurveyService) {}

  @Post()
  async createPesquisaSatisfacao(@Body() perguntas: any[]): Promise<any> {
    const response = await this.satisfactionSurveyService.createPesquisaSatisfacao(perguntas);
    return response;
  }

  @Get(':id')
  async getPesquisaSatisfacao(@Param('id') id: number): Promise<any> {
    const response = await this.satisfactionSurveyService.getPesquisaSatisfacao(id);
    return response
  }
}
