// satisfaction-survey.service.ts
import { Injectable, NotFoundException } from '@nestjs/common';
import { PrismaService } from '../prisma.service';

@Injectable()
export class SatisfactionSurveyService {
  constructor(private prisma: PrismaService) {}

  async createPesquisaSatisfacao(questionsAndAnswers: any[]): Promise<any> {
    try {
      const createdSurvey = await this.prisma.satisfactionSurvey.create({
        data: {
          questionsAndAnswers: questionsAndAnswers,
        },
      });
      return createdSurvey;
    } catch (error) {
      console.error(`Error creating satisfaction survey: ${error}`);
      return null;
    }
  }

  async getPesquisaSatisfacao(id: number): Promise<any> {
    try {
      const retrievedSurvey = await this.prisma.satisfactionSurvey.findUnique({
        where: {
          id: id,
        },
      });
      return retrievedSurvey;
    } catch (error) {
      console.error(`Error getting satisfaction survey by ID: ${error}`);
      return null;
    }
  }
}
