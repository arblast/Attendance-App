var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  entry: './frontend/attendance.jsx',
  output: {
    path: path.resolve('./assets/bundles/'),
    filename: 'bundle.js',
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    })
  ],
  module: {
    loaders: [
      {
        test: [/\.jsx?$/, /\.js?$/],
        exclude: /(node_modules)/,
        loader: 'babel-loader',
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  },
  devtool: 'source-map',
  resolve: {
    extensions: ['.js', '.jsx' ]
  }
};
