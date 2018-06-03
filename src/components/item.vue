<template>
  <div class="sheet-list">
      <div class="sheet-header" >
          <i class="icon iconfont icon-enter" ref="toggleicon"></i>
          <span class="sheet-header-span" ><span @click="toggleSheet">机房: {{data_item.r_name }} ,设备数：{{data_item.num}}</span><span class="detail" @click="previewRoom">详</span> </span>
          <div class="preview" v-show="previewroom"  @click="previewRoom">
            <p>名称：{{data_item.r_name}}</p>
            <p>所有者：{{data_item.r_owner}}</p>
            <p>地点：{{data_item.r_pos}}</p>
            <p>长度：{{data_item.r_length}}</p>
            <p>宽度：{{data_item.r_width}}</p>
            <p>高度：{{data_item.r_height}}</p>
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
           <p>名称：{{device.d_name}}</p>
            <p>U位：{{device.d_u}}</p>
            <p>地点：{{device.d_pos}}</p>
            <p>长度：{{device.d_length}}</p>
            <p>宽度：{{device.d_width}}</p>
            <p>高度：{{device.d_height}}</p>
            <p>状态：{{device.d_status}}</p>
            <p>生产商：{{device.d_producer}}</p>
            <p>序列号：{{device.d_seq}}</p>
        <img class="previewImg" :src="device.d_pic">
      </div>
  </div>
</template>

<script>
  import qs from "qs"
export default {
  components:{},
  props: {
      item:{
      type:Object
      }
  },
  data(){
  return{
      showSheets:false,
      data_item:{},
      editicon:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525925336206&di=0639d0503540384d2ca6ca92d1a90e3b&imgtype=0&src=http%3A%2F%2Fpic.qiantucdn.com%2F58pic%2F14%2F99%2F24%2F86m58PICvDW_1024.jpg",
      delicon:"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=225219922,1963963014&fm=27&gp=0.jpg",
      isPreview: false,
      previewroom:false,
      device:{},
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
        vm.isPreview = true;
        vm.device = i;
      },
      closePreview: function () {
        let vm = this;
        vm.isPreview = false;
        vm.device = {};
      },
      edit:function(){alert("功能正在完善")},

      delet:function(device){
        let vm = this;
        vm.isPreview = false;
        vm.device = {};
        let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
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
                alert(error);
             })
      },

    },
      created(){
        this.data_item = this.item;
      },
}
</script>


<style scoped="scoped">
.sheet-list{
  margin-top: 2px;
  margin-bottom: 2px;
}
.sheet-header{
    height: 60px;
    width: 748px;
    background-color: #B5F0E6;
    bottom: 2px;
    border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
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
    border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
    margin-top: 4px;
    margin-left: 30px;
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
  width: 500px;
  height: 600px;
  top: 300px;
  left: 200px;
  position: fixed;
  border-width: 1px;
  border-style: solid;
  border-color: #e5e5e5;
  background-color: #B5F0E6;
  z-index: 99;
  overflow: scroll;
}
.previewImg{
  width: 100%;
  height: 40%;
}
.detail{
  background-image:url('http://pic.58pic.com/58pic/14/63/61/71s58PICrAg_1024.jpg');
  background-size:100% 100%;
  float:right;
}
</style>