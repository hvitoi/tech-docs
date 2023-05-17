import React from 'react'

class SearchBar extends React.Component {

    // constructor() {              // This is a way to solve the this.fn problem
    //     super()
    //     this.drive = this.drive.bind(this)
    // }

    state = { term: '' }

    // onFormSubmit(e) {   // Function declared as conventional onFormSubmit = function () ...
    //     e.preventDefault()
    //     console.log(this.state.term);
    // }

    onFormSubmit = (e) => {   // This arrow function makes sure the 'this' refers to the class that is was called from
        e.preventDefault()
        this.props.onSearch(this.state.term)    // Call the function provided in the props
    }

    render () {
        return (
            <div className="ui segment">
                <form onSubmit={this.onFormSubmit} className="ui form">
                    <div className="field">
                        <label>Image Search</label>
                        <input
                            type="text"
                            value={this.state.term}
                            onChange={ (e) => this.setState({ term: e.target.value })} 
                        /> {/* function is passed as a callback function, so that it's not executed on every rerender */}
                    </div>
                </form>
            </div>
        )
    }
}

export default SearchBar