<template>
  <simple-card title="Filters">
    <template #header>
      <div class="p-2">
        <div class="row g-3 p-2">
          <select
            id="categoriesSelect"
            class="form-control"
            aria-label="Default select example"
            @change="$emit('selected_category', $event.target.value)"
          >
            <option selected>Categories</option>
            <option
              v-for="category in categories"
              v-bind:key="category.id"
              v-bind:value="category.name"
            >
              {{ category.name }}
            </option>
          </select>
        </div>
      </div>
    </template>
  </simple-card>
</template>

<script>
import { ProductCategoryService } from "../../services/api";
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  data() {
    return {
      categories: [],
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      ProductCategoryService.getAll()
        .then((response) => (this.categories = response.data))
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>