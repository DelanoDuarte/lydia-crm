<template>
  <simple-card title="Actions">
    <template #header>
      <div class="p-2">
        <div class="row g-3 p-2">
          <select
            id="purchaseOppsOptions"
            class="form-control"
            aria-label="Default select example"
            @change="$emit('filter-purchase-opportunity', $event.target.value)"
          >
            <option selected>Status</option>
            <option
              v-for="pos in purchase_opportunity_status"
              v-bind:key="pos"
              v-bind:value="pos"
            >
              {{ pos }}
            </option>
          </select>
        </div>
        <div class="row d-grid gap-2 p-2">
          <router-link
            class="btn btn-success btn-sm btn-block"
            :to="{ name: 'purchase-opportunity-create' }"
            >New Opportunity</router-link
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
  </simple-card>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  props: {
    purchase_opportunity_status: [],
  },
};
</script>

<style>
</style>