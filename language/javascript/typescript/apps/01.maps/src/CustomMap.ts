// Interface in order to satisfy the addMarker parameter
export interface Mappable {
  location: {
    lat: number;
    lng: number;
  };
  markerContent(): string;
  color: string;
}

// The CustomMap removes some properties from the original Google Maps element
export class CustomMap {
  private googleMap: google.maps.Map;

  constructor(divId: string) {
    // Create an instance of the map class
    // First arg is the div and the second is an object with options. Ctrl+Click to see the available options
    this.googleMap = new google.maps.Map(document.getElementById(divId), {
      // properties with ? are optional
      zoom: 1,
      center: {
        lat: 0,
        lng: 0
      }
    });
  }

  // Unified method to add both User or Company
  addMarker(mappable: Mappable): void {
    // Create the marker
    const marker = new google.maps.Marker({
      map: this.googleMap,
      position: {
        lat: mappable.location.lat,
        lng: mappable.location.lng
      }
    });

    // Create the InfoWindow
    marker.addListener('click', () => {
      const infoWindow = new google.maps.InfoWindow({
        content: mappable.markerContent()
      });
      infoWindow.open(this.googleMap, marker);
    });
  }
}
