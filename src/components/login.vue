<template>
  <div id="bg" class="bg">
  	<div class="signinpanel">
            <div class="col-sm-12">
                    <p class="m-t-md">欢迎登录设备信息采集系统</p>
                <div class="form-group">
                    <input type="email" class="form-control" placeholder="用户名" required="" v-model="userInfo.userName">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" placeholder="密码" required="" v-model="userInfo.password">
                </div>
                <!--<label><input type="checkbox" v-model="checked" >一周内自动登录</label><br/>-->
                <button type="submit" class="btn" @click="submitForm">登 录</button>
                <p>测试账号：Catherine 密码：123456</p>

                <button  @click="register">注册一个新账号</button>

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
      checked:false,
  }
},
methods: {
    register(){
      this.$router.push('register')
    },
    submitForm() {
      var self=this;
        var name=self.userInfo.userName;
        var pass=self.userInfo.password;
        if(name==''||name==null){
          if (window.plus){plus.nativeUI.toast("请输入正确的用户名");}
          else alert("请输入正确的用户名")
          return
        }else if(pass==''||pass==null) {
          if (window.plus){plus.nativeUI.toast("密码名不能为空");}
          else alert("密码名不能为空")
          return
        }
        if(self.checked=true){
          self.setCookie(name,pass,7);
        }
        //接口
        let config = {
            headers: {'Content-Type':'application/x-www-form-urlencoded'},
          }
        let para ={"userName":self.userInfo.userName ,"password":self.userInfo.password}

        self.$axios.post('http://'+self.$IP+'/login', qs.stringify(para), config)
          .then(res => {
              if(res.status == 200 && res.data=='success'){
                  if (window.plus){plus.nativeUI.toast("登陆成功");}
                  self.$USER.user = self.userInfo.userName
                  self.$USER.password = self.userInfo.password
                  self.$router.push('index');
                  self.$USER.id = res.data;
                  Bus.$emit("changeindex","yes")
              }else {
                    if (window.plus){plus.nativeUI.toast("用户名或密码错误,请重新输入");}
                    else alert("用户名或密码错误,请重新输入");
                      self.userInfo.userName='';
                      self.userInfo.password='';
                      return
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
  setCookie(c_name,c_pwd,exdays) {
    var exdate=new Date();
    exdate.setTime(exdate.getTime() + 24*60*60*1000*exdays);
    window.document.cookie="userName"+ "=" +c_name+";path=/;expires="+exdate.toGMTString();
    window.document.cookie="userPwd"+"="+c_pwd+";path=/;expires="+exdate.toGMTString();
  },
  getCookie:function () {
    if (document.cookie.length>0) {
      var arr=document.cookie.split('; ');
      for(var i=0;i<arr.length;i++){
        var arr2=arr[i].split('=');
        if(arr2[0]=='userName'){
          this.userInfo.userName=arr2[1];
        }else if(arr2[0]=='userPwd'){
          this.userInfo.password=arr2[1];
        }
      }
    }
  },

  clearCookie:function () {
    this.setCookie("","",-1);//修改2值都为空，天数为负1天就好了
  }
},

mounted(){
        this.getCookie()
        }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped="scoped">
  .bg {
  	 width: 750px;
  	 height: 1440px;
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
    margin: 230px auto 0 auto;
    text-align: center;
}

.signinpanel .form-control {
    display: block;
    margin-top: 15px;
    margin-left: 40px;
    height: 60px;
}

.signinpanel .btn {
    margin-top: 15px;
}
.col-sm-12 {
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