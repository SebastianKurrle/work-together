import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'

import HomeView from '../views/HomeView.vue'
import RegisterView from '../views/RegisterView.vue'
import LoginView from '../views/LoginView.vue'
import AccountView from '../views/AccountView.vue'
import CreateOrgView from '../views/CreateOrgView.vue'
import OrgsView from '../views/OrgsView.vue'
import OrgDetailView from '../views/OrgDetailView.vue'
import WorkspaceDetailView from '../views/WorkspaceDetailView.vue'

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
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: 'login', query: { to: to.path }})
  } else {
    next()
  }
})

export default router
