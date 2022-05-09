import Redux from 'redux'

// Action creators (Function that returns the object)
const createPolicy = (name, amount) => { 
    return {  // Action (Object)
        type: 'CREATE_POLICY',   // By convention the type is in upper case
        payload: {
            name: name,
            amount: amount
        }
    }
}
const deletePolicy = (name) => {
    return {
        type: 'DELETE_POLICY',
        payload: {
            name: name
        }
    }
}
const createClaim = (name, amountMoney) => {
    return {
        type: 'CREATE_CLAIM',
        payload: {
            name: name,
            amountMoney: amountMoney
        }
    }
}


// Reducers
const claimsHistory = (claimsList = [], action) => {   // oldList is set to an empty array in case undefined is received
    if (action.type === 'CREATE_CLAIM') {
        return [...claimsList, action.payload]  // Create new list with the old list and add the new element
    }
    return claimsList
}
const accounting = (bagOfMoney = 100, action) => {
    if (action.type === 'CREATE_CLAIM') {
        return bagOfMoney - action.payload.amountMoney
    } else if (action.type === 'CREATE_POLICY') {
        return bagOfMoney + action.payload.amount
    } 
    return bagOfMoney
}
const policies = (policiesList = [], action) => {
    if (action.type === 'CREATE_POLICY') {
        return [...policiesList, action.payload.name]
    } else if (action.type === 'DELETE_POLICY') {
        return policiesList.filter((name) => name !== action.payload.name)
    }
    return policiesList
}

// Extract functions from Redux library
const { createStore, combineReducers } = Redux

// combineReducers and createStore
const ourDepartments = combineReducers({
    accounting: accounting,
    claimsHistory: claimsHistory,
    policies: policies
})
const store = createStore(ourDepartments)


// Create an action
const action1 = createPolicy('Alex', 50)
const action2 = createPolicy('Maria', 60)
const action3 = createClaim('Julia', 20)
const action4 = deletePolicy('Alex')

// Dispatch
store.dispatch(action1)
store.dispatch(action2)
store.dispatch(action3)
store.dispatch(action4)

// State
store.getState()
console.log(store.getState());
