<template>
	<div class="out">
		<div class="mui-content-padded">
			<img class="device-img" @click="choiceImg" :src="imgsrc"/>
			<button class="mui-btn mui-btn-primary device-btn" @click="uploadImg">开始识别</button>
			<p id="res"></p>
		</div>
		
		<form method="post" action="http://upload.qiniu.com/" enctype="multipart/form-data" id="deviceForm">
			<input name="file" type="file" />
			<input name="key" type="hidden" />
			<input name="token" type="hidden" />
		</form>
		</div>
	
</template>
<script>
	import jquery from 'jquery'
	//import  '../../shisuilib/js/mui.js'
	
	//import "../../shisuilib/js/lib/jquery/jquery-1.11.2.min.js"
	//import "../../shisuilib/js/lib/jquery/jquery.form.js"
	// import "../../shisuilib/js/lib/encode/core-min.js"
	// import "../../shisuilib/js/lib/encode/cipher-core-min.js"
	// import "../../shisuilib/js/lib/encode/enc-base64-min.js"
	// import "../../shisuilib/js/lib/encode/hmac-min.js"
	// import "../../shisuilib/js/lib/encode/sha1-min.js"
	//import  '../../shisuilib/js/lib/qiao.js'
	export default{
		data(){
			return{
				imgsrc:"",
			}
		},
		methods:{
			choiceImg(){
					this.sheet('选择照片', ['拍照','相册'], function(e){
					var index = e.index;
					if(index == 1) choiceCamera();
					if(index == 2) choicePic();
				});
			},
			choiceCamera(){
				var cmr = plus.camera.getCamera();
				cmr.captureImage(function (p){
					plus.io.resolveLocalFileSystemURL(p, function(entry){
						setImg(entry.toLocalURL());
					}, function(e){});
				}, function(e){},{index:1,filename:"_doc/camera/"});
			},
			choicePic(){
				plus.gallery.pick(function(path){setImg(path);},function(e){},{filter:'image'});
			},
			setImg(src){
				this.imgsrc=src;
			},
			uploadImg(){},

			sheet: function(title, btns,func){
			if(title && btns && btns.length > 0){
				var btnArray = [];
				for(var i=0; i<btns.length; i++){
					btnArray.push({title:btns[i]});
				}
				
				plus.nativeUI.actionSheet({
					title : title,
					cancel : '取消',
					buttons : btnArray
				}, function(e){
					if(func) func(e);
				});
			}
		},

		},
	}
</script>
<style scoped="scoped">
#res{
	margin: 10px auto;
	width: 300px;
}
form{
	display: none;
}
	.mui-btn-primary, .mui-btn-blue
{
    color: #fff;
    border: 1px solid #007aff;
    background-color: #007aff;
}
	.mui-btn
{
    font-size: 14px;
    font-weight: 400;
    line-height: 1.42;

    position: relative;

    display: inline-block;

    margin-bottom: 0;
    padding: 6px 12px;

    cursor: pointer;
    -webkit-transition: all;
            transition: all;
    -webkit-transition-timing-function: linear;
            transition-timing-function: linear;
    -webkit-transition-duration: .2s;
            transition-duration: .2s;
    text-align: center;
    vertical-align: top;
    white-space: nowrap;

    color: #333;
    border: 1px solid #ccc;
    border-radius: 3px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
    border-bottom-left-radius: 3px;
    background-color: #fff;
    background-clip: padding-box;
}
.out{
	display: flex;
	flex-direction: column;
	align-items: center;
}
	.mui-content-padded{
	margin-top: 50px;
}
.device-img{
	display: block;
	margin: 0 auto;
	width: 300px;
	height: 400px;
}
.device-btn{
	display: block;
	margin: 20px auto;
	height: 60px;
	width: 300px;
	font-size: 20px;
	background-color: #007aff;
}
</style>