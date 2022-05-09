// Utils
import { stringToDate } from './utils';

// Enumerations
import { FootballResult } from './FootballResult';

// Types & Interfaces
import { FootballData } from './FootballData';

import { CsvFileReader } from './CsvFileReader';

// ---

// Interface DataReader
interface DataReader {
  read(): void;
  data: string[][];
}

// ---

export class FootballReader {
  static fromCsv(filename: string): FootballReader {
    return new FootballReader(new CsvFileReader(filename));
  }
  matches: FootballData[] = [];
  constructor(public reader: DataReader) {}

  load(): void {
    this.reader.read();
    this.matches = this.reader.data.map(
      (row: string[]): FootballData => {
        return [
          stringToDate(row[0]), // date
          row[1], // string
          row[2], // string
          parseInt(row[3]),
          parseInt(row[4]),
          row[5] as FootballResult, // 'H', 'A' or 'D'
          row[6] // string
        ];
      }
    );
  }
}
