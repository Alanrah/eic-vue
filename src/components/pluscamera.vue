<template>
	<div>
		<div class="plusCamera"  @click="onPlusReady">请选择设备图片上传</div>
	</div>
</template>

<script > 
	 
	export default{
		methods:{
			onPlusReady() {
				if (!window.plus){
					alert("不支持 plus.camera");
					return;
				}
		    var cmr = plus.camera.getCamera();
		    alert( "Camera supperted image resolutions: " + cmr.supportedImageResolutions );
		}
		}
	}
</script>
<style>
	.plusCamera{
		width: 100px;
		height: 100px;
	}
</style>