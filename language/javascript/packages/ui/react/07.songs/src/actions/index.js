// Action creator
const selectSong = (song) => { // Named export
    return {    // Action
        type: 'SELECT_SONG',
        payload: song
    }
}

export default selectSong