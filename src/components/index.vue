<template>
	<div class="out">

		<header>
			<input type="text" placeholder="search" class="inputSearch" :autofocus=false value=""/>
		</header>

		<div class="panel" >
				<Item v-for="(item,index) in lists" :item="item" :key="index" @childrefresh="fetchData"></Item>
		</div>
		<div class="addroom" @click="roomInsert">
			添加新机房
		</div>
		<div class="preview" v-show="previewroom">
        <p>名称：<input class="input" v-model="room.name"></p>
        <p>所有者：<input class="input" v-model="room.owner"></p>
        <p>地点：<input class="input" v-model="room.pos"></p>
        <p>长度：<input class="input" v-model="room.length"></p>
        <p>宽度：<input class="input"  v-model="room.width"></p>
        <p>高度：<input class="input"  v-model="room.height"></p>
        <!--<p>图片：<input class="input" type="file"></p>-->
        <div class="bwrap">
         <button   @click="confirmAdd">确认</button>
         <button   @click="quitAdd">退出</button></div>
      </div>

	</div>
</template>
<script>
	import Item from './item.vue'
	import qs from "qs"
	import Vue from 'vue'
	import Bus from '../bus.js'
	export default{
		data(){//从服务器获取数据
			return{
				user:this.$USER,
				txtInput: '',
        txtChange: '',
        searchValue:"",
				lists:[],
				refreshing:false,
				previewroom:false,
				room:{}
			}
		},

		components:{
			Item,
			
		},
		mounted(){
			this.fetchData();
			Bus.$on('fresh',(e)=>{
				this.fetchData();
			})
		},
		methods:{
			fetchData(){
				console.log("刷新data")
				var self =this
				let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }
        let para ={"user":self.$USER.user}
				self.$axios.post('http://'+self.$IP+'/fetch', qs.stringify(para), config)
            .then(response => {
              let data = response.data;
							let deviceInfo=data[1];
							self.$USER.id =deviceInfo[0].u_id;

							if(self.lists)
								self.lists.splice(0, self.lists.length)

							let lists=data[0];
							for(let list of lists){
								list.devices=[];
								list.num=0;
								for(let device of deviceInfo){
									if(device.r_id == list.r_id){
										list.devices.push(device);
										list.num = list.num+1;
									}
								}
								self.lists.push(list)
							}
							for (var i in lists) {
								Vue.set(self.lists,i,lists[i])
							}
							console.log(self.lists)

							let t = self.cabinetList();
							console.log("fetchdata")
			      	console.log(t)
							Bus.$emit('cabinetss',t);
							console.log(Bus)
							console.log("触发")
            })
            .catch(function (error) {
                alert(error);
             })           
          },
      cabinetList(){
      	var self =this
      	if(! self.lists)
      		return ;
      	let cabinetInfo = []
      	for( let list of self.lists){
      		let roomCabinets = {}
      		roomCabinets.r_id = list.r_id;
      		roomCabinets.r_name = list.r_name;
      		roomCabinets.r_owner = list.r_owner;
      		roomCabinets.cabinets = [];
      		for(let device of list.devices){
      			if(device.c_id==device.d_id)
      				roomCabinets.cabinets.push(device);
      		}
      		cabinetInfo.push(roomCabinets)
      	}
      	self.$CabinetInfo = cabinetInfo
      	localStorage.setItem("cabinetInfo",JSON.stringify(cabinetInfo));
      	return cabinetInfo;
      },

    roomInsert:function(e){
    	event.preventDefault();
    	this.previewroom=true;
    },
    onFileChange(e){
    	var self  = this
    	let files = e.target.files || e.dataTransfer.files;
        if (!files.length) return;
        let file = files[0];
        let reader = new FileReader();
		    reader.readAsDataURL(file);
		    reader.onload = function(e){
	        self.room.pic= e.target.result;//图片内容的base64编码
		    }
    },
    quitAdd(){
			this.previewroom =false;
    },

    confirmAdd:function(e){
    	event.preventDefault();
    	let self = this;
    	self.room.uid = self.$USER.id;
    	self.previewroom =false;
    	let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
          }
      let para =self.room;

      self.$axios.post('http://'+self.$IP+'/operate/addroom', qs.stringify(para), config)
          .then(response => {
            if(response.status == 200){
              if( window.plus)
              plus.nativeUI.toast("添加成功");
            else
              alert("添加成功")
            self.previewroom =false;
            Bus.$emit('fresh')
            }
            else{
            	if( window.plus)
              plus.nativeUI.toast("添加失败");
            else
              alert("添加失败")
            }

          })
          .catch(function (error) {
              alert("添加失败了")
              self.previewroom =false;
           })
         
    },
	}
}
</script>
<style scoped="scoped">
.bwrap{
  display: flex;
  justify-content: center;
}
	.input{
		height: 50px;
		width: 200px;
	}
.preview{
	display: flex;
	flex-direction: column;
  width: 450px;
  height: 700px;
  top: 200px;
  position: fixed;
  margin-left:150px;
  background: #ECECEC;
  color: #666;
  border-radius: 10px;
  z-index: 99;
  overflow: scroll;
  padding: 30px 30px 20px 30px;
}

	.image{
		width: 710px;
		height: 250px;
		position: absolute;
		top: 32px;
		left: 14px;
	}
	.panel{
		display: flex;
		width: 710px;
		margin-left: 16px;
		margin-top: 10px;
		margin-bottom: 20px;
		flex-direction: column;
		align-items: center;
		border-width: 2px;
		border-style: solid;
		border-color: rgb(162,217,192);
		border-color: rgba(162,217,192,0.2);

	}
	.text{
		font-size: 40px;
		text-align: center;
		color: #666666;
	}
	.inputSearch {
    font-size: 40px;
    height: 70px;
    width: 730px;
    margin-left: 10px;
    margin-top: 10px;
    margin-bottom: 5px;
    border-width: 2px;
		border-style: solid;
		border-color: rgb(162,217,192);
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #EDEBEB;
  }
  .addroom{
		float: left;
  	color:  #666666;
		font-size: 40px;
    height: 50px;
    width: 400px;
    text-align: center;
    margin: auto;
		position: relative;
    border-width: 2px;
		border-style: solid;
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #D2E9FF;
  }
  .out{
		display: flex;
		flex-direction: column;
  }
</style>