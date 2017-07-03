const path = require('path');
const webpack = require('webpack');


module.exports = {
  context: path.resolve(__dirname, './src'),
  entry: {
    app: './evaluation.js',
  },
  output: {
    path: path.resolve(__dirname, './static'),
    filename: '[name].bundle.js'
  },
  devServer: {
    contentBase: path.resolve(__dirname, './src'),  // New
  }
};
