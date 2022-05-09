// Classes
import { CsvFileReader } from './CsvFileReader';

// Enumerations
import { FootballResult } from './FootballResult';

// Functions
import { stringToDate } from './utils';

// ---

// [0] Date of the match
// [1] Home team
// [2] Away team
// [3] Home team score
// [4] Away team score
// [5] Who won? H (home), A (away), D (draw)
// [6] Stadium

// ---

// Create the tuple type annotation for FootballData
type FootballData = [
  Date,
  string,
  string,
  number,
  number,
  FootballResult,
  string
];

export class FootballReader extends CsvFileReader<FootballData> {
  // Implementing the abstract method
  mapRow(row: string[]): FootballData {
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
}
