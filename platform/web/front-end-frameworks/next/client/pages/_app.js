// This file must be named exactly _app.js
// This file defines a custom App component

import buildClient from '../api/build-client'; // api to authenticate
import 'bootstrap/dist/css/bootstrap.css'; // Import bootstrap for all components
import Header from '../components/header';

// AppComponent wraps every other component in the project (index.js, banana.js)
// pageProps is each component's props. Component is the component being wrapped
const AppComponent = ({ Component, pageProps, currentUser }) => {
  // We cannot make data loading inside of the component itself!
  return (
    <div>
      <Header currentUser={currentUser} />
      <Component {...pageProps} />
    </div>
  );
};

// getInitialProps is specific to NextJS. It is called before an instance of a component is created
// getInitialProps is superseded, getStaticProps and getServerSideProps are now used instead
// The CONTEXT is the PROPS for generic Componentes.
// context === { req, res }
// The APPCONTEXT is the PROPS for the AppComponent. It has the shape
// appContext === { Component, AppTree, router, ctx: { req, res }}
AppComponent.getInitialProps = async (appContext) => {
  // THIS here inside is the SSR itself
  // We CANNOT use a hook here because this is not a react component

  // buildClient is a AXIOS instance!
  const client = buildClient(appContext.ctx); // ctx is the { req, res }
  const response = await client.get('/api/users/currentuser');

  // Call the getInitialProps (if it exists) of the child component
  let pageProps = {};
  if (appContext.Component.getInitialProps) {
    pageProps = await appContext.Component.getInitialProps(appContext.ctx);
  }

  // This here is passed as props to the components
  return {
    pageProps,
    ...response.data // response.data = { currentUser: ... || null }
  };
};

export default AppComponent;
