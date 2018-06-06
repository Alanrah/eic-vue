<template>
  <div class="sheet-list">
      <div class="sheet-header" >
          <i class="icon iconfont icon-enter" ref="toggleicon"></i>
          <span class="sheet-header-span" >
            <span @click="toggleSheet">机房: {{data_item.r_name }} ,设备数：{{data_item.num}}</span>
            <span class="detail" @click="previewRoom"></span> 
          </span>
          <div class="preview" v-show="previewroom"  @click="previewRoom">
            <p class="input">名称：{{data_item.r_name}}</p>
            <p class="input">所有者：{{data_item.r_owner}}</p>
            <p class="input">地点：{{data_item.r_pos}}</p>
            <p class="input">长度：{{data_item.r_length}}</p>
            <p class="input">宽度：{{data_item.r_width}}</p>
            <p class="input">高度：{{data_item.r_height}}</p>
            <img class="previewImg" :src="data_item.r_pic" alt="机房图片">
          </div>
      </div>

      <div v-if="showSheets" class="sheet-content" v-for="i in data_item.devices">
          <div class="sheet-content-image">
              <img class="image" :src="i.d_pic">
          </div>
          <div class="sheet-content-middle" @click="previewDevice(i)">
              {{i.d_name}}
          </div>
          <div class="sheet-content-image" @click="edit(i)">
              <img class="imageicon" :src="editicon">
          </div>
          <div class="sheet-content-image" @click="delet(i)">
              <img class="imageicon" :src="delicon">
          </div>
      </div>

      <div class="preview" v-show="isPreview" @click="closePreview"> 
           <p class="input">名称：{{device.d_name}}</p>
            <p class="input">U位：{{device.d_u}}</p>
            <p class="input">长度：{{device.d_length}}</p>
            <p class="input">宽度：{{device.d_width}}</p>
            <p class="input">高度：{{device.d_height}}</p>
            <p class="input">状态：{{device.d_status}}</p>
            <p class="input">生产商：{{device.d_producer}}</p>
            <p class="input">序列号：{{device.d_seq}}</p>
        <img class="previewImg" :src="device.d_pic" alt="设备图片">
      </div>

      <div class="preview" v-show="editDeviceShow">
            <p>名称：<input class="inputt" v-model="device.d_name"></p>
            <p>U位：<input class="inputt" v-model="device.d_u"></p>
            <p>长度：<input class="inputt" v-model="device.d_length"></p>
            <p>宽度：<input class="inputt" v-model="device.d_width"></p>
            <p>高度：<input class="inputt" v-model="device.d_height"></p>
            <p>状态：<input class="inputt" v-model="device.d_status"></p>
            <p>生产商：<input class="inputt" v-model="device.d_producer"></p>
            <p>序列号：<input class="inputt" v-model="device.d_seq"></p>
            <div class="bwrap"> <button @click="confirmEdit">确认修改</button>
              <button @click="quitEdit">退出修改</button></div>
      </div>
  </div>
</template>

<script>
  import qs from "qs"
  import Bus from '../bus.js'
export default {
  components:{},
  props: {
      item:{
      type:Object
      }
  },
  watch: {  
    item: {  
　　　　handler(newValue, oldValue) {  
            this.data_item = newValue//数据视图舒心成功
　　　　　　},  
　　　　deep: true  
　　　　}  
    } ,
  data(){
  return{
      showSheets:false,
      data_item:this.item,
      editicon:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525925336206&di=0639d0503540384d2ca6ca92d1a90e3b&imgtype=0&src=http%3A%2F%2Fpic.qiantucdn.com%2F58pic%2F14%2F99%2F24%2F86m58PICvDW_1024.jpg",
      delicon:"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=225219922,1963963014&fm=27&gp=0.jpg",
      isPreview: false,
      previewroom:false,
      device:{},
      editDeviceShow:false,
    }
  },
  methods:{

//向右的小图标动画
      toggleSheet:function(index){
          event.preventDefault();
          this.$refs.toggleicon.style.transform = !this.showSheets ? 'rotate(90deg)' : 'rotate(0)'
          this.showSheets = !this.showSheets
      },
      previewRoom:function(e){
        if(this.previewroom)
          this.previewroom=false;
        else
          this.previewroom=true;
        e.stopPropagation()
      },
      previewDevice: function (i) {
        let vm = this;
        vm.editDeviceShow = false;
        vm.isPreview = true;
        vm.device = i;
      },
      closePreview: function (e) {
        e.stopPropagation()
        e.preventDefault();
        let vm = this;
        vm.isPreview = false;
        vm.device = {};
      },

      edit:function(device){
        let vm = this;
        vm.editDeviceShow = true;
        vm.isPreview = false;
        vm.device = device;

      },
      quitEdit:function(){
        this.editDeviceShow = false;
        this.device = {};
      },
      confirmEdit:function(event){
        event.preventDefault();
        let vm = this;

        let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }
        let para =vm.device;
        vm.$axios.post('http://'+vm.$IP+'/operate/editDevice', qs.stringify(para), config)
            .then(response => {
              if(response.status == 200){
                if( window.plus)
                  plus.nativeUI.toast("修改成功");
                else
                  alert("修改成功")

              Bus.$emit('fresh');
              vm.editDeviceShow = false;
              vm.device = {};
              }

            })
            .catch(function (error) {
                if( window.plus)
                  plus.nativeUI.toast(error);
                else
                  alert(error)
             })
      },

      delet:function(device){
        let vm = this;
        vm.isPreview = false;
        vm.device = {};
        let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }
        let para ={"user":vm.$USER.user,"device_id":device.d_id}
        vm.$axios.post('http://'+vm.$IP+'/operate/delete', qs.stringify(para), config)
            .then(response => {
              if(response.status == 200){
                if( window.plus)
                  plus.nativeUI.toast("删除成功");
                else
                  alert("删除成功")
              Bus.$emit('fresh')
              }

            })
            .catch(function (error) {
                if( window.plus)
                  plus.nativeUI.toast(error);
                else
                  alert(error)
             })
      },

    },
      created(){
        //this.data_item = this.item;
      },
}
</script>


<style scoped="scoped">
.input{
    height: 70px;
    width: 100%;
    margin-top: 10px;
  }
  .inputt{
    height: 70px;
    width: 300px;
  }
.sheet-list{
  margin-top: 2px;
  margin-bottom: 2px;
  color: #666666;
}
.sheet-header{
    height: 80px;
    width: 748px;
    background-color: #D2E9FF;
    bottom: 2px;
    border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
    padding-top: 10px;
}

.sheet-header-span{
    left: 15px;
    font-size: 40px;
    width: 720px;
    position:absolute;
}
.sheet-content{
    display: flex;
    width: 720px;
    height: 70px;
    border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
    margin-top: 5px;
    margin-left: 30px;
    padding-top: 10px;
    flex-direction: row;
}

.sheet-content-image{
    width: 100px;
    height:60px; 
}
.sheet-content-middle{
    width: 400px;
    height: 60px;
    text-align: center;
    margin-left: 5px;
    font-size: 40px;
    color: #666666;
}
.image{
    width: 80px; 
    height:60px; 
    padding: 5px;
}
.imageicon{
    width: 50px; 
    height:50px; 
    margin-top:5px;
    flex-direction: row;
    justify-content: center;
}
.preview{
  width: 450px;
  height: 700px;
  top: 200px;
  position: fixed;
  margin-left:150px;
  margin-right:auto;
  max-width: 500px;
  background: #ECECEC;
  padding: 30px 30px 20px 30px;
  box-shadow: rgba(187, 187, 187, 1) 0 0px 20px -1px;
  -webkit-box-shadow: rgba(187, 187, 187, 1) 0 0px 20px -1px;
  font: Arial, Helvetica, sans-serif;
  color: #666;
  border-radius: 10px;
  -webkit-border-radius: 10px;
  z-index: 99;
  overflow: scroll;
}

.previewImg{
  width: 200px;
  height: 200px;
}
.bwrap{
  display: flex;
  justify-content: center;
  padding-left: 20px;
}

.detail{
  background-image:url('http://10.108.104.228:5000/static/devicePic/assets/detail.png');
  background-size:100% 100%;
  float:right;
  width: 80px;
  height: 80px;
}
</style>