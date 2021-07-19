import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "bootstrap/dist/css/bootstrap.min.css";

import "jquery/src/jquery.js";
import "bootstrap/dist/js/bootstrap.min.js";
import "offcanvas";

import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faUserCircle, faUser } from "@fortawesome/free-regular-svg-icons";
import { library } from "@fortawesome/fontawesome-svg-core";

library.add(faUserCircle);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(router)
  .mount("#app");
