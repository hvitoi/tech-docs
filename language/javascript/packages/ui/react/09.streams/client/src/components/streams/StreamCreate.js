// Modules
import React from 'react'
import { connect } from 'react-redux'

// Actions
import { createStream } from '../../actions'

// Components
import StreamForm from './StreamForm'

class StreamCreate extends React.Component {

    onSubmit = (formValues) => {  // onSubmit doesn't receive e anymore, instead it receives the values from the form
        //e.preventDefault()        // preventDefault don't need to be called with redux-form
        this.props.createStream(formValues) // OnSubmit is called after validation
    }

    render() {

        return (
            <div>
               <h3>Create a Stream</h3>
               <StreamForm onSubmit={this.onSubmit} />
            </div>
        )

    }
}


 export default connect(null, { createStream  })(StreamCreate)