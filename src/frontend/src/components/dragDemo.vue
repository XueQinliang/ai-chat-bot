<template>
  <div class="move">
    <h2 @click="add">+</h2>

    <div class="all">
      <div class="item" v-for="(item, index) in list" :key="item.name"
        :style="{ left: item.sleft + 'px', top: item.stop + 'px' }" @mousedown.stop="move(index, $event)">
        <img :src="item.url" alt="" style="width: 100%; height: 100%" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      sonLeft: 0,
      sonTop: 0,
      list: [
        {
          name: "1",
          sleft: 20,
          stop: 30,
          url:
            require("@/assets/p1.png"),
        },
        {
          name: "2",
          sleft: 200,
          stop: 300,
          url:
            require("@/assets/p2.png"),
        },
        {
          name: "3",
          sleft: 400,
          stop: 600,
          url:
            require("@/assets/logo.png"),
        },
      ],
    };
  },
  methods: {
    // 元素拖动事件
    move(index, e) {
      let element = e.currentTarget;
      console.log(e.currentTarget);
      //   阻止默认的图片拖拽事件
      e.preventDefault();

      //算出鼠标相对元素的位置
      let disX = e.clientX - element.offsetLeft * 0.6;
      let disY = e.clientY - element.offsetTop * 0.6;

      document.onmousemove = (e) => {
        //用鼠标的位置减去鼠标相对元素的位置，得到元素的位置
        let left = e.clientX - disX;
        let top = e.clientY - disY;
        //移动当前元素
        this.list[index]["sleft"] = left / 0.6;
        this.list[index]["stop"] = top / 0.6;

      };
      document.onmouseup = (e) => {
        console.log(e);
        //鼠标弹起来的时候不再移动
        document.onmousemove = null;
        //预防鼠标弹起来后还会循环（即预防鼠标放上去的时候还会移动）
        document.onmouseup = null;
      };
    },

    add() {
      console.log("添加元素");
      this.list.push({
        name: "4",
        url:
          require("@/assets/logo.png"),
      });
    },


  },
};
</script>

<style scoped>
.all {
  position: relative;
  width: 1000px;
  height: 1000px;
  background-color: rgba(232, 199, 204, 0.841);
  transform: scale(0.6, 0.6);
  transform-origin: 0% 0%;
}

.item {
  position: absolute;
  left: 0px;
  top: 0px;
  width: 50px;
  height: 50px;
  background-color: rgba(0, 119, 255, 0.788);
}
</style>
