import React, { useState } from 'react'

// COmponents
import ResourceList from './ResourceList'
import UserList from './UserList'

const App = () => {

    // Defines a STATE and a SETSTATE with default value 'posts'
    const [resource, setResource] = useState('posts')   // useState returns an array. The first takes the 'posts' value

    // Array destructuring
    // const colors = ['red', 'green']
    // const [myRed, myGreen] = colors

    return (
        <div>
            <h1>Users</h1>
            <UserList />
            <div>
                <button onClick={() => setResource('posts')} >Posts</button>
                <button onClick={() => setResource('todos')} >Todos</button>
            </div>
            <ResourceList resource={resource} />
        </div>
    )
}


export default App