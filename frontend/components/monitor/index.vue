<template>
  <div class="my-8 p-4 border rounded-md shadow-sm bg-grey-light">
    <div class="flex justify-between items-center mb-8">
      <h3>{{ cameraData.name }}</h3>
      <RadarSpinner :animation-duration="2000" :size="60" :color="spinnerColor" />
    </div>
    <client-only>
      <MonitorChart :key="lastChecked.format('ss')" :barChartData="barChartData" />
    </client-only>
    <p class="my-8">Updated at: {{lastChecked.format('DD-MMM-YYYY HH:mm:ss')}}</p>
    <div class="my-8">
      <div class="flex flex-row justify-start items-center mb-4">
        <h4>Alerts in the past 24 hours ({{alerts24hours.length}}) </h4>
        <p class="text-blue-500 underline cursor-pointer ml-4 button--green px-2 py-1" @click="toggleAlerts">{{showAlerts ? 'hide' :'show'}}</p>
      </div>
      <div class="max-h-80 overflow-y-scroll overflow-x-hidden">
      <MonitorAlert v-show="showAlerts" v-for="alert in alerts24hours" :key="alert.id" :alert="alert" />
      </div>
    </div>
  </div>
</template>

<script>
  import moment from 'moment';
  export default {
    data() {
      return {
        showAlerts: false,
        barChartData: {},
        spinnerColor: '#47d337'
      }
    },
    props: {
      cameraData: {
        type: Object,
        required: true
      },
    },
    computed: {
      alerts24hours() {
        let now = moment().format('x')
        let alerts = this.allAlerts.filter(al => {
          return (now - moment(al.timestamp).format('x')) <= 86400000
        });
        return alerts.reverse()
      },
      allAlerts() {
        let camAlerts = this.$store.state.alertsList.filter(a => a.cameraId == this.cameraData.id)
        return camAlerts
      },
      lastChecked() {
        var lastChecked = this.$store.getters.getLastChecked
        var last = moment(parseInt(lastChecked))
        return last
      },
    },
    methods: {
      toggleAlerts() {
        this.showAlerts = !this.showAlerts
      },
      timeOneHour() {
        let allAlerts = this.allAlerts
        var minsPerHour = 60;
        var data = [];
        var formattedTime;
        var alertsPerMin;
        for (let i = 0; i < minsPerHour + 1; i++) {
          formattedTime = (moment().subtract(i, "minutes")).format("HH:mm");
          alertsPerMin = allAlerts.filter(al => {
            return formattedTime === moment(al.timestamp).format('HH:mm')
          });
          data.unshift({
            'time': formattedTime,
            'alert': alertsPerMin.length > 1 ? 1 : 0
          });
        }
        return data
      },
      chartData() {
        let labels = this.timeOneHour().map(e => e['time'])
        let data = this.timeOneHour().map(e => e['alert'])
        this.spinnerColor = data[data.length - 1] ? '#dc2828' : '#47d337'
        var barChartData = {
          labels: labels,
          datasets: [{
              label: "No fire",
              data: data.map(e => e ^ 1),
              backgroundColor: "#47d337",
            },
            {
              label: "Fire",
              data: data,
              backgroundColor: "#dc2828",
            },
          ],
        }
        this.barChartData = barChartData
      },
    },
    mounted() {
      var interveralId = setInterval(() => {
        this.chartData()
      }, 5000)
    }
  }

</script>

<style>

</style>
