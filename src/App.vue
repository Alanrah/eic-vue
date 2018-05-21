<template>
  <div class="wrapper">
    <div class="header">
      <div class = "headerword">{{header}}</div>
    </div>

    <div class="nav">
      <div @click="jump('index')" :class="[selectpath=='index'?'nav-item-selected':'nav-item-normal']">机房信息</div>
      <div @click="jump('add')" :class="[selectpath=='add'?'nav-item-selected':'nav-item-normal']">采集信息</div>
      <div @click="jump('me')" :class="[selectpath=='me'?'nav-item-selected':'nav-item-normal']">我的</div>
    </div>
 <!-- 路由出口 -->
  <!-- 路由匹配到的组件将渲染在这里 -->
    <router-view class="template"></router-view>
  </div>
</template>

<style scoped="scoped">
  html {
    font-family: Microsoft YaHei, Helvetica Neue, Helvetica, Arial, sans-serif;
    overflow: hidden;
  }
  .wrapper{
    width: 750px;
  }
  .header{
    width: 750px;
    height: 68px;
  }
  .headerword{
    height: 60px;
    font-size: 40px;
    border-color: #000000;
    border-style: solid;
    border-width: 1px;
    align-items: center;
    text-align: center;
  }
  .nav{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 750px;
    height: 80px;
    position: fixed;
    bottom: 0px;
    z-index: 98;
    background-color: #B5F0E6;
  }
  .template{
    height: 1100px;
    top: 0px;
    bottom: 80px;
    left: 0px;
    right: 0px;
  }
  .nav-item-selected{
    width: 250px;
    color: #9ACD32;
    text-align: center;
    line-height: 80px;
    height: 80px;
    font-size: 40px;
  }
  .nav-item-normal{
    width: 250px;
    line-height: 80px;
    height: 80px;
    color: #000000;
    text-align: center;
    font-size: 40px;
  }
</style>
<script>
  import Bus from './bus.js'
  export default{
    data:function(){
      return{
        header:"今日机房",
        selectpath:'index'
      }
    },
    methods:{
      jump:function(e){
        switch (e) {
          case 'index':
            this._data.header = "今日机房";
            break;

          case 'add':
            this._data.header = "采集信息";
            break;

          case 'me':
            this._data.header = "我的";
            break;
        }
        this.$router.push(e);
        this._data.selectpath=e;
      }
    },
  mounted(){
    Bus.$on('jumptoindex',(e)=>{
      this._data.header = "今日机房";
      this._data.selectpath=e;
    })
  }
  }
</script>