export const productModule = {
  namespaced: true,
  state: () => ({
    products: [],
  }),
  mutations: {
    add(state, product) {
      state.products.push(product);
    },
    clear(state) {
      state.products = [];
    },
  },
  actions: {},
};
