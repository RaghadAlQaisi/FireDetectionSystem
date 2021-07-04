<template>
  <div>
    <h2>Cameras Configuration</h2>
    <Camera v-for="camera in cameras" :key="camera.id + camera.name + camera.location" :cameraData="camera" class="my-8 p-4 rounded-md shadow-md bg-grey-light"/>
    <CameraAdd class="my-8"/>
  </div>
</template>

<script>
  export default {
    computed: {
      cameras() {
        return this.$store.getters.getCameras
      }
    }
  }

</script>

<style>

</style>
