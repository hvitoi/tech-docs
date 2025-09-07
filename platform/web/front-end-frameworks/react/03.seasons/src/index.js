// Modules
import React from 'react'
import ReactDOM from 'react-dom'

// Components
import SeasonDisplay from './SeasonDisplay'
import Spinner from './Spinner'


class App extends React.Component {

    // // In JS class, the constructor function is the first function to be called when an instance is created
    // constructor(props) {
    //     // Calls the constructor function of the parent (React.Component)
    //     super(props)    

    //     // constructor() initializes the state object
    //     this.state = { lat: null, errorMessage: '' }       
    // } 

    // State object initialization
    state = { lat: null, errorMessage: '' }     // Babel converts it to the exact same constructor function above

    componentDidMount() {
        // Start to get the user current location at the initialization
        window.navigator.geolocation.getCurrentPosition(
            (position) => { // Success callback
                this.setState({ lat: position.coords.latitude })    // Updates the state object               
            },
            (err) => { // Error callback
                this.setState({ errorMessage: err.message })
            }
        ) 
    }

    componentDidUpdate() {
        console.log('My component was updated')
    }

    componentWillUnmount() {
        console.log('My component will unmount')
    }

    renderContent() {
        if (this.state.errorMessage && !this.state.lat) {
            return <div>Error: {this.state.errorMessage}</div>
        }

        if (!this.state.errorMessage && this.state.lat) {
            return <SeasonDisplay lat={this.state.lat} />
        }

        return <Spinner message="Please accept location request" />
    }

    render() { // Render method must be defined!
        return (
            <div className="border red">
                {this.renderContent()}
            </div>    
        )
    }

}

ReactDOM.render(
    <App />,
    document.querySelector('#root')
)