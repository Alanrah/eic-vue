<template>
	<div>
		<device></device>
		<position></position>
		<inserttodb></inserttodb>
	</div>
</template>
<script>

//上传图片到服务器
	import Bus from '../bus.js'
	import device from './device.vue'
	import position from './position.vue'
	import inserttodb from './insert_to_db.vue'
	export default{
		
		methods:{
			jump:function(){
				this.$router.push('index');
			},
		},
		components:{
			device,
			position,
			inserttodb,
		}
	}
</script>
