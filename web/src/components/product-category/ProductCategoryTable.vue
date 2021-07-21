<template>
  <table class="table table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Active</th>
      </tr>
    </thead>
    <tbody>
      <tr
        class="table-row"
        v-for="categorie in categories"
        v-bind:key="categorie.id"
        @dblclick="$emit('on-row-selected', categorie.id)"
      >
        <td>{{ categorie.name }}</td>
        <td>
          <div class="form-check form-switch">
            <input
              v-if="categorie.active === true"
              class="form-check-input"
              type="checkbox"
              checked
              disabled
            />
            <input v-else class="form-check-input" type="checkbox" disabled />
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    categories: {
      type: Array,
      default: [],
    },
  },
};
</script>

<style>
</style>