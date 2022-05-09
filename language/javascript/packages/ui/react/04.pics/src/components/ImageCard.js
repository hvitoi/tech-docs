import React from 'react'

class ImageCard extends React.Component {

    constructor(props) {
        super(props)

        // Initialize the state object
        this.state = { spans: 0 }

        // imageRef refers to the html tag itself! <img>
        this.imageRef = React.createRef()
    }

    componentDidMount() {   // If the imageRef (height) was called in componentDidMount() it would be 0 because the image would then not be loaded yet
        // A event listener can be created using the <img> element referenced
        this.imageRef.current.addEventListener('load', this.setSpans)
    }


    setSpans = () => {
        const height = this.imageRef.current.clientHeight
        const spans = Math.ceil(height / 10)    // With 10px row height, the image will take up more rows
        this.setState({ spans })
    }

    render() {
        return (
            <div style={{gridRowEnd: `span ${this.state.spans}`}}> {/* Inline style so that the image has the corrent number of rows */}
                <img 
                    ref={this.imageRef}
                    alt={this.props.image.description}
                    src={this.props.image.urls.regular}
                />
            </div>
        )
    }
}

export default ImageCard