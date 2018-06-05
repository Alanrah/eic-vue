<template>
	<div class="me">
		<div class="head">
			<uploadheadsculpture></uploadheadsculpture>
		</div>
		<div class="text"><div class="prefix">用户名:</div><div class="textword">{{name}}</div></div>
		<div class="text"><div class="prefix">ID:</div><div class="textword">{{ID}}</div> </div>
		<div class="text"><div class="prefix">简介:</div><div class="textword">{{introduction}}</div> </div>
		<div class="text"><div class="prefix">提醒:</div><div class="textword">{{hint}} </div></div>
		<div class="text"><div class="prefix">设置</div> </div>
		<div class="text"><div class="prefix">帮助与反馈</div> </div>
	</div>
</template>

<script>
 import uploadheadsculpture from './headsculpture.vue'
	export default{
		data(){
			return{
					name:this.$USER.user,
					ID:this.$USER.id,
					introduction:"啥也不留",
					hint:0,
					usericon:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525928989050&di=86f9e7f2efc098cf7e4f00949997c832&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fback_pic%2Fqk%2Fback_origin_pic%2F00%2F01%2F79%2F50c42a7c9c0c1ec2a219d5755af8af42.jpg",

			}
	},
	components:{
		uploadheadsculpture,
	}
	}
</script>
<style scoped="scoped">
	.me{
		height: 100%;
		overflow: hidden;
	}
	.text{
		color: #666666;
		display: flex;
		width: 740px;
		height: 80px;
		line-height: 80px;
		padding-left: 100px;
		padding-left: 40px;
		margin-top: 20px;
		border-width: 1px;
		border-style: solid;
		border-color: #A8A8A8;
		border-radius: 5px;
		flex-direction: row;
	}
	.head{
		display: flex;
		width: 740px;
		height: 300px;
		background-image: url('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525928989050&di=86f9e7f2efc098cf7e4f00949997c832&imgtype=0&src=http%3A%2F%2Fpic.90sjimg.com%2Fback_pic%2Fqk%2Fback_origin_pic%2F00%2F01%2F79%2F50c42a7c9c0c1ec2a219d5755af8af42.jpg');
		background-size:750px 300px;
		flex-direction: column;
		align-items: center;
	}
	.headsculpture{
		width: 200px;
		height: 200px;
		margin-top: 50px;
		background-image: url('http://h.hiphotos.baidu.com/zhidao/pic/item/cf1b9d16fdfaaf515c9a6f528a5494eef11f7ae6.jpg');
		background-size:200px 200px;
		border-width: 1px;
		border-style: solid;
		border-color: #A8A8A8;
		border-radius: 100px;
	}
	.textword{
		font-size: 40px;
	}
	.prefix{
		font-size: 40px;
		color: #666666;

	}
</style>