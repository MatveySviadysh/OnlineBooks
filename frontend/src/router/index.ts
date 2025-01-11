import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomePage from '@/components/common/HomePage.vue'
import LoginPage from '@/components/common/LoginPage.vue'
import RegisterPage from '@/components/common/RegisterPage.vue'
import AuthorsList from '@/components/common/AuthorsList.vue'
import ProfilePage from '@/components/common/ProfilePage.vue'
import AllBooks from '@/components/common/AllBooks.vue'
import ContactUs from '@/components/common/ContactUs.vue'


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },
  {
    path: '/authors',
    name: 'Authors',
    component: AuthorsList
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfilePage,
    meta: { requiresAuth: true }
  },
  {
    path: '/all_books',
    name: 'AllBooks',
    component: AllBooks,
    meta: { requiresAuth: true }
  },
  {
    path: '/contact_us',
    name: 'ContactUs',
    component: ContactUs,
    meta: { requiresAuth: true }
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
