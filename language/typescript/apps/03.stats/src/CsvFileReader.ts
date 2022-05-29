import fs from 'fs';

// Read and parse the data from the csv file
export class CsvFileReader {
  data: string[][] = [];
  constructor(public filename: string) {}

  read(): void {
    this.data = fs

      // Read the file as plain text
      .readFileSync(this.filename, {
        encoding: 'utf-8' // Return a string. If not, a buffer with raw data would be retrieved
      })

      // Slipt each row
      .split('\n')

      // Split the elements of each row
      .map((row: string): string[] => row.split(','));
  }
}
