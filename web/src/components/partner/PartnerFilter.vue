<template>
  <simple-card>
    <template v-slot:header>
      <h4>Filters</h4>
      <div class="row p-2">
        <select
          id="partnerTypeSelect"
          class="form-select"
          aria-label="Default select example"
          @change="$emit('filter-partner', $event.target.value)"
        >
          <option selected>Partner Type</option>
          <option
            v-for="pt in partnerTypes"
            v-bind:key="pt.id"
            v-bind:value="pt.id"
          >
            {{ pt.name }}
          </option>
        </select>
      </div>
      <div class="row d-grid gap-2 p-2">
        <button class="btn btn-success" type="button">Advanced Filters</button>
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
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  data() {
    return {};
  },
  props: {
    partnerTypes: {
      type: Array,
      default: [],
    },
  },
  methods: {
    onFilterChange(partner_type_id) {
      console.log(partner_type_id);
      this.$emit("filter-partner", partner_type_id);
    },
  },
};
</script>

<style>
</style>