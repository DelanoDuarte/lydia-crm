<template>
  <simple-card title="Filters">
    <template #header>
      <div class="p-2">
        <div class="row g-3 p-2">
          <label for="categoriesSelect">Categories</label>
          <select
            id="categoriesSelect"
            class="form-control"
            aria-label="Default select example"
            @change="$emit('selected_category', $event.target.value)"
          >
            <option selected>Category</option>
            <option
              v-for="category in categories"
              v-bind:key="category.id"
              v-bind:value="category.name"
            >
              {{ category.name }}
            </option>
          </select>
        </div>

        <div class="row g-3 p-2">
          <label for="name">Name</label>
          <input id="name" type="text" class="form-control" />
        </div>

        <div class="row g-3 p-2">
          <label for="amount">Price Range</label>
          <div class="row">
            <div class="col">
              <div class="input-group mb-2">
                <div class="input-group-prepend">
                  <div class="input-group-text">From €</div>
                </div>
                <input
                  type="number"
                  class="form-control"
                  id="inlineFormInputGroup"
                  placeholder="3250"
                />
              </div>
            </div>
            <div class="col">
              <div class="input-group mb-2">
                <div class="input-group-prepend">
                  <div class="input-group-text">To €</div>
                </div>
                <input
                  type="number"
                  class="form-control"
                  id="inlineFormInputGroup"
                  placeholder="8500"
                />
              </div>
            </div>
          </div>
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