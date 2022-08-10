const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
      proxy: 'https://localhost:8000'
  } 
}
