<template>
  <div class="border p-3 rounded mb-3">
    <b>{{ messageObj.user.username }}</b>:
    <span>{{ messageObj.message }}</span>
  </div>
</template>

<script>
export default {
    name: 'ChatMessage',

    props: {
        messageObj : ''
    },
}
</script>

<style>

</style>