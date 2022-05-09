import React from 'react'

const Spinner = (props) => {
    return (
        <div className="ui active dimmer">
            <div className="ui big text loader">{props.message}</div>
        </div>
    )
}

// Setup default props in case it's not provided
Spinner.defaultProps = {       
    message: 'Loading...'
}

export default Spinner