<template>
  <table class="table table-bordered table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Price</th>
        <th scope="col"></th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="product in products"
        v-bind:key="product.id"
        @dblclick="$emit('on_row_click', product.id)"
      >
        <td>
          {{ product.name }}
        </td>
        <td class="font-weight-bold">€ {{ product.unit_price }}</td>
        <td>
          <font-awesome-icon
            v-if="isAlreadyOnStore(product)"
            icon="check-circle"
            size="2x"
            :style="{ color: 'green' }"
          />

          <button
            v-else
            class="btn btn-success btn-sm"
            @click="$emit('product_selected', product)"
          >
            Add
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    products: [],
  },
  methods: {
    isAlreadyOnStore(product) {
      const productsOnStore = this.$store.state.product.products;
      if (productsOnStore && productsOnStore.length > 0) {
        return productsOnStore.some((p) => p.id === product.id);
      }
      return false;
    },
  },
};
</script>

<style>
</style>