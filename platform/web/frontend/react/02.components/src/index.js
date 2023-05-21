import React from 'react'
import ReactDOM from 'react-dom'
import faker from 'faker'
import CommentDetail from './CommentDetail'
import ApprovalCard from './ApprovalCard'

const App = () => {
    return (
        <div className="ui container comments">

            <ApprovalCard>
                <div>
                    <h4>Warning!</h4>
                    Are you sure?
                </div>
            </ApprovalCard>

            <ApprovalCard>
                <CommentDetail 
                    author="Sam"
                    timeAgo="Today at 4:45am"
                    content="Nice blog!"
                    image={faker.image.avatar()}
                />  {/* Import a component by its name */ /* CommentDetail here is a child component */}
            </ApprovalCard>

            <ApprovalCard>
                <CommentDetail
                    author="Alex"
                    timeAgo="Yesterday at 2:45am"
                    content="Awesome!"
                    image={faker.image.avatar()}
                />  {/* Passing props to the child */}
            </ApprovalCard>

            <ApprovalCard>
                <CommentDetail
                    author="Jane"
                    timeAgo="Yesterday at 1:25am"
                    content="Sucks."
                    image={faker.image.avatar()}
                />
            </ApprovalCard>
            
        </div>
    )
}

ReactDOM.render(
    <App />,
    document.querySelector('#root')
)