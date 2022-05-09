import { FootballData } from './FootballData';
import { WinsAnalysis } from './analyzers/WinsAnalysis';
import { HtmlReport } from './reportTargets/HtmlReport';

// Interface to analyze a string
export interface Analyzer {
  run(matches: FootballData[]): string;
}

// Interface to output a result
export interface OutputTarget {
  print(report: string): void;
}

// ---
// On instantiation of Summary a 'Analyzer object' and a 'OutputTarget object' must be passed
export class Summary {
  constructor(public analyzer: Analyzer, public outputTarget: OutputTarget) {}

  buildAndPrintReport(matches: FootballData[]): void {
    const output = this.analyzer.run(matches);
    this.outputTarget.print(output);
  }

  static winsAnalysisWithHtmlReport(team: string): Summary {
    return new Summary(new WinsAnalysis(team), new HtmlReport());
  }
}
