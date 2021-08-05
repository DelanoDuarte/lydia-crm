import Vue from "vue";
import Vuex from "vuex";

import { productModule } from "./modules/product";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    product: productModule,
  },
});
