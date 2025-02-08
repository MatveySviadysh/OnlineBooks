import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AllBooks from '@/components/common/AllBooks.vue'
import AuthorDetail from '@/components/help/AuthorDetail.vue'
import AuthorsList from '@/components/common/AuthorsList.vue'
import BookDetail from '@/components/common/BookDetail.vue'
import BookListen from '@/components/common/BookListen.vue'
import BookReader from '@/components/common/BookReader.vue'
import ContactUs from '@/components/common/ContactUs.vue'
import HomePage from '@/components/common/HomePage.vue'
import LoginPage from '@/components/common/LoginPage.vue'
import MobileApp from '@/components/help/MobileApp.vue'
import News_Feed from '@/components/common/News_Feed.vue'
import ProfilePage from '@/components/common/ProfilePage.vue'
import Quotes_Book from '@/components/common/QuotationBook.vue'
import RegisterPage from '@/components/common/RegisterPage.vue'
import Storage from '@/components/common/Storge.vue'
import StoreLocator from '@/components/common/StoreLocator.vue'
import WriteComment from '@/components/common/WriteComment.vue'
import AllReadBooks from '@/components/common/AllReadBooks.vue'

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
  },
  {
    path: '/news/news_feed',
    name: 'News_Feed',
    component: News_Feed,
    meta: { requiresAuth: true }
  },
  {
    path: '/quotes/quotes_book',
    name: 'Quotes_Book',
    component: Quotes_Book,
    meta: { requiresAuth: true }
  },
  {
    path: '/comments/write_comments',
    name: 'WriteComment',
    component: WriteComment,
    meta: { requiresAuth: true }
  },
  {
    path: '/book/:id',
    name: 'BookDetail',
    component: BookDetail,
    props: true,
  },
  {
    path: '/book/read/:id',
    name: 'BookReader',
    component: BookReader,
    props: true,
  },
  {
    path: '/book/listen/:id',
    name: 'BookListen',
    component: BookListen,
    props: true,
  },
  {
    path: '/account/storege',
    name: 'Storage',
    component: Storage,
  },
  {
    path: '/store-locator',
    name: 'StoreLocator',
    component:StoreLocator,
  },
  {
    path: '/mobile-app',
    name: 'MobileApp',
    component:MobileApp
  },
  {
    path: '/authors/details/:id',
    name: 'AuthorDetail',
    component: AuthorDetail,
    props: true,
  },
  {
    path: '/book/read',
    name: 'AllReadBooks',
    component: AllReadBooks 
  }
]


const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
