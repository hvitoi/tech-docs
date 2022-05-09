import { OutputTarget } from '../Summary'; // interface to output

export class ConsoleReport implements OutputTarget {
  print(report: string): void {
    console.log(report);
  }
}
