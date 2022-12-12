// Other imports
import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

// Views importing

import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import AccountView from '../views/AccountView.vue'
import CreateOrgView from '../views/CreateOrgView.vue'
import OrgsView from '../views/OrgsView.vue'
import OrgDetailView from '../views/OrgDetailView.vue'
import WorkspaceDetailView from '../views/WorkspaceDetailView.vue'
import SearchView from '../views/SearchView.vue'
import JoinRequestsView from '../views/JoinRequestsView.vue'

// Routes for the Website
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },

  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/account',
    name: 'account',
    component: AccountView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/organization/create',
    name: 'org-create',
    component: CreateOrgView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/organizations',
    name: 'orgs',
    component: OrgsView,
    meta: {
      requireLogin: true
    },
  },
  {
    path: '/organization/:org_slug',
    name: 'org-detail',
    component: OrgDetailView,
    meta: {
      requireLogin: true
    },
  },
  {
    path: '/organization/:org_slug/:workspace_slug',
    name: 'workspace-detail',
    component: WorkspaceDetailView,
    meta: {
      requireLogin: true
    },
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView,
    meta: {
      requireLogin: true
    },
  },
  {
    path: '/join-requests',
    name: 'join-requests',
    component: JoinRequestsView,
    meta: {
      requireLogin: true
    },
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Checks witch route needs an login to continue
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: 'login', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
