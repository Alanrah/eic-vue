<template>
	<div>

		<div class="camera-photo" ref="divGenres" v-show="isPhoto" @click.stop="addPic">
        <img src="../assets/icon_photo.png" />
        <br>
        <span>请选择或者拍照上传照片</span>
        <input type="file" @change="onFileChange" accept="image/*" capture="camera" style="display: none;">
      </div>

    <div class="list-li" v-show="show">
	    <div style="display: inline-block;">
	    	<a class="list-link" @click='previewImage(imgsrc)'>
		      <img :src="imgsrc">
		    </a>
		    <span class="list-img-close" @click='delImage'></span>
	    </div>
	    <br>
	    <div class="add-preview" v-show="isPreview" @click="closePreview">
	      <img :src="previewImg">
	      <br>
	    </div>
	    <button type="button" class="upload-button">识别该设备</button> 
	  </div>

	  
		
	</div>
</template>

<script>  

	export default {  
		data(){
			return{
				imgsrc:'',
				show:false,
				previewImg: '',
        isPreview: false,
        isPhoto: true,
			}
		},
		watch: {
      show: 'toggleAddPic'
    },
		methods:{
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
        let file = files[0];
        let reader = new FileReader();
		    reader.readAsDataURL(file);
		    reader.onload = function(e){
	        self.imgsrc= e.target.result;
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
	},
}
</script> 

<style>
	.upload-button{
		display: block;
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
    margin-top:80px;
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