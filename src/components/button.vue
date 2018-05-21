<template>
  <div>
    <button></button>
  </div>
</template>
<script>
  module.exports = {
  	props:{
  		text:{
  			type:String,
  			required:true
  		}
  	},
    data: {
      disabled: false,//控制是否可用
      full: false//是否满宽度显示，否则显示650
    },
    methods:{
    	
    }

    }

</script>
<style>
  .btn {
    height: 70px;
    border-radius: 5px;
    justify-content: center;
    align-items: center;
    padding: 20px;
    background-color: #0f8cf0;
  }
	.text{
		font-size: 40px;
		text-align: center;
		align-items: center;
	}
  .btn-normal {
  	color:#000000;
  	margin-top: 10px;
    width: 650px;
    height: 100px;
    margin-left: 50px;
    background-color: #0f8cf0;
  }
  .btn-full {
  	color: #000000;
  	margin-top: 10px;
    width: 750px;
    height: 100px;
    background-color: #9bcdfa;
  }

  .btn:active {
    background-color: #9bcdfa;
  }
  .text{
  	font-size: 40px;
  	color: #000000;
  }
</style>