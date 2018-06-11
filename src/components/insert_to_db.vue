<template>
	<div class="rapp">
		<div class="insert" v-show="showInsert">
			<p>识别结果如下：</p>

			<div v-show="showDeviceName" class="line">
				<p>该设备名称：<input class="input" v-model="deviceName"></p>
			</div>

			<div v-show="showDeviceName" class="line">
				<p>该设备类型：<input class="input" v-model="deviceClass"></p>
			</div>

			<div v-show="showPosition" class="line">
				<p>该设备位置：<input class="input" v-model="positionNum">U</p>	
			</div> 

			<div v-show="showSubmit" class="line">
				<select  class="selecto" v-model="selectRoom">	
					<option disabled value="">选择机房</option>
			    <option v-for="option in cabinets" v-bind:value="option.r_id">{{ option.r_name }}</option>
			  </select>	

			  <select class="selecto" v-model="selectCabinet">
			    <option disabled value="">选择机柜</option>
			    <option v-for="option in cabinetOption" v-bind:value="option.d_id">{{ option.d_name }}</option>
			    <option value=0>不在机柜里</option>
			    <option value=-1>是机柜</option>
			  </select>	
			<br>
			<button style="height:30px;margin-bottom: 80px;"  @click="submitInsert">确认添加设备到机房数据库</button>
		</div>
		</div>
	</div>
</template>
<script>
	import Bus from '../bus.js'
	import qs from "qs"
	export default {
		data(){
			return{
				deviceName:null,//d_name
				deviceClass:null,//d_class
				deviceFile:null,//d_pic
				positionNum:-1,//d_u
				positionFile:null,//pos_pic
				selectRoom:'',//r_id
				selectCabinet:'',//c_id
				cabinets:null,
			}
		},
		computed:{
			cabinetOption(){
				if(! this.cabinets && !this.selectRoom)
					return;
				for(let room of this.cabinets){
					if(room.r_id  == this.selectRoom)
						return room.cabinets;
				}
			},
			showSubmit(){
				return this.showDeviceName ;
			},
			showInsert(){
				return this.showDeviceName | this.showPosition;
			},
			showPosition(){
				if(this._data.positionNum!=-1)
					return true;
				return false;
			},
			showDeviceName(){
				if(this._data.deviceClass!=null)
	    		return true;
				return false;
			}
		},
		created(){
			console.log("created")
	    	console.log(this.cabinets)
			this.cabinets=JSON.parse(localStorage.getItem("cabinetInfo"));
		},
		mounted(){
			Bus.$on('cabinetss',(e)=>{
	    	this._data.cabinets = e;
	    	if(!this.cabinets)
	    		this.cabinets=JSON.parse(localStorage.getItem("cabinetInfo"));
	    	console.log("mounted")
	    	console.log(this.cabinets)
	    });
	    Bus.$on('device',(e)=>{
	    	this._data.deviceClass=e.deviceName;
	    	this._data.deviceName=e.deviceName;
	    	this._data.deviceFile=e.file;
	    });
	    Bus.$on('position',(e)=>{
	    	this._data.positionNum=e.positionNum;
	    	this._data.positionFile=e.file;
	    });

	    
  } ,
  methods:{
  	submitInsert(){
  		var self =this;
  		let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }
      let d_u = self.positionNum;
       if(self.selectCabinet ==''){//是机柜
       	self.selectCabinet = 0;
       	d_u=0;
       }
       if(self.selectCabinet ==0){//不在机柜里
       	 d_u=-1;
       }

       if(self._data.positionNum==-1 && self.selectCabinet !=='')
  			alert("缺少设备位置信息")
  		if((self._data.deviceClass =='' || self._data.deviceClass =='识别出错')&&self.selectCabinet > 0)
  			alert("缺少设备类型信息")
       	

      let para ={"r_id":self.selectRoom.toString() ,"c_id":self.selectCabinet,"pos_pic":d_u,"d_class":self.deviceClass,"d_name":self.deviceName,"d_u":self.positionNum,"d_pic":self.deviceFile}


      self.$axios.post('http://'+self.$IP+'/operate/insertDevice', qs.stringify(para), config)
          .then(response => {
            if(response.status == 200){
              if( window.plus)
              plus.nativeUI.toast("添加成功");
            else
              alert("添加成功")
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
              if( window.plus)
              	plus.nativeUI.toast(error);
           })
  	},
  }
	}
</script>
<style>
.rapp{
	margin-top: 10px;
	color:#666666;
	margin-left:30px;
}
	.insert{
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}
	.line{
		height: 70px;
		float: left;
		margin-top: 0px;
		margin-top: 10px;
	}
	.input{
		height: 60px;
		width: 200px;
	}
	.selecto{
		height:50px;
		margin-bottom: 20px;
	}
</style>