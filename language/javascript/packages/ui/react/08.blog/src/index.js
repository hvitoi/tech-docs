// Modules
import React from 'react'
import ReactDOM from 'react-dom'
import { createStore, applyMiddleware } from 'redux'
import { Provider } from 'react-redux'
import thunk from 'redux-thunk'

// Components
import App from './components/App'

// Reducers
import reducers from './reducers'

// -------------------------
// Create the store with the reducers applying the middleware thunk
const store = createStore(reducers, applyMiddleware(thunk))


ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.querySelector('#root')
)