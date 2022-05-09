// Modules
import _ from 'lodash'

// Types of actions
import actionTypes from '../actions/types'


const streamReducer = (state = {}, action) => {
    switch(action.type) {
        case actionTypes.FETCH_STREAMS:
            return { ...state, ..._.mapKeys(action.payload, 'id')} // mapkeys take an array and make an object in property 'id'
        case actionTypes.FETCH_STREAM:
            return {...state, [action.payload.id]: action.payload}
        case actionTypes.CREATE_STREAM:
            return {...state, [action.payload.id]: action.payload}
        case actionTypes.EDIT_STREAM:
            return {...state, [action.payload.id]: action.payload}
        case actionTypes.DELETE_STREAM:
            return _.omit(state, action.payload)    // Creates a new object without the last parameter property
        default:
            return state
    }
}

export default streamReducer