# Firebase

- Create new project: <https://console.firebase.google.com/>
- Enable `google analytics` at the creation of the project

## Android app

- The package name of the app must be the same as defined in `android/app/main/AndroidManifest.xml`

### android/app/google-services.json

- Save the `google-services.json` file into your computer (it's shown once at the firebase project creation)
- It's the config file for a firebase project
- It contains the authentication key in order to connect to firebase servers
- Move it to `android/app/google-services.json`
- Add it to `.gitignore`

### android/build.gradle

- Modify `android/build.gradle` to add the google-services dependency

```groovy
buildscript {
  repositories {
    google()  // google's maven repository
  }
  dependencies {
    classpath 'com.google.gms:google-services:4.3.10' // firebase core
    classpath 'com.google.firebase:firebase-crashlytics-gradle:2.8.1'

  }
}
allprojects {
  repositories {
    google()
  }
}
```

### android/app/build.gradle

- Modify `android/app/build.gradle`

```groovy
apply plugin: 'com.android.application'
apply plugin: 'com.google.gms.google-services'
apply plugin: 'com.google.firebase.crashlytics'

dependencies {
  // Firebase BoM
  // When using the BoM, don't specify versions in Firebase dependencies
  implementation platform('com.google.firebase:firebase-bom:29.3.1')

  implementation 'com.google.firebase:firebase-analytics-ktx'
  implementation 'com.google.firebase:firebase-crashlytics-ktx'

  // Add the dependencies for any other desired Firebase products
  // https://firebase.google.com/docs/android/setup#available-libraries
}

```

## Web App

- It's possible to install the sdk using `npm` (serverside and spa) or using `script html tags`
- For webapps, you have to generate `web push certificates`
  - The web push certificate is used in order to retrieve a `token` from FCM server
  - `messaging.getToken(vapidKey: 'webpushcertificate');`
- For web apps, permissions to receive notifications are also required in the browser
  - Notifications in web browsers are integrated with the operating system

### web/index.html

```html
<!DOCTYPE html>r
<html>
  <head>
    <meta charset="UTF-8" />
    <title>example</title>
  </head>

  <body>
    <script src="main.dart.js" type="application/javascript"></script>
    <script>
      var serviceWorkerVersion = null;
      var scriptLoaded = false;
      function loadMainDartJs() {
        if (scriptLoaded) {
          return;
        }
        scriptLoaded = true;
        var scriptTag = document.createElement("script");
        scriptTag.src = "main.dart.js";
        scriptTag.type = "application/javascript";
        document.body.append(scriptTag);
      }

      if ("serviceWorker" in navigator) {
        // Service workers are supported. Use them.
        window.addEventListener("load", function () {
          //register firebase-messaging service worker
          navigator.serviceWorker.register("/firebase-messaging-sw.js");
          // Wait for registration to finish before dropping the <script> tag.
          // Otherwise, the browser will load the script multiple times,
          // potentially different versions.
          var serviceWorkerUrl =
            "flutter_service_worker.js?v=" + serviceWorkerVersion;

          navigator.serviceWorker.register(serviceWorkerUrl).then((reg) => {
            function waitForActivation(serviceWorker) {
              serviceWorker.addEventListener("statechange", () => {
                if (serviceWorker.state == "activated") {
                  console.log("Installed new service worker.");
                  loadMainDartJs();
                }
              });
            }
            if (!reg.active && (reg.installing || reg.waiting)) {
              // No active web worker and we have installed or are installing
              // one for the first time. Simply wait for it to activate.
              waitForActivation(reg.installing ?? reg.waiting);
            } else if (!reg.active.scriptURL.endsWith(serviceWorkerVersion)) {
              // When the app updates the serviceWorkerVersion changes, so we
              // need to ask the service worker to update.
              console.log("New service worker available.");
              reg.update();
              waitForActivation(reg.installing);
            } else {
              // Existing service worker is still good.
              console.log("Loading app from service worker.");
              loadMainDartJs();
            }
          });

          // If service worker doesn't succeed in a reasonable amount of time,
          // fallback to plaint <script> tag.
          setTimeout(() => {
            if (!scriptLoaded) {
              console.warn(
                "Failed to load app from service worker. Falling back to plain <script> tag."
              );
              loadMainDartJs();
            }
          }, 4000);
        });
      } else {
        // Service workers not supported. Just drop the <script> tag.
        loadMainDartJs();
      }
    </script>
  </body>
</html>
```

### web/firebase-messaging-sw.js

- It's a `service worker` service
- It will run in background in your browser, listening for new notifications

```javascript
importScripts("https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js");
importScripts(
  "https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js"
);

firebase.initializeApp({
  apiKey: "myapikey",
  authDomain: "mydomain.firebaseapp.com",
  databaseURL: "myurl",
  projectId: "myprojectid",
  storageBucket: "mybucket.appspot.com",
  messagingSenderId: "mysenderid",
  appId: "myappid",
});
// Necessary to receive background messages:
const messaging = firebase.messaging();

// Optional:
messaging.onBackgroundMessage((m) => {
  console.log("onBackgroundMessage", m);
});
```
