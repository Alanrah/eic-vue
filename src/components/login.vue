<template>
  <div id="bg" class="bg">
  	<div class="signinpanel">
        <div class="row">
            <div class="col-sm-12">
                    <p class="m-t-md">欢迎登录设备信息采集系统</p>
                <div class="form-group">
                    <input type="email" class="form-control" placeholder="用户名" required="" v-model="userInfo.userName">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" placeholder="密码" required="" v-model="userInfo.password">
                </div>
                <button type="submit" class="btn btn-primary block full-width m-b" @click="doLogin">登 录</button>
                <p>测试账号：catherine 密码：123456</p>
<!--

                <p class="text-muted text-center"> <a href="login.html#"><small>忘记密码了？</small></a> | <a href="register.html">注册一个新账号</a>
                </p>
-->
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import Bus from '../bus.js'
import qs from "qs"
export default {
  data () {
    return {
      userInfo :{
          userName : '',
          password : '',
      },
      show : false,
    }
  },
  methods : {
      doLogin (){
          if (this.userInfo.userName == ''){
          	if (window.plus){plus.nativeUI.toast("用户名不能为空");}
              return false
          }
          if (this.userInfo.password == ''){
          	if (window.plus){plus.nativeUI.toast("密码名不能为空");}
              return false
          }
          if(this.userInfo.userName == 'catherine' && this.userInfo.password == '123456' ){
          	if (window.plus){plus.nativeUI.toast("密登陆成功");}
          	this.$router.push('index')
            console.log(this.$IP)
            this.$USER.user = this.userInfo.userName
            this.$USER.password = this.userInfo.password
            console.log(this.$USER)
            return true
          }

          
          this.$axios.post('/login',JSON.stringify(this.userInfo))
              .then(res => {
                  console.log(res)
                  if(res.status == 200){
                      this.$store.commit('setToken',res.data);
                      localStorage.userName = this.userInfo.userName;
                      localStorage.token_expire = res.data.expire;
                      localStorage.token = res.data.token;
                      this.$notify({
                          title : '提示信息',
                          message : '登录成功',
                          type : 'success'
                      });
                      this.$router.push('index')
                      this.$USER = this.userInfo.userName
                  }else {
                      this.$notify({
                          title : '提示信息',
                          message : '账号或密码错误',
                          type : 'error'
                      });
                  }
              })
              .catch(err => {
                  console.log(err)
              })
      }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="scoped">
  .bg {
  	 width: 750px;
  	 height: 1340px;
  	 position: fixed;
  	 left: 0;
  	 right: 0;
  	 top: 0;
  	 bottom: 0;
    background-color: aqua;
    background-image: url(../assets/bg.png);
    background-size:100% 100%;
     z-index: 11;
     font-size: 50px;
  }
  .signinpanel {
    width: 500px;
    margin: 10% auto 0 auto;
}

.signinpanel .logopanel {
    float: none;
    width: auto;
    padding: 0;
    background: none;
}

.signinpanel .signin-info ul {
    list-style: none;
    padding: 0;
    margin: 20px 0;
}

.signinpanel .form-control {
    display: block;
    margin-top: 15px;
    height: 60px;
}

.signinpanel .uname {
    background: #fff ;color:#333;
}

.signinpanel .pword {
    background: #fff ;color:#333;
}

.signinpanel .btn {
    margin-top: 15px;
}

.col-sm-12 {
		top: 150px;
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255,255,255,.3);
    -moz-box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    -webkit-box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    -moz-border-radius: 3px;
    -webkit-border-radius: 3px;
    border-radius: 3px;
    padding: 30px;
}
</style>