import Vue from 'vue'
import Router from 'vue-router'
import router from '../APP.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'router',
      component: router
    }
  ]
})
