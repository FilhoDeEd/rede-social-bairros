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
import ForumDetailPage from '@/views/ForumDetailPage.vue';

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
    redirect: '/auth/login'
  },
  {
    path: '/home',
    component: Landing,
    name: 'home',
    meta: { requiresAuth: true }
  },
  {
    path: '/forums',
    component: ForumPage,
    name: 'forums',
    meta: { requiresAuth: true }
  },
  {
    path: '/forums/:slug',
    component: ForumDetailPage,
    name: 'forum-detail',
    meta: { requiresAuth: true }
  },
  {
    path: '/events',
    component: EventPage,
    name: 'events',
    meta: { requiresAuth: true }
  },
  {
    path: '/reports',
    component: ReportPage,
    name: 'reports',
    meta: { requiresAuth: true }
  },
  {
    path: '/about',
    component: AboutPage,
    name: 'about',
    meta: { requiresAuth: true }
  },
  {
    path: '/profile',
    component: Profile,
    name: 'profile',
    meta: { requiresAuth: true }
  },
  { path: "/:pathMatch(.*)*", redirect: "/auth/login" },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('user.access') !== null;
  
  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/auth/login');
  } else if (to.path.startsWith('/auth') && isAuthenticated) {
    next('/home');
  } else {
    next();
  }
});

export default router;
