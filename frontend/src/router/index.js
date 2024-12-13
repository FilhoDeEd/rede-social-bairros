import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/auth/Login.vue';
import Register from '../views/auth/Register.vue';
import Profile from '../views/Profile.vue';

import Landing from '@/views/Landing.vue';
import Admin from "@/layouts/Admin.vue";
import Auth from "@/layouts/Auth.vue";

// views for Admin layout
import Dashboard from "@/views/admin/Dashboard.vue";
import Settings from "@/views/admin/Settings.vue";
import Tables from "@/views/admin/Tables.vue";
import Maps from "@/views/admin/Maps.vue";

// views for main layout
import ForumPage from '@/views/ForumPage.vue';
import EventPage from '@/views/EventPage.vue';
import ReportPage from '@/views/ReportPage.vue';
import AboutPage from '@/views/AboutPage.vue';

const routes = [
  {
    path: "/admin",
    redirect: "/admin/dashboard",
    component: Admin,
    children: [
      {
        path: "/admin/dashboard",
        component: Dashboard,
      },
      {
        path: "/admin/settings",
        component: Settings,
      },
      {
        path: "/admin/tables",
        component: Tables,
      },
      {
        path: "/admin/maps",
        component: Maps,
      },
    ],
  },
  {
    path: "/auth",
    redirect: "/auth/login",
    component: Auth,
    children: [
      {
        path: "/auth/login",
        component: Login,
      },
      {
        path: "/auth/register",
        component: Register,
      },
    ],
  },
  {
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: Landing,
    name: 'home'
  },
  {
    path: '/forums',
    component: ForumPage,
    name: 'forums'
  },
  {
    path: '/events',
    component: EventPage,
    name: 'events'
  },
  {
    path: '/reports',
    component: ReportPage,
    name: 'reports'
  },
  {
    path: '/about',
    component: AboutPage,
    name: 'about'
  },
  {
    path: '/profile',
    component: Profile,
    name: 'profile'
  },
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
