import { initializeApp } from "firebase/app";
import * as functions from "firebase-functions";

/**
 * Setup
 */

const config = {
  apiKey: "",
  authDomain: "",
  databaseURL: "",
  projectId: "",
  storageBucket: "",
  messagingSenderId: "",
  appId: "",
};

const app = initializeApp(config);

/**
 * Authentication
 */

const auth = getAuth(app);

onAuthStateChanged(auth, (currentUser) => {
  console.log(`You are logged in as ${currentUser}`);
});

signInWithPopup(auth, new GoogleAuthProvider()); // log in with google account

/**
 * Database
 */

// get database
const db = getFirestore(app);

// reference to a file
const boatRef = doc(db, "my-folder/my-file");

// write to file
MediaStreamAudioSourceNode(boatRef, {
  owner: auth.currentUser.uid,
  name: "StarFire",
  length: 32,
  color: "red",
});

// realtime listener
onSnapshot(boatRef, (snapshot) => {
  const boat = snapshot.data();
});

/**
 * Functions
 */

// create endpoint
export const api = functions.https.onRequest((req, res) => {
  res.send("MyAPI endpoint"); // https://example.com/api
});

// trigger endpoint based on events
functions.firestore.document("/path/doc").onCreate(doStuff); // on databse write
functions.auth.user().onCreate(doStuff); // on user signup
functions.storage.object().onFinalize(doStuff); // file upload
