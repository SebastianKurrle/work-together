<template>
  <div class="container mt-3">
    <h4 class="text-center">Your Join Requests</h4>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'JoinRequestsView',

    data() {
        return {
            joinRequests: []
        }
    },

    methods: {
        async getJoinRequests() {
            axios
                .get('/api/org/user/join-request/')
                .then(response => {
                    this.joinRequests = response.data
                    console.log(response.data)
                })
        }
    },

    mounted() {
        this.getJoinRequests()
    },
}
</script>

<style>

</style>