<template>
  <div class="home">
    <div class="mt-3">
      <h3 class="text-center">WorkTogether</h3>
    </div>

    <div class="container border p-3 mt-3">
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
  </div>
</template>

<script>
export default {
  name: 'HomeView',

  data() {
    return {
      isAuthenticated: this.$store.state.isAuthenticated
    }
  },

  mounted() {
    document.title = 'Home | WorkTogether'
  }
}
</script>
