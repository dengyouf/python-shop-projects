import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/Login.vue'
import '../assets/css/global.css'
import Home from '../components/Home.vue'
import Welcome from '../components/Welcome.vue'
import User from '../components/user/User.vue'
import Menu from '../components/power/Menu.vue'
import Role from '../components/power/Role.vue'
import Cate from '../components/goods/Cate.vue'
import Attr from '../components/goods/Attribute.vue'
import Goods from '../components/goods/Goods.vue'
import Add from '../components/goods/Add.vue'
import Order from '../components/order/Order.vue'
import Data from '../components/data/Data.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    component: Login
  },
  {
    path: '/home',
    component: Home,
    redirect: '/welcome',
    children: [
      { path: '/welcome', component: Welcome },
      { path: '/user_list', component: User },
      { path: '/menu_list', component: Menu },
      { path: '/role_list', component: Role },
      { path: '/cate_list', component: Cate },
      { path: '/attr_list', component: Attr },
      { path: '/goods_list', component: Goods },
      { path: '/add_goods', component: Add },
      { path: '/order_list', component: Order },
      { path: '/data_list', component: Data }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router

router.beforeEach((to, from, next) => {
  if (to.path === '/login') return next()
  const tokenStr = window.sessionStorage.getItem('token')
  if (!tokenStr) return next('/login')
  next()
})
