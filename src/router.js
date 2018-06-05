import Vue from 'vue'
/*global Vue*/
import Router from 'vue-router'

//导入组件
import index from './components/index.vue'
import add from './components/add.vue'
import me from './components/me.vue'
import login from './components/login.vue'
import register from './components/register.vue'

//让vue使用vuerouter当做自己的路由
//
Vue.use(Router)
//创建一个路由对象并且输出
export default new Router({
  routes: [
  {
    path:'/register',
    name:'register',
    component:register
  },
  {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/index',
      name: '机房信息',
      component: index
    },
    {
      path: '/add',
      name: '采集信息',
      component: add
    },
    {
      path: '/me',
      name: '我的',
      component: me
    }
  ]
})
