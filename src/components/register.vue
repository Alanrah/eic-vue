<template>
  <div id="bg" class="bg">
  	<div class="signinpanel">
            <div class="col-sm-12">
                    <p>注册</p>
                <div class="form-group">
                    <input type="email" class="form-control" placeholder="用户名" required="" v-model="userInfo.userName">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" placeholder="密码" required="" v-model="userInfo.password">
                </div>
                <div class="form-group">
                    <input type="tel" class="form-control" placeholder="电话" required="" v-model="userInfo.tel">
                </div>
                <div class="form-group">
                    <input type="email" class="form-control" placeholder="邮箱" required="" v-model="userInfo.email">
                </div>
                <button type="submit" class="btn btn-primary block full-width m-b" @click="submitForm">注册</button>
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
          tel:'',
          email:'',
      },
  }
},
methods: {
    submitForm() {
      var self=this;
        var name=self.userInfo.userName;
        var pass=self.userInfo.password;
        var email = self.userInfo.email;
        var tel =self.userInfo.tel;
        if(name==''||name==null){
          if (window.plus){plus.nativeUI.toast("请输入正确的用户名");}
          else alert("请输入正确的用户名")
          return
        }else if(pass==''||pass==null) {
          if (window.plus){plus.nativeUI.toast("密码名不能为空");}
          else alert("密码名不能为空")
          return
        }
        else if(email==''||email==null) {
          if (window.plus){plus.nativeUI.toast("邮箱不能为空");}
          else alert("邮箱不能为空")
          return
        }
        else if(tel==''||tel==null) {
          if (window.plus){plus.nativeUI.toast("电话不能为空");}
          else alert("电话不能为空")
          return
        }
        //接口
        let config = {
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
          }
        let para ={"userName":self.userInfo.userName ,"password":self.userInfo.password,"tel":self.userInfo.tel,"email":self.userInfo.email}

        self.$axios.post('http://'+self.$IP+'/register', qs.stringify(para), config)
          .then(res => {
              if(res.status == 200 && res.data=='exist'){
                  if (window.plus){plus.nativeUI.toast("该用户名已存在，请重新输入");}
                  else alert("该用户名已存在，请重新输入")
                    self.userInfo.userName='';
                    self.userInfo.password='';
                        return
              }else {
                    if (window.plus){plus.nativeUI.toast("注册成功，请登录");}
                    else alert("注册成功，请登录");
                    self.$router.push('login')
              }
          })
          .catch(err => {
              if (window.plus){plus.nativeUI.toast("登陆失败,请重新输入");}
                    else alert("登陆失败,请重新输入");
                      self.userInfo.userName='';
                      self.userInfo.password='';
                      return
          })

    },
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
    background-image: url(http://10.108.104.228:5000/static/devicePic/assets/bg.png);
    background-size:100% 100%;
     z-index: 11;
     font-size: 40px;
     color: #000000;
  }
  .signinpanel {
    width: 500px;
    margin: 10% auto 0 auto;
}


.signinpanel .form-control {
    display: block;
    margin-left: 40px;
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
		top: 350px;
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255,255,255,.3);
    -moz-box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    -webkit-box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    box-shadow: 0 3px 0 rgba(12, 12, 12, 0.03);
    -moz-border-radius: 3px;
    -webkit-border-radius: 3px;
    border-radius: 3px;
    padding: 30px;
    text-align: center;
}
</style>