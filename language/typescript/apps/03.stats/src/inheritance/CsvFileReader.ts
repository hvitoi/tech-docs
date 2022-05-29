import fs from 'fs';

// Read and parse the data from the csv file
export abstract class CsvFileReader<T> {
  data: T[] = [];
  constructor(public filename: string) {}
  abstract mapRow(row: string[]): T;

  read(): void {
    this.data = fs
      // Read the file as plain text
      .readFileSync(this.filename, { encoding: 'utf-8' }) // utf-8 returns a string. If not, a buffer with raw data is returned

      // Slipt each row
      .split('\n')

      // Split the elements of each row
      .map((row: string): string[] => row.split(','))

      // Convert each element to the appropriate data type
      .map(this.mapRow);
  }
}
