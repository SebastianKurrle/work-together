<template>
  <div class="mt-3 container">
    <h4 class="text-center">{{ org.name }}</h4>

    <div class="mb-3">
        <button type="button" class="btn btn-primary m-1" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            Options
        </button>

        <router-link class="btn btn-secondary" to="/organizations">Back</router-link>
    </div>
    
    <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="staticBackdropLabel">Options</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div>
                    <b>Organization Details:</b>
                    <p>
                        Name: {{ org.name }}
                        <br/>
                        Description: {{ org.description }}
                    </p>
                </div>
                <hr/>
                <div v-if="isOwner">
                    <button class="btn btn-success mb-3" data-bs-target="#createWorkspaceModal" data-bs-toggle="modal" data-bs-dismiss="modal">Create Workspace</button>
                    <br/>
                    <button class="btn btn-success" @click="getJoinRequests" data-bs-target="#joinRequests" data-bs-toggle="modal" data-bs-dismiss="modal">Join Requests</button>
                </div>
                <div v-else>
                    <button class="btn btn-danger" data-bs-dismiss="modal">Leave</button>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
        </div>
        </div>
    </div>

    <div class="modal fade" id="createWorkspaceModal" aria-hidden="true" aria-labelledby="exampleModalToggleLabel2" tabindex="-1">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="createWorkspaceModal">Create Workspace</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form @submit.prevent="workspaceSubmitForm">
                    <label for="name" class="form-label">Name:</label>
                    <input type="text" id="name" class="form-control" v-model="workspaceName">

                    <label for="desc" class="form-label">Description</label>
                    <input type="text" class="form-control" id="desc" v-model="workspaceDesc">
                    
                    <div class="bg-danger text-white p-3 mt-3 rounded" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>

                    <button class="btn btn-success mt-3">Create</button>
                </form>
            </div>
            <div class="modal-footer">
              <button class="btn btn-primary" data-bs-target="#staticBackdrop" data-bs-toggle="modal" data-bs-dismiss="modal">Back to options</button>
            </div>
          </div>
        </div>
    </div>

    <div class="modal fade" id="joinRequests" tabindex="-1" role="dialog" aria-labelledby="joinRequestsLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-scrollable" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="joinRequestsLabel">Join Requests</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div>
                    <div class="card mb-3" v-for="req in joinRequests" :key="req.join_request_id">
                        <div class="card-header">
                        Request From
                        </div>
                        <div class="card-body">
                            <h5 class="card-title">{{ req.user.username }}</h5>
                            <button class="btn btn-success m-1" @click="acceptJoinRequest(req.user.id, req.join_request_id)">Accept</button>
                            <button class="btn btn-danger" @click="denyJoinRequest(req.join_request_id)">Deny</button>
                        </div>
                    </div>
                </div>
            </div>
          </div>
        </div>
    </div>


    <div class="border p-3">
        <h5 class="text-center">Organization Workspaces</h5>

        <div class="container text-center mt-3">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3">
              <div class="card m-3" v-for="workspace in workspaces" :key="workspace.id">
                <div class="card-header">
                  {{ workspace.name }}
                </div>
                <div class="card-body">
                  <h5 class="card-title">Description</h5>
                  <p class="card-text">{{ workspace.description }}</p>
                  <router-link :to="workspace.get_absolute_url" class="btn btn-primary">Visit</router-link>
                </div>
              </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Toastify from 'toastify-js'

export default {
    name: 'OrgDetailView',

    data() {
        return {
            org: {},
            workspaces: [],
            isOwner: false,
            workspaceName: '',
            workspaceDesc: '',
            joinRequests: [],
            errors: []
        }
    },

    methods: {
        async getOrg() {
            const org_slug = this.$route.params.org_slug

            axios
                .get(`api/org/${org_slug}/`)
                .then(response => {
                    this.org = response.data.org
                    this.isOwner = response.data.is_owner
                    document.title = this.org.name + ' | WorkTogether'
                    this.getWorkspaces()
                })
                .catch(error => {
                    if (error.response.status === 403) {
                        Toastify({
                            text: "You don`t have permissons",
                            duration: 3000,
                            close: true,
                            gravity: "bottom",
                            position: "right",
                            stopOnFocus: true,

                            style: {
                                background: "red",
                            },
                        }).showToast();
                    } else {
                        Toastify({
                            text: "Something went wrong",
                            duration: 3000,
                            close: true,
                            gravity: "bottom",
                            position: "right",
                            stopOnFocus: true,

                            style: {
                                background: "red",
                            },
                        }).showToast();
                    }
                })
        },

        async workspaceSubmitForm() {
            this.errors = []

            const formData = {
                name: this.workspaceName,
                description: this.workspaceDesc,
                organization: this.org.id
            }

            await axios
                .post('/api/workspace/create/', formData)
                .then(response => {
                    if (response.data.error) {
                        this.errors.push(response.data.error)
                    } else {
                        Toastify({
                            text: "Workspace successfuly created",
                            duration: 3000,
                            close: true,
                            gravity: "bottom",
                            position: "right",
                            stopOnFocus: true,

                            style: {
                                background: "green",
                            },
                        }).showToast();

                    }
                })
                .catch(error => {
                    this.errors.push(error) 
                })
        },

        async getWorkspaces() {
            await axios
                .get(`/api/org/${this.org.id}/workspace/get/`)
                .then(response => {
                    this.workspaces = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },

        async getJoinRequests() {
            axios
                .get(`/api/org/owner/${this.org.id}/join-requests/`)
                .then(response => {
                    this.joinRequests = response.data
                })
                .catch(error => {
                    console.log(error)
                    Toastify({
                        text: error.data,
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
        },

        async acceptJoinRequest(userId, join_req_id) {
            const formData = {
                org: this.org.id,
                user: userId,
                join_req_id: join_req_id
            }

            axios
                .post('/api/org/owner/decide/join-request/', formData)
                .then(response => {
                    this.getJoinRequests()
                    Toastify({
                        text: 'Request Accepted',
                        duration: 3000,
                        close: true,
                        gravity: "bottom",
                        position: "right",
                        stopOnFocus: true,

                        style: {
                            background: "green",
                        },
                    }).showToast();
                })
                .catch(error => {
                    console.log(error)
                })
        },

        async denyJoinRequest(joinReqId) {
            axios
                .delete(`/api/org/user/delete-request/${joinReqId}/`)
                .then(response => {
                    this.getJoinRequests()
                    Toastify({
                        text: 'Denied join request',
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
        }
    },

    mounted() {
        this.getOrg()
    },
}
</script>
