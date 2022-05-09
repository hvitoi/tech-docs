// This file is automatically loaded whenever nextjs starts up

module.exports = {
  webpackDevMiddleware: (config) => {
    config.watchOptions.poll = 300; // watch for the files automatically once every 300 ms
    return config;
  }
};
