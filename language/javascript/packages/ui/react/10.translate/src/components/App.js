import React from 'react';
import UserCreate from './UserCreate';
import { LanguageStore } from '../contexts/LanguageContext';
import ColorContext from '../contexts/ColorContext';
import LanguageSelector from './LanguageSelector';

class App extends React.Component {
  render() {
    return (
      <div className="ui container">
        <LanguageStore>
          <LanguageSelector />

          <ColorContext.Provider value="red">
            <UserCreate />
          </ColorContext.Provider>
        </LanguageStore>

        {/*}
          <LanguageContext.Provider value="dutch">        Separate instance of context
              <UserCreate />
          </LanguageContext.Provider>         Pass information to the Language Context. The value here updates whatever value in the context

          <UserCreate />          Gets value from 'default value'
        */}
      </div>
    );
  }
}

export default App;
