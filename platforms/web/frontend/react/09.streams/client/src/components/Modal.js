import React from 'react'
import ReactDOM from 'react-dom'


const Modal = (props) => {
    return ReactDOM.createPortal(
        <div onClick={props.onDismiss} className="ui dimmer modals visible active"> {/* OnClick event when the user clicks outside of the modal */}
            <div onClick={(e) => e.stopPropagation() } className="ui stand modal visible active"> {/* onClick prevents the onclick actions of the other elements to take place */}
                <div className="header">{props.title}</div>
                <div className="content">{props.content}</div>
                <div className="actions">
                    {props.actions}
                </div>
            </div>
        </div>,
        document.querySelector('#modal')    // Creates a child into the #modal element
    )
}
export default Modal