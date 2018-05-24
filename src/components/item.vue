<template>
  <div class="sheet-list">
      <div class="sheet-header" @click="toggleSheet">
          <i class="icon iconfont icon-enter" ref="toggleicon"></i>
          <span class="sheet-header-span">{{" 机房名: "+data_item.r_name +" 设备数："+data_item.num}} </span>
      </div>

      <div v-if="showSheets" class="sheet-content" v-for="i in data_item.devices">
          <div class="sheet-content-image">
              <img class="image" :src="i.d_pic">
          </div>
          <div class="sheet-content-middle" @click="previewImage(i)">
              {{i.d_name}}
          </div>
          <div class="sheet-content-image" @click="edit">
              <img class="imageicon" :src="editicon">
          </div>
          <div class="sheet-content-image" @click="delet">
              <img class="imageicon" :src="delicon">
          </div>
      </div>

      <div class="preview" v-show="isPreview" @click="closePreview"> 
        <p>{{previewName}}：详情待补充</p>
        <img class="previewImg" :src="previewImg">
      </div>
  </div>
</template>

<script>
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

      previewImg:"",
      previewName:"",
  }
  },
  methods:{

//向右的小图标动画
      toggleSheet:function(index){
          console.log(this.$refs);
          this.$refs.toggleicon.style.transform = !this.showSheets ? 'rotate(90deg)' : 'rotate(0)'
          this.showSheets = !this.showSheets
      },
      previewImage: function (i) {
        let vm = this;
        vm.isPreview = true;
        vm.previewImg = i.d_pic;
        vm.previewName = i.d_name;
      },
      closePreview: function () {
        let vm = this;
        vm.isPreview = false;
        vm.previewImg = "";
        vm.previewName = ""
      },
      edit:function(){alert("功能正在完善")},
      delet:function(){alert("功能正在完善")},
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
  width: 350px;
  height: 300px;
  top: 300px;
  left: 200px;
  position: fixed;
  border-width: 1px;
  border-style: solid;
  border-color: #e5e5e5;
  background-color: #F7F7F7;
  z-index: 99;
}
.previewImg{
  width: 100%;
  height: 40%;
}
</style>