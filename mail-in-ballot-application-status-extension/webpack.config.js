const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const ZipPlugin = require("zip-webpack-plugin");

const BUILD_PATH = path.resolve(__dirname, "dist");
const NAME = "status-checker";

module.exports = [
  {
    entry: {
      background: "./src/background.ts",
      content: "./src/content.ts",
    },
    module: {
      rules: [
        {
          test: /\.ts$/,
          loader: "ts-loader",
          options: { onlyCompileBundledFiles: true },
          exclude: /node_modules/,
        },
      ],
    },
    resolve: {
      extensions: [".ts", ".js"],
    },
    output: {
      filename: "[name].js",
      sourceMapFilename: "[name].js.map",
      path: BUILD_PATH,
    },
    devtool: "source-map",
    mode: "none",
    plugins: [
      new CleanWebpackPlugin(),
      new CopyPlugin({
        patterns: [
          {
            // Copy webextension-pollyfill and its source map to
            // ./${BUILD_PATH}. See docs for details on this setup:
            // https://github.com/mozilla/webextension-polyfill/tree/faa22a4df1bc0bbaf2a6c093352d8df8b33b9b92#usage-with-webpack-without-bundling.
            // The webextension-pollyfill provides the global namespace
            // `browser`, which allows the extension to run in Chrome and
            // Brave.
            from:
              "node_modules/webextension-polyfill/dist/browser-polyfill.js*",
            flatten: true,
          },
          {
            from: "./src/manifest.json",
          },
        ],
      }),
      new ZipPlugin({
        filename: `${NAME}`,
        extension: "xpi",
      }),
    ],
    node: {
      fs: "empty",
    },
  },
];
