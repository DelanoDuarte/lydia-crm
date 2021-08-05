<template>
  <simple-card title="Actions">
    <template #header>
      <div class="row p-2">
        <select
          id="partnerTypeSelect"
          class="form-control"
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
        <router-link
          class="btn btn-success btn-sm btn-block"
          :to="{ name: 'partner-create' }"
          >New Partner</router-link
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
    </template>
  </simple-card>
</template>

<script>
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  props: {
    partnerTypes: [],
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