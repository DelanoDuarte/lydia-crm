import Vue from "vue";
import VueRouter from "vue-router";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faEllipsisV,
  faUserCircle,
  faPlus,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import { ModalPlugin, ToastPlugin } from "bootstrap-vue";
import Multiselect from "vue-multiselect";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "jquery/src/jquery.js";
import "offcanvas";
import "animate.css";

library.add(faUserCircle);
library.add(faEllipsisV);
library.add(faPlus);

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.component("multiselect", Multiselect);

Vue.use(VueRouter);
Vue.use(ModalPlugin);
Vue.use(ToastPlugin);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
