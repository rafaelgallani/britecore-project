import Vue from "vue";
import App from "./App.vue";
import VueToastr from "vue-toastr";
import router from "./router";

Vue.use(VueToastr, {
  /* OverWrite Plugin Options if you need */
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
  mounted(){
    this.$toastr.defaultClassNames = ["animated", "zoomInUp"];
    // Change Toast Position
    this.$toastr.defaultPosition = "toast-top-right";
    // Send message to browser screen
    this.$toastr.s(
      "This Message From Toastr Plugin\n You can access this plugin : <font color='yellow'>this.$toastr</font>"
    );
  }
}).$mount("#app");
