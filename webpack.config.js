webpack = require('webpack');
path = require('path');
var ExtractTextPlugin = require('extract-text-webpack-plugin');


module.exports = {
    context: __dirname,

    entry: {
        bundle: './app/static/app.js',
    },
    output: {
        filename: '[name].js',
        path: './app/static/build',
        library: '[name]'
    },

    resolve: {
      extensions: ['', '.js'],
    },

    devtool: '#cheap-module-source-map',
    module: {
        loaders: [
            { test: /\.(woff|woff2)$/,  loader: "url-loader?limit=10000&mimetype=application/font-woff" },
            { test: /\.ttf$/,    loader: "file-loader" },
            { test: /\.eot$/,    loader: "file-loader" },
            { test: /\.svg$/,    loader: "file-loader" }
        ]
    },
    plugins: [
        new ExtractTextPlugin('styles.css', {
            allChunks: true
        }),
    ]
};