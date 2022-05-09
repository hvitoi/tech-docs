// Import React and ReactDOM libs
import React from 'react'
import ReactDOM from 'react-dom'

// A react component is a function or a class.
// The component produces the HTML using JSX and handle feedback from the user

// Create component as a function
const App = () => {
    const buttonText = 'Click me!'

    // jsx calls a function React.createElement() behinds the scenes
    return (        // This is JSX          // Convention: Double quotes for JSX elements and single quotes for JS elements         // "class" elements might be needed to be converted to "className"      // "for" element must be replaced to "htmlFor"
        <div>   
            <label className="label" htmlFor="name">        {/* "for" associates the label with the input*/}
                Enter name:
            </label>

            <input id="name" type="text" />

            <button style={{ backgroundColor: 'blue', color:'white' }}>         {/* JSX inline style. The style provided is an js object. Dashes are removed with the next letter capitalized */}
                {buttonText}   {/* Only data can be printed out. Objects must be stringfied*/}
            </button>

            {/* <button style="background-color: blue; color:white;">Submit</button> //This is native HTML inline style*/}
        </div>
    )
}

// Take component and render in the .html
ReactDOM.render(                    // render(jsx,target)
    <App />,                        // JSX tag (It's is converted to a react component by Babel)
    document.querySelector('#root') // Target
)