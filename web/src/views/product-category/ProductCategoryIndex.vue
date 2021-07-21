<template>
  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-10">
      <simple-card title="Product Categories">
        <template #content>
          <product-category-table :categories="product_categories" />
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import ProductCategoryTable from "../../components/product-category/ProductCategoryTable.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { ProductCategoryService } from "../../services/api";
export default {
  components: { SimpleCard, ProductCategoryTable },
  data() {
    return {
      product_categories: [],
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      ProductCategoryService.getAll().then(
        (categories) => (this.product_categories = categories.data)
      );
    },
  },
};
</script>

<style>
</style>