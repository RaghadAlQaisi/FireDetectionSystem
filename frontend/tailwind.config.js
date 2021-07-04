/*
 ** TailwindCSS Configuration File
 **
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */
module.exports = {
  theme: {
    container: {
      center: true,
      padding: {
        default: '2rem',
      }
    },
    extend: {
      colors: {
        'black': {
          default: '#2e3436',
        },
        'grey': {
          default: '#35495e',
          'light': '#fcfcfc'
        },
        'green': {
          default: '#3b8070',
          'shine': '#47d337'
        },
      },
      fontFamily: {
        'IBMPlexSans': 'IBM Plex Sans',
        'IBMPlexMono': 'IBM Plex Mono',
      }
    }
  }
}
