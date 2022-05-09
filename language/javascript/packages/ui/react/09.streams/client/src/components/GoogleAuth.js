import React from 'react'
import { connect } from 'react-redux'
import { signIn, signOut } from '../actions'

class GoogleAuth extends React.Component {

    componentDidMount () {
        // gapi is available at window scope
        window.gapi.load('client:auth2', () => {    // Callback to be called after the lib is downloaded
            window.gapi.client.init({   // Initialize authentication client
                clientId: '254975281408-an2h5d7sitm7r2agd7te8gtj9nh3c2sr.apps.googleusercontent.com',
                scope: 'email'   // What different parts of the user we wanna get access
            }).then(() => {     // If successfully initialized
                this.auth = window.gapi.auth2.getAuthInstance()     // Reference to the auth instance
                this.onAuthChange(this.auth.isSignedIn.get())    // Change the initial state
                this.auth.isSignedIn.listen(this.onAuthChange)  // When isSignedIn is changed, call onAuthChange
            })
        })
    }

    onAuthChange = (isSignedIn) => {
        if (isSignedIn) {
            this.props.signIn(this.auth.currentUser.get().getId())
        } else {
            this.props.signOut()
        }
    }

    onSignInClick = () => {
        this.auth.signIn()
    }

    onSignOutClick = () => {
        this.auth.signOut()
    }

    renderAuthButton() {
        if (this.props.isSignedIn === null) {
            return null
        } else if (this.props.isSignedIn) {
            return (
                <button onClick={this.onSignOutClick} className="ui red google button">
                    <i className="google icon" />
                    Sign out
                </button>
            )
        } else {
            return (
                <button onClick={this.onSignInClick} className="ui red google button">
                    <i className="google icon" />
                    Sign in with Google
                </button>
            )
        }
    }

    render () {
        return (
            <div>
                {this.renderAuthButton()}
            </div>
        )
    }
}


const mapStateToProps = (state) => {
    return { isSignedIn: state.auth.isSignedIn }
}

export default connect(mapStateToProps, { signIn, signOut })(GoogleAuth)