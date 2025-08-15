export abstract class Sorter {
  //constructor(public collection: number[] | string) {} // This is not a good approach because they have few properties and methods in common
  //constructor(public collection: Sortable) {} // Commented because Sorter will only be used as a parent class

  abstract compare(leftIndex: number, rightIndex: number): boolean;
  abstract swap(leftIndex: number, rightIndex: number): void;
  abstract length: number;

  sort(): void {
    let { length } = this; // Destructuring the 'this' object
    while (length > 1) {
      for (let i = 0; i < length - 1; i++) {
        if (this.compare(i, i + 1)) {
          this.swap(i, i + 1);
        }
      }
      length--;
    }
  }
}
