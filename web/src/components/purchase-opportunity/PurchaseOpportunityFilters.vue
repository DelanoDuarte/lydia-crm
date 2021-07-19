<template>
  <div class="col-md-2">
    <simple-card>
      <template v-slot:header>
        <h4>Filters</h4>
        <div class="row p-2">
          <select
            id="purchaseOppsOptions"
            class="form-select"
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
          <button class="btn btn-success" type="button">
            Advanced Filters
          </button>
          <button
            class="btn btn-outline-danger"
            type="button"
            @click="$emit('clear-filters')"
          >
            Clear Filters
          </button>
        </div>
      </template>
    </simple-card>
  </div>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  props: {
    purchase_opportunity_status: {
      type: Array,
      default: [],
    },
  },
};
</script>

<style>
</style>