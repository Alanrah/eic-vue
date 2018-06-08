<template>
	<div>

		<header>
			<input type="text" placeholder="search device" class="inputSearch" v-model="keyword" v-on:input="search"/>
		</header>

			<div class="panel" v-show="showItem">
				<Item  v-for="(item,index) in lists" :item="item" :key="index"></Item>
		</div>
		<div v-show="showItem" class="addroom" @click="roomInsert">
			添加新机房
		</div>
		<div class="preview" v-show="previewroom">
        <p class="inputp">名称：<input class="input" placeholder="必填" v-model="room.name"></p>
        <p class="inputp">所有者：<input class="input" placeholder="必填" v-model="room.owner"></p>
        <p class="inputp">地点：<input class="input" placeholder="必填" v-model="room.pos"></p>
        <p class="inputp">长度：<input class="input" v-model="room.length"></p>
        <p class="inputp">宽度：<input class="input"  v-model="room.width"></p>
        <p class="inputp">高度：<input class="input"  v-model="room.height"></p>
        <!--<p>图片：<input class="input" type="file"></p>-->
        <div class="bwrap">
         <button style="height:40px;margin-right:30px;"  @click="confirmAdd">确认</button>
         <button style="height:40px;"  @click="quitAdd">退出</button></div>
      </div>
			
			<div class="panel" v-show="searchResultShow">
	      <div  class="sheet-content" v-for="i in searchResult">
	          <div class="sheet-content-image">
	              <img class="image" :src="i.d_pic">
	          </div>
	          <div class="sheet-content-list">
	          	<div class="sheet-content-middle">
	              设备名称：{{i.d_name}}
		          </div>
		          <div class="sheet-content-middle">
		              所在机房名：{{i.r_name}}
		          </div>
		          <div class="sheet-content-middle">
		              所在机柜名：{{i.c_name}}
		          </div>
	          </div>
	      </div>
		</div>
	</div>
</template>
<script>
	import Item from './item.vue'
	import qs from "qs"
	import Bus from '../bus.js'
	export default{
		data(){//从服务器获取数据
			return{
				user:this.$USER,
				keyword: '',
				searchResult:[],
				lists:[],
				previewroom:false,
				room:{},
				searchResultShow:false,
				showItem:true,
			}
		},

		components:{
			Item,
		},
		created(){this.fetchData();},
		mounted(){
			Bus.$on('fresh',(e)=>{
				this.fetchData();
			})
		},
		watch:{
			keyword(newValue, oldValue) {  
        if(newValue == "")  {
        	this.searchResultShow =false;
      		this.showItem = true;
        }
    	}
		},
		methods:{
			search(){
				let keyword=this.keyword;
				if(keyword=="") {
					this.searchResultShow =false;
      		this.showItem = true;
					return
				}
				let searchResult = []

      	for( let list of this.lists){
      		for(let device of list.devices){
      			if(device.d_name.indexOf(keyword)>-1 || keyword.indexOf(device.d_name)>-1){
      					device.r_name = list.r_name;
		      			if(device.c_id>=1 && device.c_id !== device.d_id){
		      				for(let d of list.devices){
		      					if(d.d_id == device.c_id)
		      						device.c_name = d.d_name;
		      				}
		      			}
      				searchResult.push(device);
      			}
      			}
      		}

      	this.searchResult = searchResult;
      	this.searchResultShow =true;
      	this.showItem = false;
			},
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
							self.$USER.id = data[2][0];
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
							}
							for (var i in lists) {
								self.$set(self.lists,i,lists[i])
							}
							let t = self.cabinetList();
							Bus.$emit('cabinetss',t);
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
.sheet-content{
    display: flex;
    width: 720px;
    border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
    margin-top: 10px;
    margin-left: 30px;
    padding-top: 10px;
    flex-direction: row;
}

.sheet-content-image{
		border-width: 1px;
    border-style: solid;
    border-color: #e5e5e5;
    width: 200px;
    height:200px; 
}
.sheet-content-middle{
    text-align: center;
    margin-left: 5px;
    font-size: 40px;
    color: #666666;
}
.sheet-content-list{
	border-width: 1px;
  border-style: solid;
  border-color: #e5e5e5;
	width: 500px;
	display: flex;
	flex-direction: column;
	align-items: flex-start;
}
.image{
    width: 190px; 
    height:190px; 
    padding: 5px;
}

.bwrap{
	margin-top: 30px;
  display: flex;
  justify-content: center;
}
.inputp{
		height: 80px;
		margin: 20px auto auto 30px;
}
	.input{
		height: 70px;
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
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #EDEBEB;
  }
  .addroom{
  	color:  #666666;
		font-size: 40px;
    height: 50px;
    width: 250px;
    text-align: center;
    margin-top: 10px;
    margin-left: 250px;
		position: relative;
    border-width: 2px;
		border-style: solid;
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #D2E9FF;
		margin-bottom: 80px;
  }
</style>