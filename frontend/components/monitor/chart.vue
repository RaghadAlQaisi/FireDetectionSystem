<template>
  <section>
    <div class="chart">
      <BarChart :data="barChartData" :options="barChartOptions" :height="50" />
    </div>
  </section>
</template>

<script>
  export default {
    props: {
      barChartData: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        barChartOptions: {
          animation: false,
          responsive: true,
          legend: {
            display: false,
          },
          title: {
            display: false,
          },
          tooltips: {
            backgroundColor: "#2e3436",
          },
          scales: {
            xAxes: [{
              gridLines: {
                display: false,
              },
            }, ],
            yAxes: [{
              display: false,
              ticks: {
                beginAtZero: true,
                max: 1,
                min: 0,
                stepSize: 1,
              },
              gridLines: {
                display: false,
              },
            }, ],
          },
        },
      };
    },
  };

</script>
