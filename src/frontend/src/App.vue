<template>
  <el-container class="bigcontainer">
    <el-aside class="aside">
      <div v-for="clickuser in user_list" :key="clickuser" :class="{'left_parent':true}">
        <div :class="{'user':true, 'grey':clickuser==user}" @click="chooseuser(clickuser)">
          <div style="display: flex;">
            <el-avatar
              src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
            />
            <div class="text" style="margin-top: 10px; margin-bottom: 10px;">{{clickuser}}</div>
          </div>
        </div>
      </div>
      <TestPage />
    </el-aside>
    <el-main style="margin:0px; padding: 0px;">
      <el-header class="header">{{user}}</el-header>
      <div class="container">
        <div v-for="item in list" :key="item.id" :class="{'left_parent':item.role=='system', 'right_parent':item.role=='user'}">
          <div :class="{'text_dialog':true, 'white':item.role=='system', 'green':item.role=='user'}"
               v-loading="loading && item.id==list.length-1 && item.role=='system'">
            <p class="text" style="white-space: pre-wrap;" v-show="item.id<list.length-1 || item.role=='user'">{{item.text}}</p>
            <p class="text" style="white-space: pre-wrap;" v-show="item.id==list.length-1 && item.role=='system'">{{answer}}</p>
          </div>
        </div>
        <el-dialog v-model="centerDialogVisible" title="你是不是想问这些问题？" width="80%" center>
          <div class="msgdialog" v-loading="dialog_loading">
            <div v-for="item in question_list" :key="item" :class="{'left_parent':true}">
              <div :class="{'text_dialog':true, 'green':true}" @click="closedialog(item)">
                <p class="text" style="white-space: pre-wrap; margin-top: 0px; margin-bottom: 0px;">{{item}}</p>
              </div>
            </div>
          </div>
          <template #footer>
            <span class="dialog-footer">
              <el-button @click="centerDialogVisible = false">不了，谢谢</el-button>
              <el-button type="primary" @click="showdialog()">
                换一批问题
              </el-button>
            </span>
          </template>
        </el-dialog>
      </div>
      <el-button @click="send()" class="button" :disabled="disable">发送提问</el-button>
      <el-button @click="showdialog()" class="button">猜你想问</el-button>
      <div style="margin: 10px;">
        <el-input
          type="textarea"
          :rows="5"
          placeholder="请提问"
          v-model="question">
        </el-input>
      </div>
    </el-main>
  </el-container>
</template>
 
<style scoped>
.bigcontainer {
  padding: 5px; /* 添加内边距 */
  margin: 5px;
}
.aside {
  width: 30%;
  overflow-y: scroll; /* 显示垂直滚动条 */
  border: 1px solid #e4e4e4; /* 添加边框 */
  background-color: #fbfbfb; /* 添加底色 */
  padding: 10px; /* 添加内边距 */
  margin: 10px;
}
.header {
  height: 50px;
  margin:10px; 
  padding: 10px;
  margin-bottom: 0px; 
  background-color: rgb(163, 163, 163);
}
.user {
  display: inline-block;
  background-color: #c9c8c8;
  border: 1px solid #ddd;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 10px;
  margin: 2px;
  width: 85%;
}
.container {
  height: 430px; /* 设置容器高度 */
  overflow-y: scroll; /* 显示垂直滚动条 */
  border: 1px solid #e4e4e4; /* 添加边框 */
  background-color: #fbfbfb; /* 添加底色 */
  padding: 10px; /* 添加内边距 */
  margin: 10px;
  margin-top: 0px;
}
.msgdialog {
  height: 200px; /* 设置容器高度 */
  overflow-y: scroll; /* 显示垂直滚动条 */
}
.left_parent{
	text-align: left;
	margin: 0px auto 0px auto;
}
.right_parent{
	text-align: right;
	margin: 0px auto 0px auto;
}
.text_dialog {
  display: inline-block;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 10px;
  margin: 10px;
  max-width: 400px;
}
.white {
  background-color:rgb(243, 239, 233);
}
.green {
  background-color:greenyellow;
}
.grey {
  background-color:rgb(163, 163, 163);
}
.text {
  text-align: left;
  max-width: 400px;
  margin: 5px;
  word-wrap: break-word; /* 设置自动换行 */
}
.button {
  margin-left:10px; 
  margin-top: 4px;
  background-color: rgba(11, 76, 228, 0.876);
  color: #ddd;
}
</style>

<script setup>
// import {inject} from 'vue'
// const global = inject('global')
import axios from 'axios'
import TestPage from './components/TestPage.vue';
import { ref } from 'vue'
const centerDialogVisible = ref(false);
const loading = ref(false);
const disable = ref(false);
const dialog_loading = ref(false);
const question_list = ref([]);
const user_list = ref(['心理小百科','情感小天使','答题小天才']);
const user = ref('心理小百科');
const question = ref('');
const init_answer = ref('有什么我可以帮你的吗？');
const answer = ref('');
answer.value = '亲，我是你的'+user.value+','+init_answer.value;
const list = ref([{
  'id':0,
  'role':'system',
  'text': answer.value
}]);

function closedialog(item) {
  question.value = item;
  centerDialogVisible.value = false;
}
function chooseuser(clickuser) {
  if (disable.value == false) {
    user.value = clickuser;
    answer.value = '亲，我是你的'+user.value+','+init_answer.value;
    list.value = [{
      'id':0,
      'role':'system',
      'text': answer.value
    }];
  } else {
    alert("亲，请耐心等我说完吧！");
  }
}
function showdialog() {
  centerDialogVisible.value = true;
  dialog_loading.value = true;
  question_list.value = [];
  axios({
      method: "post", //接口方法
      data: {'system': user.value},
      url: "/api/get_more_question", //接口
    }).then((res) => {
      var str = res.data;
      console.log(str);
      try {
        if (typeof(str) == "string") {
          str=str.slice(1,-1)
          var list=str.split(',');
          var newlist = [];
          for(let i = 0; i < list.length; i++) {
            newlist.push(list[i].trim().slice(1, -1));
          }
          question_list.value = newlist;
        } else if (typeof(str) == "object") {
          question_list.value = str;
        } else {
          alert("发生了一些未知错误，请重试");
        }
      } catch (e) {
        alert("发生了一些未知错误，请重试");
      }
      dialog_loading.value = false;
    })
}

function send() {
  if (question.value.length > 0) {
    list.value.push({'id':list.value.length, 'role':'user', 'text':question.value});
    list.value.push({'id':list.value.length, 'role':'system', 'text':''});
    question.value = '';
    answer.value = '努力思考中...';
    loading.value = true;
    disable.value = true;
    axios({
      method: "post", //接口方法
      data: {'question': list.value, 'system': user.value},
      url: "/api/get_reply", //接口
    }).then((res) => {
      list.value.pop();
      list.value.push({'id':list.value.length, 'role':'system', 'text':res.data});
      answer.value = '';
      loading.value = false;
      print(answer, res.data);
    });
  }
}

function print(answer, data) {
  console.log(answer.value.length, data.length);
  if (answer.value.length >= data.length) {
    disable.value = false;
    return;
  } else {
    setTimeout(()=>{
      answer.value += data.charAt(answer.value.length);
      print(answer, data);
    }, 50);
  }
}
</script>
 