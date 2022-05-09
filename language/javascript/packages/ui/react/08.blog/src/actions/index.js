// Modules
import _ from 'lodash'

// APIs
import jsonPlaceholder from '../apis/jsonPlaceholder'

// Actions  
const fetchPosts = () => async (dispatch) => {  // Redux-thunk allows function actions to be returned! 
    const res = await jsonPlaceholder.get('/posts') // Fetch data from API
    dispatch({ type: 'FETCH_POSTS', payload: res.data }) // Dispatch the response manually
}  

const fetchUser = (id) => async (dispatch) => {  
    const res = await jsonPlaceholder.get('/users/' + id)
    dispatch({ type: 'FETCH_USER', payload: res.data })
} 

const fetchPostsAndUsers = () => async (dispatch, getState) => {

    // Dispatch has to be done manually if an action created is evoked from inside another action
    await dispatch(fetchPosts())
    
    // // Lodash map
    // const userIds = _.uniq(_.map(getState().posts, 'userId'))   
    // // Iterate each userId to a fetchUser dispatch
    // userIds.forEach((id) => dispatch(fetchUser(id)))      // Doesn't have await because it's not necessary, the data can appear afterwards

    // Allows chaining a bunch of functions
    _.chain(getState().posts)
        .map('userId')                              // Fetch only 'userId' property 
        .uniq()                                     // Extract unique values only
        .forEach((id) => dispatch(fetchUser(id)))   // Loop each userId and dispatch
        .value()                                    // Execute
}


export { fetchPosts, fetchUser, fetchPostsAndUsers }

// export const fetchPosts = () => {
//     return async (dispatch, getState) => {     // dispatch modifies the store, getState shows the store     
//         // Fetch data from API
//         const res = await jsonPlaceholder.get('/posts')
//         // Dispatch the response from API
//         dispatch({ type: 'FETCH_POSTS', payload: res })
//     }  
// }

//import _ from 'lodash'
// const fetchUser = (id) => (dispatch) => _fetchUser(id, dispatch)
// const _fetchUser = _.memoize(async (id, dispatch) => {
//     const res = await jsonPlaceholder.get('/users/' + id)
//     dispatch({
//         type: 'FETCH_USER',
//         payload: res.data
//     })
// })