// Filename : backendmain.py
// Author by : Qinliang Xue
// Date : 2022-11-14
// 修改这个文件之后，需要重启前端服务

const { defineConfig } = require('@vue/cli-service')
module.exports = {
  devServer: {
    host: '127.0.0.1',
    port: 8080,
    open: true,
    proxy: {
        '/api': { // 代理api，向后端发送的请求均需要以/api开头
            target: 'http://127.0.0.1:504/', //接口域名
            changeOrigin: true,             //是否跨域
            ws: true,                       //是否代理 websockets
            secure: true,                   //是否https接口
            pathRewrite: {                  //路径重置
                '^/api': '',
                '/api': ''
            }
        }
    },
  },
}
