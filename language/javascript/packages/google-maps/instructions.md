# Google Maps Api

## Google Developers console

- Access the [Developers Console](https://console.developers.google.com/)
- Create a new project
- Access the [Library API](https://console.developers.google.com/apis/library)
- Enable the `Maps JavaScript API`
- Generate API key under [Credentials](https://console.developers.google.com/apis/credentials)
  - Create credentials (API key)
- Copy the API key

## GMaps script to HTML

- Add the gmaps script above the other js scripts
- Create a div with an id to place the map

```html
<body>
  <div id="map" style="height: 100vh;"></div>
  <script src="https://maps.googleapis.com/maps/api/js?key=yourapikey"></script>
  <script src="./src/index.ts"></script>
</body>
```

## Typescript support

- Install @types/googlemaps for TS support in the project
- Add the following statement to the top of the index.ts

  ```typescript
  /// <reference types="@types/googlemaps" />
  ```

- Or create a tsconfig.json at the root folder with the following

  ```json
  {
    "types": ["google"]
  }
  ```

- 'google' will work as a global variable
