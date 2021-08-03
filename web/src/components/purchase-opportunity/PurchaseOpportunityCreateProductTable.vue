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
          <button
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

  watch: {},
};
</script>

<style>
</style>