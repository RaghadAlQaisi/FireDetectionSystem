import { Bar } from "vue-chartjs";
import Vue from 'vue'

Vue.component("BarChart", {
  extends: Bar,
  props: ["data", "options"],
  mounted() {
    this.renderChart(this.data, this.options);
  },
});
