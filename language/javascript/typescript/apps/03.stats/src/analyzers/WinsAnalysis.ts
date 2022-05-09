// Types & Interfaces & Enums
import { Analyzer } from '../Summary';
import { FootballData } from '../FootballData';
import { FootballResult } from '../FootballResult';

// ---

export class WinsAnalysis implements Analyzer {
  constructor(public team: string) {}

  run(matches: FootballData[]): string {
    // Analyse data
    let wins = 0;
    for (let match of matches) {
      if (match[1] === this.team && match[5] === FootballResult.HomeWin) wins++;
      else if (match[2] === this.team && match[5] === FootballResult.AwayWin)
        wins++;
    }
    return `Team ${this.team} won ${wins} matches.`;
  }
}
