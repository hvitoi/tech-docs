// Modules
import { combineReducers } from 'redux'
import { reducer as formReducer } from 'redux-form'

// Reducers
import authReducer from './authReducer'
import streamReducer from './streamReducer'


export default combineReducers({
    auth: authReducer,
    form: formReducer,       // 'form' reducer must be added in order to make redux-form work
    stream: streamReducer
})