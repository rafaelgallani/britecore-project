import Vue from "vue";
import App from "./App.vue";
import VueToastr from "vue-toastr";
import router from "./router";
import Loading from "vue-loading-overlay";

import "vue-loading-overlay/dist/vue-loading.css";
Vue.use(Loading, { 
  color: "#08859b",
  loader: "dots",
},{
  // slots
});

Vue.use(VueToastr, {
  /* OverWrite Plugin Options if you need */
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
  mounted(){
    this.$toastr.defaultClassNames = ["animated", "zoomInUp"];
    this.$toastr.defaultPosition = "toast-top-right";
  }
}).$mount("#app");
