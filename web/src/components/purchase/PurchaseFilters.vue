<template>
  <div class="p-2">
    <div class="row g-3 p-2">
      <select
        id="purchaseStatus"
        class="form-control form-control-sm"
        aria-label="Default select example"
        @change="$emit('filter_selected', $event.target.value)"
      >
        <option selected>Status</option>
      </select>
    </div>
    <div class="row d-grid gap-2 p-2">
      <router-link
        class="btn btn-success btn-sm btn-block"
        :to="{ name: 'purchase-new' }"
        >New Purchase</router-link
      >
      <button class="btn btn-secondary btn-sm btn-block" type="button">
        Advanced Filters
      </button>
      <button
        class="btn btn-outline-danger btn-sm btn-block"
        type="button"
        @click="$emit('clear-filters')"
      >
        Clear Filters
      </button>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>