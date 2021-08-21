import Vue from "vue";
import VueRouter from "vue-router";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faEllipsisV,
  faUserCircle,
  faPlus,
  faCheckCircle,
  faSearch,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

import {
  ModalPlugin,
  ToastPlugin,
  OverlayPlugin,
  CarouselPlugin,
  TablePlugin,
  PaginationPlugin,
} from "bootstrap-vue";
import Multiselect from "vue-multiselect";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import "bootstrap-vue/dist/bootstrap-vue.css";
import "jquery/src/jquery.js";
import "offcanvas";
import "animate.css";
import "vue-multiselect/dist/vue-multiselect.min.css";

library.add(faUserCircle);
library.add(faEllipsisV);
library.add(faPlus);
library.add(faCheckCircle);
library.add(faSearch);

Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.component("multiselect", Multiselect);

Vue.use(Vuex);
Vue.use(VueRouter);

Vue.use(ModalPlugin);
Vue.use(ToastPlugin);
Vue.use(OverlayPlugin);
Vue.use(CarouselPlugin);
Vue.use(TablePlugin);
Vue.use(PaginationPlugin);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
