<template>
	<div style="margin-top: 10px;color:#666666;">
		<div class="insert" v-show="showInsert">
			<p>识别结果如下：</p>

			<div v-show="showDeviceName" class="line">
				<p>该设备名称：<input class="input" v-model="deviceName"></p>
			</div>

			<div v-show="showPosition" class="line">
				<p>该设备位置：<input class="input" v-model="positionNum">U</p>	
			</div> 

			<div v-show="showSubmit" class="line">
				<select v-model="selectRoom">	
					<option disabled value="">选择机房</option>
			    <option v-for="option in cabinets" v-bind:value="option.r_id">{{ option.r_name }}</option>
			  </select>	

			  <select v-model="selectCabinet">
			    <option disabled value="">选择机柜</option>
			    <option v-for="option in cabinetOption" v-bind:value="option.d_id">{{ option.d_name }}</option>
			    <option value=0>不在机柜里</option>
			    <option value=-1>是机柜</option>
			  </select>	

			<button  @click="submitInsert">确认添加设备到机房数据库</button>
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
				deviceFile:null,//d_pic
				positionNum:-1,//d_u
				positionFile:null,//pos_pic
				selectRoom:'',//r_id
				selectCabinet:'',//c_id
				cabinets:[],
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
				if(this._data.deviceName!=null)
	    		return true;
				return false;
			}
		},
		mounted(){
	    Bus.$on('device',(e)=>{
	    	this._data.deviceName=e.deviceName;
	    	this._data.deviceFile=e.file;
	    });
	    Bus.$on('position',(e)=>{
	    	this._data.positionNum=e.positionNum;
	    	this._data.positionFile=e.file;
	    });

	    Bus.$on('cabinets',(e)=>{
	    	if(e)
	    		this._data.cabinets = e;
	    	else 
	    		this._data.cabinets=self.$CabinetInfo
	    	
	    	console.log("cabinetInfo")
	    	console.log(this.cabinets)
	    });
  } ,
  methods:{
  	submitInsert(){
  		var self =this;
  		if(self._data.positionNum==-1 && self.selectCabinet !=='')
  			alert("缺少设备位置信息")
  		if(self._data.deviceName =='' || self._data.deviceName =='识别出错')
  			alert("缺少设备类型信息")

  		let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
          }

       if(self.selectCabinet =='')//d_u>1 && c_id 设备在机柜里，d_u=0,c_id =d_id 是机柜，d_u=0,c_id =0，设备不是机柜 不在机柜里
       	self.selectCabinet = -1;
       if(self.selectCabinet ==0)
       	self.positionNum=0

      let para ={"r_id":self.selectRoom.toString() ,"c_id":self.selectCabinet,"pos_pic":self.positionFile,"d_name":self.deviceName,"d_u":self.positionNum,"d_pic":self.deviceFile}

      console.log(para)

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
	.insert{
		display: flex;
		flex-direction: column;
		align-items: flex-start;
	}
	.line{
		height: 50px;
		float: left;
		margin-top: 0px;
	}
	.input{
		height: 30px;
		width: 200px;
	}
</style>