<template>
  <div>
    <h2>Monitor</h2>
    <div class="grid grid-cols-2 gap-4">
      <Monitor v-for="camera in cameras" :key="camera.id + camera.name + camera.location" :cameraData="camera" />
    </div>
  </div>
</template>

<script>
  export default {
    computed: {
      cameras() {
        var cams = this.$store.state.camerasList
        return cams
      }
    },
    mounted() {
      // Check Alerts every 2 seconds
      var intervalId = setInterval(() => {
        this.$store.dispatch('fetchAlerts');
      }, 2000);
    }
  }

</script>

<style>

</style>
