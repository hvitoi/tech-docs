import faker from 'faker';
import { Mappable } from './CustomMap';

// Convention in TS to never export default
export class User implements Mappable {
  name: string;
  location: {
    lat: number;
    lng: number;
  };
  color: string = 'green';
  // At that point name and location do not exist yet (undefined)

  constructor() {
    // Initialization of the variables and objects
    this.name = faker.name.firstName(); // Ctrl+Click to check up the definition file
    this.location = {
      lat: parseFloat(faker.address.latitude()), // Converts the string (from faker) to float (for class)
      lng: parseFloat(faker.address.longitude())
    };
  }

  markerContent(): string {
    return `User Name: ${this.name}`;
  }
}
