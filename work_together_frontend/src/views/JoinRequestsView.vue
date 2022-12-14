<template>
  <div class="container mt-3">
    <h4 class="text-center">Your Join Requests</h4>

    <div>
        <div class="card mb-3" v-for="req in joinRequests" :key="req.join_request_id">
            <div class="card-header">
            Request To
            </div>
            <div class="card-body">
                <h5 class="card-title">{{ req.org.name }}</h5>
                <p class="card-text">{{ req.org.description }}</p>
                <button class="btn btn-danger" @click="deleteJoinRequest(req.join_request_id)">Delete Request</button>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Toastify from "toastify-js";

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
                })
        },

        async deleteJoinRequest(req_id) {
            axios
                .delete(`/api/org/user/delete-request/${req_id}/`)
                .then(response => {
                    this.getJoinRequests()

                    Toastify({
                        text: "Join request has been deleted",
                        duration: 3000,
                        close: true,
                        gravity: "bottom",
                        position: "right",
                        stopOnFocus: true,

                        style: {
                            background: "red",
                        },
                    }).showToast();
                })
                .catch(error => {
                    console.log(error)
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