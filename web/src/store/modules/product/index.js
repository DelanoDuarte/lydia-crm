export const productModule = {
  namespaced: true,
  state: () => ({
    products: [],
  }),
  mutations: {
    add(state, product) {
      state.products.push(product);
    },
  },
  actions: {},
};
