// Modules
import React from 'react'
import { Field, reduxForm } from 'redux-form'   // Field is a Component, reduxForm is a function (similar to connect)

class StreamForm extends React.Component {

    renderError({ error, touched }) {
        if (touched && error) {
            return (
                <div className="ui error message">
                    <div className="header">{error}</div>
                </div>
            )
        }
    }

    renderInput = (fieldProps) => {   // Field props has all the information about the field
       const className = `field ${fieldProps.meta.error && fieldProps.meta.touched ? 'error' : ''}` // Trick to show the field in red when there's error
        return (   
            <div className={className}>
                <label>{fieldProps.label}</label>
                <input {...fieldProps.input} autoComplete="off" />
                <div>{this.renderError(fieldProps.meta)}</div>  { /* Print error from the validation step */}
            </div>
        )
    }

    onSubmit = (formValues) => {  // onSubmit doesn't receive e anymore, instead it receives the values from the form
        //e.preventDefault()        // preventDefault don't need to be called with redux-form
        this.props.onSubmit(formValues) // OnSubmit is called after validation
    }

    render() {

        return (
            <div>
                <form onSubmit={this.props.handleSubmit(this.onSubmit)} className="ui form error" >   { /* { Submit with redux-form } */ }
                    <Field name="title" component={this.renderInput} label="Enter title" />
                    <Field name="description" component={this.renderInput} label="Enter description" />
                    <button className="ui button primary">Submit</button>
                </form>
            </div>
        )

    }
}

const validate = (formValues) => {
    const errors = {}

    if (!formValues.title) {    // If there's no title
        errors.title = 'You must enter a title'
    }

    if (!formValues.description) {
        errors.description = 'You must enter a description'
    }
    
    return errors   // Errors are associated with field
}


// reduxForm({options})(component)
export default reduxForm({ 
    form: 'streamForm',
    validate: validate      // validate function is evoked on init or on user interaction
 })(StreamForm)