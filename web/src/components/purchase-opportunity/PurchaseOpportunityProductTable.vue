<template>
  <table class="table table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Price</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="product in products"
        v-bind:key="product.id"
        @dblclick="$emit('on-row-click', product.id)"
      >
        <td>
          {{ product.name }}
        </td>
        <td>€ {{ product.unit_price }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    products: {
      type: Array,
      default: [],
    },
  },
};
</script>

<style>
</style>