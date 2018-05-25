<template>
	<div>
		<div class="plusCamera"  @click="choiceImg">请选择设备图片上传</div>
		<img :src="src" v-show="show">
	</div>
</template>

<script > 
	 
	export default{
		data(){
			return{show:false,src:""}
		},
		methods:{
			choiceImg(){
				let self = this;
				if (!window.plus){
						alert("不支持 plus");
						return;
					}

				let title = "选择照片"
				let btns = ['拍照','相册']

				var func = function(e){  
	        var index = e.index;  
	        alert("inex="+index);
	        if(index == 1) self.choiceCamera();  
	        if(index == 2) self.choicePic();  
	    	}

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
			choiceCamera(){ 
				let self = this;
				//cmr.captureImage( successCB, errorCB, option );  
		    var cmr = plus.camera.getCamera();  
		    cmr.captureImage(function (p){  
		    	//plus.io.resolveLocalFileSystemURL( url, succesCB, errorCB );  
		    	//通过IO组件，获取文件对象
		        plus.io.resolveLocalFileSystemURL(p, function(entry){

		        	entry.file( function(file){
					      let reader = new FileReader();
		    				reader.readAsDataURL(file);
					      reader.onload = function(e){
					      	alert("支持 choiceImg");
					          alert(e.target.result)
					  			}
					       })

		            self.setImg(entry.toLocalURL());  
		        }, function(e){});  
		        plus.gallery.save( "_doc/a.jpg", function () {alert( "保存图片到相册成功" );} );
		    }, function(e){},{index:1,filename:"_doc/camera/"});  
			} , 

			choicePic(){  
				let self = this;
	    	plus.gallery.pick(function(path){
	    		let reader = new FileReader();
  				reader.readAsDataURL(path);
		      reader.onload = function(e){
		          alert(e.target.result)
		  			}
	    		self.setImg(path);},function(e){},{filter:'image'});  
			}, 
	},
	setImg(src){  
		alert("进入setimg");
    this.show=true;
    this.src=src;
}  
}
</script>
<style>
	.plusCamera{
		background-color: #9A2121;
		width: 100px;
		height: 100px;
	}
</style>