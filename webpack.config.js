const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
// const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  // the base directory for resolveing the entry option
  // context: __dirname
  // The entry point that will have all the js, don't need extension because of resolve
  entry: './index',
  output: {
    // where we want the bundle to go
    path: path.resolve('./assets/bundles/'),
    // convention for webpack
    filename: '[name]-[hash].js',
    // below solved the publicPath issue with autoMain
    publicPath: ''
  },
  plugins: [
    // new CleanWebpackPlugin(),
    // stores data about bundles here
    new BundleTracker({
      filename: './webpack-stats.json'
    })
  ],
  module: {
    rules: [
      {
        // tells webpack to use the below loaders on all jsx and jsx files
        test: [/\.jsx?$/, /\.js?$/],
        // avoid node modules cause this will take forever
        exclude: /node_modules/,
        loader: 'babel-loader',
      }
    ]
  },
  resolve: {
    // extensions to resolve modules
    extensions: ['.js', '.jsx']
  }
}
