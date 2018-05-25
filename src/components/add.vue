<template>
	<div>
		<div class="modifyEquip" v-on:click="jump">
			修改个人机房设备信息
		</div>
		
		<device></device>
		<position></position>
		<inserttodb></inserttodb>
		<pluscamera></pluscamera>
		<!---->
	</div>
</template>
<script>

//上传图片到服务器
	import Bus from '../bus.js'
	import device from './device.vue'
	import position from './position.vue'
	import inserttodb from './insert_to_db.vue'
	import pluscamera from './pluscamera.vue'

	export default{
		
		methods:{
			jump:function(){
				this.$router.push('index');
				Bus.$emit('jumptoindex', 'index');//添加一个 触发 #emit的事件按钮
			},
		},
		components:{
			device,
			position,
			inserttodb,

			pluscamera,
		}
	}
</script>
<style scoped="scoped">
	.icon{
		display: flex;
		width: 740px;
		margin-top: 100px;
		flex-direction: column;
    align-items: center;
		overflow: hidden;
	}
	
	.modifyEquip{
		display: none;
		height: 68px;
		width: 740px;
		line-height: 80px;
		text-align: center;
		padding-left: 100px;
		font-size: 40px;
		padding-left: 40px;
		padding-bottom: 5px;
		border-width: 1px;
		border-style: solid;
		border-color: #A8A8A8;
		border-radius: 25px;
		position: fixed;
		bottom: 95px;
		background-color: #A7A5A5;
	}
</style>