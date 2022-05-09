# nuvigator

- Allows using named routes (`deeplinks`)
- It's a centralized mechanism for navigating thoughout the app
- With nuvigator the responsibility for the navigation no longer belongs to the widget
- To register a new route, it must be added to the `router`

## Deeplink

- Allows redirection to a mobile page (instead of opening it in the browser)
- **URI Schemes**
  - Tt's like a internal DNS in your phone
  - Interpret deeplinks like `myapp://products`
  - Interpret deeplinks like `http://myapp.com/products` (when com.myapp is the package name of the app).
- In mobile devices, deeplinks have an extra function which is to identify the app that this link must be opened with

## Universal link

- `Universal link` (for Apple)
- `Android app link` (for Android)

- Transforms a plain internet URL (e.g., <https://instagram.com>) in a deeplink
- The OS figures out that it is meant to be opened in an app and creates a deeplink from it
