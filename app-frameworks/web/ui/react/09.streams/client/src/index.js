import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { createStore, applyMiddleware, compose } from 'redux'
import ReduxThunk from 'redux-thunk'

// Components
import App from './components/App'

// Reducers
import reducers from './reducers'




// Setup Redux-Devtools middleware
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose



// Redux store
const store = createStore(
    reducers,
    composeEnhancers(applyMiddleware(ReduxThunk))
)

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,    
    document.querySelector('#root')
)