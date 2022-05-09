import React from 'react'
import { connect } from 'react-redux'

// Actions
import selectSong from '../actions'

class SongList extends React.Component {

    renderList() {
        return this.props.songs.map((song) => {     // Map the array of songs and return JSX
            return (    // The song doesn't have an id to be passed as key, therefore the title is used as a key
                <div className="item" key={ song.title }>

                    <div className="right floated content"> { /* Button div */}
                        <button 
                            className="ui button primary"
                            onClick={() => this.props.selectSong(song)} 
                        >   { /* The action call here goes automatically to dispatch */}
                            Select
                        </button>
                    </div>

                    <div className="content">   { /* Label div */}
                        {song.title}
                    </div>

                </div>
            )
        })
    }

    render() {
        return <div className="ui divided list">{this.renderList()}</div>
    }
}








// Export the data from the store into props
// This function is passed as a callback function and it populates the props
// Return only the properties from the store that matters to this component
const mapStateToProps = (state) => { 
    return { 
        songs: state.songs
    }  
}

// Return a function with paramater (SongList) that inside of the connect() function
// Now instead of the SongList component, a Connect component is passed
// The mapStateToProps will choose the properties that matter to this current component
// The SongList will populate its props with the relevant properties from the store + the dispatch function

export default connect(
    mapStateToProps,
    { selectSong }
)(SongList)  