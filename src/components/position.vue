<template>
	<div>

		<div class="camera-photo" ref="divGenres" v-show="isPhoto" @click="choiceImg">
        <img src="../assets/icon_photo.png" />
        <br>
        <span>请选择位置图片上传</span>
        <input type="file" ref="uploadImage" @change="onFileChange" accept="image/*" capture="camera" style="display: none;">
      </div>

    <div class="list-li" v-show="show">
	    <div style="display: inline-block;">
	    	<a class="list-link" @click='previewImage(imgsrc)'>
		      <img :src="imgsrc">
		    </a>
		    <span class="list-img-close" @click='delImage'></span>
	    </div>
	    <div class="add-preview" v-show="isPreview" @click="closePreview">
	      <img :src="previewImg">
	    </div>
	    <button type="button" class="upload-button" @click="upload">识别该设备位置</button> 
	  </div>
	</div>
</template>

<script>  
  import Bus from '../bus.js'
  import qs from "qs"
	export default {  
		data(){
			return{
				imgsrc:'',
				show:false,
				previewImg: '',
        isPreview: false,
        isPhoto: true,
        positionNum:-1,
        positionImg:null,
        showPosition:false,
        uploadFile:null
			}
		},
		watch: {
      show: 'toggleAddPic'
    },
		methods:{
      upload(){
        var self = this
        var wt ;
        if (window.plus)
          wt = plus.nativeUI.showWaiting();
        var img = new Image,
            width = 512, //image resize   压缩后的宽
            quality = 0.5, //image quality  压缩质量
            canvas = document.createElement("canvas"),
            drawer = canvas.getContext("2d");
       img.src = self.imgsrc;
       img.onload = function(){
       canvas.width = width;
       canvas.height = width * (img.height / img.width);
        drawer.drawImage(img, 0, 0, canvas.width, canvas.height);
        var base64 = canvas.toDataURL("image/*", quality); 
        var pic = base64.split(',')[1];
        var f=self.imgsrc;
        var filename=f.replace(f.substring(0, f.lastIndexOf('/') + 1), '');

        if(self.uploadFile !== null){
          console.log("web")
          filename =  self.uploadFile.name
          let reader = new FileReader();
          reader.readAsDataURL(self.uploadFile);
          reader.onload = function(e){
            img.src = e.target.result;
          }
         img.onload = function(){
         canvas.width = width;
         canvas.height = width * (img.height / img.width);
          drawer.drawImage(img, 0, 0, canvas.width, canvas.height);
          base64 = canvas.toDataURL("image/*", quality); 
          pic = base64.split(',')[1];
        }
}
        let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
          }
      

        let para ={"fileString":pic,"filename":filename}

        self.$axios.post('http://'+self.$IP+':5000/position', qs.stringify(para), config)
            .then(response => {
              self.positionNum = response.data.split(',')[1];
              self.showPosition = true;
              let picUrl = response.data.split(',')[0];
              let d = {"file":picUrl,"positionNum":self.positionNum}
              Bus.$emit('position', d);
               if (window.plus)
              wt.close();
            })
            .catch(function (error) {
                alert(error);
                 if (window.plus)
                wt.close();
             })
      }
    },

			toggleAddPic: function () {
        let vm = this;
        if (vm.show === true) {
          vm.isPhoto = false;
        } else {
          vm.isPhoto = true;
        }
      },
			onFileChange(e){
				let self = this;

				let files = e.target.files || e.dataTransfer.files;
        if (!files.length) return;
        let file = files[0];//File对象
        self.uploadFile = file;

        let reader = new FileReader();//FileReader对象

		    reader.readAsDataURL(file);//该方法会读取指定的 Blob 或 File 对象。读取操作完成的时候，readyState 会变成已完成（DONE），并触发 loadend 事件，同时 result 属性将包含一个data:URL格式的字符串（base64编码）以表示所读取文件的内容。

		    reader.onload = function(e){
          let base64Code=this.result;
	        self.imgsrc= e.target.result;//图片内容的base64编码
	        self.show = true;
		    }
			},
			addPic: function (e) {
        let els = this.$refs.divGenres.querySelectorAll('input[type=file]')
        els[0].click()
        return false
      },
			delImage: function () {
	        this.imgsrc = "";
	        this.show = false;
	        this.isPreview = false;
          this.positionNum=-1;
          Bus.$emit('position', {"file":null,"positionNum":this.positionNum});
      },
      previewImage: function (url) {
        let vm = this;
        vm.isPreview = true;
        vm.previewImg = url;
      },
      closePreview: function () {
        let vm = this;
        vm.isPreview = false;
        vm.previewImg = "";
      },
      choiceImg(){
        let self = this;
        if (!window.plus){
            self.addPic()
            return;
          }

        let title = "选择照片"
        let btns = ['拍照','相册']

        var func = function(e){  
          var index = e.index;  

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
        cmr.captureImage(function (path){  

            plus.io.resolveLocalFileSystemURL(path, function(entry){
                  self.imgsrc= entry.toLocalURL();
                  self.show = true; 
                  console.log("camera:"+entry.toLocalURL())
 
            }, function(e){plus.nativeUI.toast("读取拍照文件错误：" + e.message);  });  
        }, function(e){},{index:1,filename:"_doc/camera/"});  
      } , 

      choicePic(){  
        let self = this;
         plus.gallery.pick( function(p){  
           plus.io.resolveLocalFileSystemURL(p, function(entry) { 
                  self.imgsrc= entry.toLocalURL();
                  self.show = true; 
                  console.log("choice:"+entry.toLocalURL()) 
          }, function(e) {  
              plus.nativeUI.toast("读取拍照文件错误：" + e.message);  
          });  
           }, function ( e ) {  plus.nativeUI.toast("读取拍照文件错误：" + e.message);}, {  
          filename: "_doc/camera/",  
          filter:"image"  
           } );  
      },  
	},
}
</script> 

<style>
	.upload-button{
		display: block;
    margin-top: 10px;
	}
	.camera-photo{
		text-align:center;
		margin-top:80px;
	}
	.list-li {

		display: flex;
		flex-direction: column;
    align-items: center;
		padding: 8px;
    margin-top:10px;
    position: relative;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }
  .list-link img {
    width: 150px;
    height: 150px;
  }
  .list-link a:visited {
    background-color: #465c71;
    border: 1px #4e667d solid;
    color: #dde4ec;
    display: flex;
    line-height: 1.35em;
    padding: 4px 20px;
    text-decoration: none;
    white-space: nowrap;
    overflow: hidden;
  }
  .list-link a:hover {
    background-color: #bfcbd6;
    color: #465c71;/
    text-decoration: none;
  }
  .list-link a:active {
    background-color: #465c71;
    color: #cfdbe6;
    text-decoration: none;
  }
  .list-img-close {
    background: #ffffff url(https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1526905315674&di=4c2d6a6985b34e141f37bc9fae7f2209&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F15%2F55%2F73%2F39I58PICCqK_1024.png) no-repeat right top;
    border-color: #ff4a00;
    background-position: center;
    background-size: 35px 35px;
    display: block;
    float: left;
    top: 5px;
    width: 10px;
    height: 10px;
    position: absolute;
    margin-top: 0px;
    margin-left: 135px;
    padding: 8px;
    z-index: 10;
    border-radius: 5px;
    text-align: center;
  }
  .add-preview{
  	width: 300px;
    height: 300px;
  }
  .add-preview img{
  	width: 100%;
    height: 100%;
  }
</style>