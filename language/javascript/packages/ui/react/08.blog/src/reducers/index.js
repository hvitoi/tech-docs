import { combineReducers } from 'redux'

// Reducers
import postsReducer from './postsReducer'
import usersReducer from './usersReducer'

export default combineReducers({
    posts: postsReducer,
    users: usersReducer
})