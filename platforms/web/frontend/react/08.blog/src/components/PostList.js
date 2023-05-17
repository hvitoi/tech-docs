import React from 'react'
import { connect } from 'react-redux'

// Actions
import { fetchPostsAndUsers } from '../actions'

// Components
import UserHeader from './UserHeader'

class PostList extends React.Component {

    componentDidMount() {
        // Call the action to request the API after the component is mounted
        this.props.fetchPostsAndUsers() 
    }

    renderList() {
        const jsxPosts = this.props.posts.map((post) => {
            return (
                <div className="item" key={post.id} >
                    <i className="large middle aligned icon user" />
                    <div className="content">
                        <div className="description">
                            <h2>{post.title}</h2>
                            <p>{post.body}</p>
                        </div>
                        <UserHeader userId={post.userId} />
                    </div>
                </div>
            )
        })
        return jsxPosts // This is an array with divs... ['<div>...</div>,<div>...</div>,...]   
    }

    render() {
        return <div className="ui relaxed divided list">{this.renderList()}</div>
    }

}




const mapStateToProps = (state) => {
    return { posts: state.posts}
}

export default connect(
    mapStateToProps,    // Passes the variables of props
    { fetchPostsAndUsers }  // Passes the functions of props
)(PostList)