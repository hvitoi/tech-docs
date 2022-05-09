import React from 'react'
import { connect } from 'react-redux'
import _ from 'lodash'

// Actions
import { fetchStream, editStream } from '../../actions'

// Components
import StreamForm from './StreamForm'

class StreamEdit extends React.Component {

    componentDidMount() {
        this.props.fetchStream(this.props.match.params.id)
    }

    onSubmit = (formValues) => {
        this.props.editStream(this.props.match.params.id, formValues)
    }
 
    render() {  
        return (
            <div>
                <h3>Edit a Stream</h3>
                <StreamForm 
                    initialValues={_.pick(this.props.stream, 'title', 'description')}
                    onSubmit={this.onSubmit}>
                </StreamForm> {/* InitialValues is a specially property in redux-form to*/} {/* the  parameters inside of initial values must match with the name of the elements inside of the form*/}
            </div>
        )
    }
}


const mapStateToProps = (state, ownProps) => {
    return { 
        stream: state.stream[ownProps.match.params.id]
    }
}
export default connect(mapStateToProps, { fetchStream, editStream })(StreamEdit)