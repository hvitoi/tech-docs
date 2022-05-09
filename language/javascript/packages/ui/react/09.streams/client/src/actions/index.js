// APIs
import streams from '../apis/streams'

// Types of Action Creators
import actionTypes from './types'

// Navigation history
import history from '../history'

const signIn = (userId) => {
    return {
        type: actionTypes.SIGN_IN,
        payload: userId
    }
}

const signOut = () => {
    return {
        type: actionTypes.SIGN_OUT
    }
}

const fetchStreams = () => async (dispatch) => {
    const res = await streams.get('/streams')
    dispatch({ type: actionTypes.FETCH_STREAMS, payload: res.data })
 }

 const fetchStream = (id) => async (dispatch) => {
    const res = await streams.get('/streams/' + id)
    dispatch({ type: actionTypes.FETCH_STREAM, payload: res.data })
 }

const createStream = (formValues) => async (dispatch,getState) => {
    const { userId } = getState().auth // Take the userid from the store
    const res = await streams.post('/streams', {...formValues, userId }) // Add userId to the formValues
    dispatch({ type: actionTypes.CREATE_STREAM, payload: res.data })

    // Do programmatic navigation (Autommatically redirect user)
    history.push('/')
 }

 const editStream = (id, formValues) => async (dispatch) => {
    const res = await streams.patch('/streams/' + id, formValues)
    dispatch({ type: actionTypes.EDIT_STREAM, payload: res.data })
    history.push('/')
 }

 const deleteStream = (id) => async (dispatch) => {
    await streams.delete('/streams/' + id)  // There is no response for delete
    dispatch({ type: actionTypes.DELETE_STREAM, payload: id })
    history.push('/')
 }


export {
    signIn,
    signOut,
    createStream,
    fetchStreams,
    fetchStream,
    editStream,
    deleteStream
}