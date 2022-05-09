import React from 'react'
import unsplash from '../api/unsplash'

// Components
import SearchBar from './SearchBar'
import ImageList from './ImageList'

class App extends React.Component {

    state = { images: [] }

    onSearchSubmit = async (term) => {
        // Request
        const res = await unsplash.get('/search/photos', {
            params: { query: term }
        })

        // Update state
        this.setState({ images: res.data.results })
    }

    render() {
        return (
            <div className="ui container" style={{ marginTop: '10px' }}>
                <SearchBar onSearch={this.onSearchSubmit} />     { /* onSearch is passed as a props. It is an arbitrary name, this event will be declared in the SearchBar component */}
                <ImageList images={this.state.images} />
            </div>
        )
    }

}

export default App