<template>
  <img class="imageicon" :src="addicon" v-on:click="collectpic"></img>
</template>
<script>
  export default{
    data(){
      return{
        addicon:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525927176928&di=26b196011f319c2aed8c72af8cd54536&imgtype=0&src=http%3A%2F%2Fpic.58pic.com%2F58pic%2F15%2F86%2F33%2F98C58PICtVg_1024.jpg",
      }
    },
    methods:{
      collectpic(){

      },
    }
  }
</script>
<style scoped="scoped">
  .imageicon{
    width: 200px; 
    height:200px; 
    margin-top:10px;
}
</style>
