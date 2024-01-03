// Filename : backendmain.py
// Author by : Qinliang Xue
// Date : 2022-11-14
// 修改这个文件之后，需要重启前端服务

import { createApp } from 'vue'
import App from './App.vue'
import Axios from 'axios';//引入axios
// 导入element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
 
const app = createApp(App)

// 全局变量，挂载axios，好像还不如每个页面引入一遍好用
app.provide('global',{
    Axios
})  
app.use(ElementPlus)
app.mount('#app')
