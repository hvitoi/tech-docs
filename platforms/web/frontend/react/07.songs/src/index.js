// Modules
import React from 'react'
import ReactDOM from 'react-dom'
import { Provider } from 'react-redux'
import { createStore } from 'redux'

// Components
import App from './components/App'

// Reducers
import reducers from './reducers'


// Wrap the <App /> inside of a <Provider /> and pass a prop with the store of reducers
ReactDOM.render(
    <Provider store={createStore(reducers)}>
        <App />
    </Provider>,
    document.querySelector('#root')
)