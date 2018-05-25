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
	//import myTree  from './tree.vue'
	const LOADMORE_COUNT = 4;
	export default{
		data(){//从服务器获取数据
			return{
				txtInput: '',
        txtChange: '',
        searchValue:"",
				lists:[
					{
						r_id:"机房1",
						r_name:"A",
						num:4,
						devices:[{
							d_id:1,
		          d_name:'机柜1',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://www.qianqigroup.com/Upload/product/max/SeverCabinet/19Inch19USeverCabinet11-18462028953.jpg'
       			},{
        			d_id:3,
		          d_name:'路由器',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://img2.imgtn.bdimg.com/it/u=3629577607,3477300825&fm=214&gp=0.jpg'
        		},
        		{
							d_id:1,
		          d_name:'机柜2',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://bmp.skxox.com/201606/23/xiaowai.153607.jpg'
       			},
        		{
	          d_id:2,
		          d_name:'塔式服务器',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://img1.imgtn.bdimg.com/it/u=1885317811,2314444115&fm=214&gp=0.jpg'
        		}]
					},

					{
						r_id:"机房2",
						r_name:"B",
						num:5,
						devices:[{
							d_id:1,
		          d_name:'路由器',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://pic.qiantucdn.com/58pic/11/01/52/72Q58PICATm.jpg'
	       		},{
	       			d_id:2,
		          d_name:'机架式服务器',
		          last_modified:"2018/05/08/15:51:00.17",
	       			d_pic:"http://img009.hc360.cn/m6/M00/40/14/wKhQolY6V3-ETfLbAAAAAN2HnuA805.jpg"
	       		},{
	          	d_id:3,
		          d_name:'路由器',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://pic.qiantucdn.com/58pic/15/68/75/98k58PICp5W_1024.jpg'
        		},{
							d_id:4,
		          d_name:'机柜1',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://www.qianqigroup.com/Upload/product/max/SeverCabinet/19Inch19USeverCabinet11-18462028953.jpg'
       			},{
							d_id:5,
		          d_name:'机柜2',
		          last_modified:"2018/05/08/15:51:00.17",
		          d_pic:'http://bmp.skxox.com/201606/23/xiaowai.153607.jpg'
       			},]
					},

				],
				refreshing:false,
			}
		},
		components:{
			Item,
			
		},
		methods:{
			fetch(e){
				this._data.loadmore = true;
				setTimeout(()=>{
					const length = this.lists.length;
					for(let i = length;i<length+LOADMORE_COUNT;i++){
						this.lists.push({r_id:i+1,r_name:"X",image:"image/1.jpg",placeholder:"测试"});
					}
					this._data.loadmore = false;},500)
		},
		onrefresh(e){
			this.refreshing = true;
			setTimeout(()=>{this.refreshing = false;},500);
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