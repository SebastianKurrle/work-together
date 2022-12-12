<template>
  <div class="container mt-3">
    <div class="text-center mb-3">
        <h4>Your search term: {{ query }}</h4>
        <h5>Results</h5>
    </div>

    <div>
        <div class="card mb-3" v-for="org in orgs" :key="org.id">
            <div class="card-header">
            Founded Organization
            </div>
            <div class="card-body">
            <h5 class="card-title">{{ org.name }}</h5>
            <p class="card-text">{{ org.description }}</p>
            <button class="btn btn-primary" @click="makeJoinRequest(org.id)">Beitritt anfragen</button>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Toastify from "toastify-js";

export default {
    name: 'SearchView',

    data() {
        return {
            orgs: [],
            query: ''
        }
    },

    methods: {
        async performSearch() {
            await axios
                .post('/api/org/search/', {'query' : this.query})
                .then(response => {
                    this.orgs = response.data
                    //console.log(this.orgs)
                })
                .catch(error => {
                    console.log(error);
                })
        },

        async makeJoinRequest(orgId) {
            const formData = {
                org: orgId,
                user: localStorage.getItem('userId')
            }

            axios
                .post('/api/org/join-request/', formData)
                .then(response => {
                    console.log(response)
                    Toastify({
                        text: "Join request has been sendet",
                        duration: 3000,
                        close: true,
                        gravity: "bottom",
                        position: "right",
                        stopOnFocus: true,

                        style: {
                            background: "green",
                        },
                    }).showToast();
                    this.performSearch()
                })
                .catch(error => {
                    console.log(error)
                })
            
        }
    },

    mounted() {
        document.title = 'WorkTogehter | Search'

        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')

            this.performSearch()
        }
    },
}
</script>

<style>

</style>