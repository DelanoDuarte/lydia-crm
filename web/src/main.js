import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "jquery/src/jquery.js";
import "offcanvas";
import "animate.css";

Vue.config.productionTip = false;

Vue.use(VueRouter)

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
