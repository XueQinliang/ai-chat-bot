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
            this.$message({"message": "上传图片功能暂未开放，敬请期待！", "type": "warning"});
        },
    },
};
</script>

<style lang="scss" scoped>

</style>
