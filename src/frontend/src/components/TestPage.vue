<template>
    <el-main>
        <div style="background-color: beige;">
            <p>这里是test页面，这里仅展示vue的组件如何插入到页面中。</p>
        </div>
        <el-image :src="imgurl" :fit="cover" :width="200" :height="200"></el-image>
        <el-row>
            <el-col :span="12">
                <el-button type="primary" @click="upload">上传图片</el-button>
            </el-col>
            <el-col :span="12">
                <el-button type="primary" @click="change">改变图片</el-button>
            </el-col>
        </el-row>
    </el-main>
</template>

<script>

export default {
    name: 'TestPage',
    data() {
        return {
        //可以对指定属性或data数组进行数据传递在页面中显示
            imgurl: require("@/assets/p2.png"),
        };
    },
    mounted() {
        //在这发起后端请求，拿回数据，配合路由钩子做一些事情,也可以在打开当前页面执行methods里面的方法，例如：
        this.test();
    },
    methods: {
        //这里是写各种不同的方法函数，这些方法可以理解为是一个属性，因为调用这个方法的时候，最终返回的是一个值
        test() {
            this.$message({"message": "你好，我是AI-Chat-Bot，很高兴为您服务！", "type": "success"});
        },
        change() {
            if (this.imgurl === require("@/assets/p1.png")) {
                this.imgurl = require("@/assets/p2.png");
            } else {
                this.imgurl = require("@/assets/p1.png");
            }
        },
      upload() {
        // 创建一个 input 元素，用于触发文件选择对话框
        const input = document.createElement('input');
        input.type = 'file';
        input.accept = 'image/*'; // 只接受图片类型的文件

        // 监听文件选择事件
        input.addEventListener('change', event => {
          const file = event.target.files[0];
          if (file) {
            // 使用 FileReader 读取文件内容并获取图片路径
            const reader = new FileReader();
            reader.onload = () => {
              this.imgurl = reader.result; // 设置 imgurl 为选择的图片路径
            };
            reader.readAsDataURL(file);
          }
        });

        // 触发文件选择对话框
        input.click();
      },
    },
};
</script>

<style lang="scss" scoped>

</style>
