// https://jestjs.io/docs/en/configuration.html

module.exports = {
  // Automatically clear mock calls and instances between every test
  clearMocks: true,

  // The directory where Jest should output its coverage files
  coverageDirectory: "coverage",

  // An array of file extensions your modules use
  moduleFileExtensions: [
    'js',
    'ts',
    'json'
  ],

  // The glob patterns Jest uses to detect test files
  testMatch: [
    '**/?(*.)+(test).ts'
  ],

  // A map from regular expressions to paths to transformers
  transform: {
    '^.+\\.(ts)$': 'ts-jest'
  }
};
