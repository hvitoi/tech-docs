import React from 'react'
import { Link } from 'react-router-dom'

// Components
import GoogleAuth from './GoogleAuth'

const Header = () => {
    return (
        <div className="ui secondary poiting menu">
            <Link to="/" className="item">Streamer</Link>
            <div className="right menu">
                <Link to="/" className="item">All Streams</Link>
                <GoogleAuth />
            </div>
        </div>
    )
}

export default Header