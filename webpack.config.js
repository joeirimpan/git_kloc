var path = require('path');
var webpack = require('webpack');

module.exports = {
  entry: './git_kloc/static/js/react/main.js',
  output: { path: __dirname + '/git_kloc/static/js/', filename: 'main.js' },
  module: {
    loaders: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['babel-preset-es2015', 'babel-preset-react'].map(require.resolve)
        }
      }
    ]
  },
};
