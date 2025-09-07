import React from 'react';
import LanguageContext from '../contexts/LanguageContext';
import ColorContext from '../contexts/ColorContext';

class Button extends React.Component {
  // Reference the context object in class component. Must be exactly 'contextType'
  //static contextType = LanguageContext

  renderSubmit(language) {
    return language === 'english' ? 'Submit' : 'Voorleggen';
  }

  renderButton(color) {
    return (
      <button className={`ui button ${color}`}>
        <LanguageContext.Consumer>
          {({ language }) => this.renderSubmit(language)}
        </LanguageContext.Consumer>
      </button>
    );
  }

  render() {
    // context object is accessible through this.context        
    //const text = this.context === 'english' ? 'Submit' : 'Voorleggen'
    // Multiple consumers
    return (
      <ColorContext.Consumer>
        {color => this.renderButton(color)}
      </ColorContext.Consumer>
    ); 
  } // {/* Get values from context with Consumer component */}
}

export default Button;
