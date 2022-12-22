<template>
  <div class="home">
    <div class="mt-3">
      <h3 class="text-center">WorkTogether</h3>
    </div>

    <div class="container">
      <div class="border p-3 mt-3 mb-3">
        <h5>Welcome to WorkTogether</h5>
        <p>On this page you can create workspaces to have the best comunication for your projects</p>

        <p v-if="isAuthenticated === false">To start <router-link to="/login">Log In</router-link> or <router-link to="/register">Register</router-link></p>

        <div v-else>
          <h5>Options</h5>

          <router-link to="/organization/create">Create new organization</router-link>
          <br/>
          <router-link to="/organizations">Show my organizations</router-link>
          <br/>
          <router-link to="/join-requests">Join requests</router-link>
        </div>
      </div>

      <h5 class="text-center">Organization Overview</h5>

      <div v-if="isAuthenticated" class="border p-3">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
          <div class="card m-3" v-for="userOrg in userOrgs" :key="userOrg.id">
            <div class="card-header">
              {{ userOrg.org.name }}
            </div>
            <div class="card-body">
              <h5 class="card-title">Description</h5>
              <p class="card-text">{{ userOrg.org.description }}</p>
              <router-link :to="userOrg.org.get_absolute_url" class="btn btn-primary">Visit</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HomeView',

  data() {
    return {
      isAuthenticated: this.$store.state.isAuthenticated,
      userOrgs: []
    }
  },

  methods: {
    // get the orgs from the user where he is a member of
    async getUserOrgs() {
      axios.get('/api/org/user/')
            .then(response => {
              this.userOrgs = response.data
              console.log(this.userOrgs)
            })
            .catch(error => {
              console.log(error)
            })          
    }
  },

  mounted() {
    document.title = 'Home | WorkTogether'

    if (this.isAuthenticated) {
      this.getUserOrgs()
    }
  }
}
</script>
