// Modules
import React from 'react'

// Components
import { Router, Route, Switch } from 'react-router-dom'
import StreamList from './streams/StreamList'
import StreamShow from './streams/StreamShow'
import StreamCreate from './streams/StreamCreate'
import StreamEdit from './streams/StreamEdit'
import StreamDelete from './streams/StreamDelete'
import Header from './Header'

// History 
import history from '../history'

const App = () => {
    return (
        // <div className="ui container">
        //     <BrowserRouter> {/* BrowserRouter creates a history object to monitor the path accessed */}
        //         <div>
        //             <Header />
        //             <Route path="/" exact={true} component={StreamList} /> {/* exact requires de path to be exact */}
        //             <Route path="/streams/new" exact component={StreamCreate} />
        //             <Route path="/streams/edit" exact component={StreamEdit} />
        //             <Route path="/streams/delete" exact component={StreamDelete} />
        //             <Route path="/streams/show" exact component={StreamShow} />
        //         </div>
        //     </BrowserRouter> {/* BrowserRouter (everything after the TLD), HashRouter (Everything the #), MemoryRouter (Doesn't track navigation) */}
        // </div> 
        <div className="ui container">
            <Router history={history}> {/* Router has to manage the own history */}
                <div>
                    <Header />
                    <Switch>    {/* Switch prevents double routing */}
                        <Route path="/" exact={true} component={StreamList} /> {/* exact requires de path to be exact */}
                        <Route path="/streams/new" exact component={StreamCreate} />
                        <Route path="/streams/edit/:id" exact component={StreamEdit} />
                        <Route path="/streams/delete/:id" exact component={StreamDelete} />
                        <Route path="/stream/:id" exact component={StreamShow} />
                    </Switch>
                </div>
            </Router> {/* BrowserRouter (everything after the TLD), HashRouter (Everything the #), MemoryRouter (Doesn't track navigation) */}
        </div> 
    )
}

export default App