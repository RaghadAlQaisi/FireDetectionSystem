<template>
  <div>
    <p class="text-red-600"><strong>Fire Alert at:</strong> {{dateTime}}</p>
  </div>
</template>

<script>
  import moment from 'moment';
  export default {
    props: {
      alert: {
        type: Object,
        required: true
      }
    },
    computed: {
      dateTime() {
        let ts = moment(this.alert.timestamp).format('ddd, DD-MMM-YYYY HH:mm:ss.SSSSSS')
        return ts
      },
      timestamp() {
        let ts = moment(this.alert.timestamp).format('x')
        return ts
      }
    }
  }

</script>

<style>

</style>
