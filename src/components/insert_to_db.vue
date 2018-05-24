<template>
	<div style="margin-top: 10px;">
		<div class="insert" v-show="showInsert">
			<p>识别结果如下：</p>

			<div v-show="showDeviceName" class="line">
				<p>该设备类型：<input class="input" v-model="deviceName"></p>
			</div>

			<div v-show="showPosition" class="line">
				<p>该设备位置：<input class="input" v-model="positionNum">U</p>	
			</div> 

			<div v-show="showSubmit" class="line">
				<select v-model="selectRoom">
			    <option disabled value="">选择机房</option>
			    <option>机房A</option>
			    <option>机房B</option>
			  </select>	

			  <select v-model="selectCabinet">
			    <option disabled value="">选择机柜</option>
			    <option>机柜1</option>
			    <option>机柜2</option>
			  </select>	

			<button  @click="submitInsert">确认添加设备到机房数据库</button>
		</div>
		</div>
	</div>
</template>
<script>
	import Bus from '../bus.js'
	export default {
		data(){
			return{
				deviceName:'',
				deviceFile:null,
				positionNum:-1,
				positionFile:null,
				selectRoom:'',
				selectCabinet:'',
			}
		},
		computed:{
			showSubmit(){
				return this.showDeviceName & this.showPosition;
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
				if(this._data.deviceName!='')
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
  } ,
  methods:{
  	submitInsert(){
  		if(this._data.positionNum==-1)
  			alert("缺少设备位置信息")
  		if(this._data.deviceName =='' || this._data.deviceName =='识别出错')
  			alert("缺少设备类型信息")
  		else{alert("功能正在完善")}

  	}
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