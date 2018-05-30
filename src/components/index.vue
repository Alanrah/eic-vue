<template>
	<div>

		<header>
			<input type="text" placeholder="search" class="input" :autofocus=false value="" @change="onchange" @input="oninput"/>
		</header>

		<div class="panel" >
				<Item v-for="(item,index) in lists" :item="item" :key="index"></Item>
		</div>

		<div class="addroom" @click="roomInsert">
			添加新机房
		</div>

	</div>
</template>
<script>
	import Item from './item.vue'
	import qs from "qs"
	//import myTree  from './tree.vue'
	const LOADMORE_COUNT = 4;
	export default{
		data(){//从服务器获取数据
			return{
				user:this.$USER,
				txtInput: '',
        txtChange: '',
        searchValue:"",
				lists:null,
				refreshing:false,
			}
		},
		components:{
			Item,
			
		},
		created(){
				var self =this
				let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
          }
        let para ={"user":this.$USER.user}
				self.$axios.post('http://'+self.$IP+':5000/fetch', qs.stringify(para), config)
            .then(response => {
              let data = response.data;
							let deviceInfo=data[1];
							self.$USER.id =deviceInfo[0].u_id;

							let lists=data[0];
							for(let list of lists){
								list.devices=[];
								list.num=0;
								for(let device of deviceInfo){
									if(device.r_id == list.r_id){
										list.devices.push(device);
										list.num = list.num+1;
									}
								}
							}
							self.lists = lists;
            })
            .catch(function (error) {
                alert(error);
             })
		},
		methods:{
			fetchData(){
				var self =this
				let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            //withCredentials: true,
          }
        let para ={"user":this.$USER.user}
				self.$axios.post('http://'+self.$IP+':5000/fetch', qs.stringify(para), config)
            .then(response => {
              let data = response.data;
							let deviceInfo=data[1];
							self.$USER.id =deviceInfo[0].u_id;

							let lists=data[0];
							for(let list of lists){
								list.devices=[];
								list.num=0;
								for(let device of deviceInfo){
									if(device.r_id == list.r_id){
										list.devices.push(device);
										list.num = list.num+1;
									}
								}
							}
							self.lists = lists;
            })
            .catch(function (error) {
                alert(error);
             })
          },

		onpullingdown(e){
			console.log(" pulling down ");
		},
		onscoll(e){
			console.log("scrolling");
		},
		onchange: function (event) {
        this.txtChange = event.value;
        console.log('onchange', event.value);
      },
    oninput: function (event) {
      this.txtInput = event.value;
      console.log('oninput', event.value);
    },
    roomInsert:function(){alert("功能正在完善")}
	}
}
</script>
<style scoped="scoped">
	.list{
		height: 1030px;
		width: 740px;
	}
	.header{
		text-align: center;
		color: #000000;
		font-size: 40px;
		background-color: #B5F0E6;
	}
	.image{
		width: 710px;
		height: 250px;
		position: absolute;
		top: 32px;
		left: 14px;
	}
	.refresh{}
	.indicator{}
	.cell{}
	.panel{
		display: flex;
		width: 710px;
		margin-left: 16px;
		margin-top: 10px;
		margin-bottom: 20px;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		border-width: 2px;
		border-style: solid;
		border-color: rgb(162,217,192);
		border-color: rgba(162,217,192,0.2);

	}
	.text{
		font-size: 40px;
		text-align: center;
		color: #2E2E2E;
	}
	.cell{
		margin-top: 10px;
	}
	.input {
    font-size: 40px;
    height: 70px;
    width: 730px;
    margin-left: 10px;
    margin-top: 10px;
    margin-bottom: 5px;
    border-width: 2px;
		border-style: solid;
		border-color: rgb(162,217,192);
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #EDEBEB;
  }
  .addroom{
  	color: #2E2E2E;
		font-size: 40px;
    height: 50px;
    width: 400px;
    text-align: center;
    margin: auto;
		position: relative;
    border-width: 2px;
		border-style: solid;
		border-color: rgb(162,217,192);
		border-color: rgba(162,217,192,0.2);
		border-radius: 25px;
		background-color: #EDEBEB;
  }
</style>