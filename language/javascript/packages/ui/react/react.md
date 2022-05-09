# Create React project

npx create-react-app <app-name>

# Start project

npm start

# Component

A component is either a function or a class

# Three Tenets of Components

Nesting, Resuability, Configuration

# Kill busy port

lsof -i tcp:3000
kill -9 PID

# Standardization for components name

CommentDetail.js

# Props (properties)

System for passing data from a parent to a child component

# Rules of State

JS object with data for a component
Updating state rerender the component
State can only be updated with 'setState'

# Lifecycle methods

Function that can be defined in the class component
It's called at certains moments in the lifecycle

# Component Lifecycle

constructor # Called on initialization
// Good place for one-time setup
render # Called on setState()
// Only return jsx
componentDidMount # Called after mounting component (after first render)
// Initial data loading
componentDidUpdate # Called after every render update
// Load updated data
componentWillUnmount # Called before unmount component
// Cleanup

Others (unused): shouldComponentUpdate, getDerivedStateFromProps, getSnapshotBeforeUpdate

# React refs

Give access to a singles DOM element
Created in the contructor()

# Redux

State management library
Action Creator -> Action -> dispatch -> Reducers -> State

# Redux-thunk

Action creator must return PLAIN JS! async await doesn't return plain JS
By the time the action gets to reducer, the data wouldn't be yet fetched
Redux-thunk assists with the asynchronous action creator
// Thunk middleware get called with every action we dispatch
// Thunk allows objects OR functions to be returned from action creators
// For action object: must have a type
// For function object: type optional

# Rules of reducers

-> Must return a value (cannot be undefined)
-> Fed with the previous state, and the action
-> Must not reach out of itself to return data (api, innerhtml, hd ...)
-> Must not change the input state

# Packages

react # Create components
react-dom # Render components
faker # Generate fake data (images, addresses, finances...)
axios # API request
SemanticUI # CSS Framework
redux # State manager
react-redux # Integrate redux to react
redux-thunk # Middleware to make requests with redux
lodash # Strings and functions manipulation
react-router-dom # Page navigation
google-apis # Google services
redux-form # Simplifies the read and write from/to redux store
json-server # Simple REST server
