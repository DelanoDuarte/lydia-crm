<template>
  <div class="p-2">
    <div class="row g-3 p-2"></div>
    <div class="row d-grid gap-2 p-2">
      <router-link
        class="btn btn-success btn-sm btn-block"
        :to="{ name: 'payment-list' }"
        >New Payment</router-link
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