<template>
  <div class="mt-3 container">
    <h4 class="text-center">{{ org.name }}</h4>

    <button type="button" class="btn btn-primary mb-3" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
        Options
    </button>
    
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
                <button class="btn btn-success" v-if="isOwner" data-bs-target="#createWorkspaceModal" data-bs-toggle="modal" data-bs-dismiss="modal">Create Workspace</button>
                <button class="btn btn-danger" v-else data-bs-dismiss="modal">Leave</button>
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
                <label for="name" class="form-label">Name:</label>
                <input type="text" id="name" class="form-control">

                <label for="desc" class="form-label">Description</label>
                <input type="text" class="form-control" id="desc">

                <button class="btn btn-success mt-3">Create</button>
            </div>
            <div class="modal-footer">
              <button class="btn btn-primary" data-bs-target="#staticBackdrop" data-bs-toggle="modal" data-bs-dismiss="modal">Back to options</button>
            </div>
          </div>
        </div>
    </div>

    <div class="border p-3">
        <h5 class="text-center">Organization Workspaces</h5>
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
            isOwner: false
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
                })
                .catch(error => {
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
                })
        }
    },

    mounted() {
        this.getOrg()
    },
}
</script>
