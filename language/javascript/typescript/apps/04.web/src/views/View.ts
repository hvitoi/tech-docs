// Models
import { Model } from '../models/Model';

// ---

// T is the class of the Data! (e.g. User)
// K is the properties of the Data (e.g. UserProps)
export abstract class View<T extends Model<K>, K> {
  // Abstract methods
  abstract template(): string;

  // Regions are the child instances that are deep nested in the current instance
  // regions: { userShow: HTMLElement, userForm: HTMLElement }
  regions: { [key: string]: Element } = {};

  // Region-Class Mapping for regions contained in the current class
  // This property might be overridden by the child classes
  // getCurrentRegions() => { userShow: 'user-show', userForm: 'user-form' }
  getCurrentRegions(): { [key: string]: string } {
    return {}; // Blank by default
  }

  // constructor
  constructor(public parent: Element, public dataModel: T) {
    this.enableRefreshOnChange();
  }

  // ---

  // Methods for the constructor
  enableRefreshOnChange(): void {
    this.dataModel.on('change', () => {
      this.render();
    });
  }
  // - Dummy methods

  // Bare implementation of eventsMap. The child classes will override this function
  eventsMap(): { [key: string]: () => void } {
    return {};
  }

  // ---

  // Bind events to the HTML Document Fragments (the tags)
  bindEvents(fragment: DocumentFragment): void {
    const eventsMap = this.eventsMap(); // Returns the events object

    for (let key in eventsMap) {
      // Split the 'click' from the 'button' (click:button)
      const [eventName, elementSelector] = key.split(':');

      // Returns the array of elements that matches the elementSelector. The elementSelector can be a elementName(button, input) or a elementClass (.set-age, .set-name, etc) or an elementId(#root, #modal)
      const elements = fragment.querySelectorAll(elementSelector); // E.g. button1, button2, button3...

      // Iterate over the elements and add a event for each element
      elements.forEach((element) => {
        element.addEventListener(eventName, eventsMap[key]);
      });
    }
  }

  mapRegions(fragment: DocumentFragment): void {
    // Populate the 'regions'
    // Initially it only has 'key' and 'class'. 'Element' must be populated
    const currentRegions = this.getCurrentRegions();

    for (let key in currentRegions) {
      const classSelector = currentRegions[key]; // extract the class
      const element = fragment.querySelector(classSelector); // find the element for that class
      if (element) {
        this.regions[key] = element; // save the element
      }
    }
  }

  onRender(): void {} // DUmmy function. Just to do not have to implement in every child class

  // Template rendering
  render(): void {
    // Clear the parent element before building it
    this.parent.innerHTML = '';

    // Create a HTML template (tag <template></template>). Type HTMLTemplateElement
    const templateElement = document.createElement('template');

    // Push the HTML string into the HTML template
    templateElement.innerHTML = this.template();

    // Add events for the appropriate elements
    this.bindEvents(templateElement.content);

    // Populate the 'regions'. Associate the element to each region in the fragment
    this.mapRegions(templateElement.content);

    // This is the nesting function! Helper method to be called right before the text is appended to the DOM
    this.onRender();

    // Append the HTML template into the HTML element
    this.parent.append(templateElement.content); // content is of type DocumentFragment
  }
}
