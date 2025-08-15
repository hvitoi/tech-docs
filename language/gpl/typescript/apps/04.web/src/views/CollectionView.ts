// Models
import { Collection } from '../models/Collection';

// ---

// T is the data class
// K is the data interface
export abstract class CollectionView<T, K> {
  constructor(public parent: Element, public collection: Collection<T, K>) {
    this.enableRefreshOnChange();
  }

  // Methods for the constructor
  enableRefreshOnChange(): void {
    this.collection.on('change', () => {
      this.render();
    });
  }

  // Abstract methods
  abstract renderItem(model: T, itemParent: Element): void;

  render(): void {
    // Clear the current parent
    this.parent.innerHTML = '';

    // Create a template
    const templateElement = document.createElement('template');

    // iterate through all the elements of the collection
    for (let model of this.collection.models) {
      const wrapperElement = document.createElement('div'); // simply a div
      this.renderItem(model, wrapperElement); // render the model inside of the wrapper element
      templateElement.content.append(wrapperElement);
    }

    // Append the result of the loop into the parent
    this.parent.append(templateElement.content);
  }
}
