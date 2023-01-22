import './SeasonDisplay.css'    // webpack sees the css and stick to index.html   
import React from 'react'

const seasonConfig = {
    summer: {
        text: `Lets hit the beach`,
        iconName: 'sun'
    },
    winter: {
        text: `Burr, it is chilly`,
        iconName: 'snowflake'
    }
}


const getSeason = (lat, month) => {
    if (month >= 4 && month <= 11) {
        return lat > 0 ? 'summer' : 'winter'
    } else {
        return lat > 0 ? 'winter' : 'summer'
    }
}

const SeasonDisplay = (props) => {
    const season = getSeason(props.lat, new Date().getMonth() + 1)
    const { text, iconName } = seasonConfig[season]

    
    return (
        <div className={`season-display ${season}`}>    {/* the outer div has className of the component itself --- convention */}
            <i className={`icon-left massive ${iconName} icon`} />
            <h1>{text}</h1>
            <i className={`icon-right massive ${iconName} icon`} />
        </div>
    )
}

export default SeasonDisplay