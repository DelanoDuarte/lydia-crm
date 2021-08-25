<template>
  <div>
    <div class="form-group row">
      <label for="product" class="col-sm-2 col-form-label">Name</label>
      <div class="col-sm-4">
        <multiselect
          v-model="selectedProduct"
          open-direction="bottom"
          :options="productOptions"
          placeholder="Select Product"
          label="name"
          track-by="id"
          :multiple="false"
          :searchable="true"
          :loading="isProductLoading"
          :internal-search="false"
          :clear-on-select="true"
          :close-on-select="true"
          :options-limit="10"
          :limit="3"
          @search-change="searchProduct"
        ></multiselect>
      </div>
    </div>

    <button
      class="btn btn-danger btn-sm"
      @click.prevent="$emit('remove_product', index)"
    >
      Remove
    </button>
  </div>
</template>

<script>
import { ProductService } from "../../services/api";
export default {
  props: { products: [] },
  data() {
    return {
      isProductLoading: false,
      productOptions: [],
      selectedProduct: {},
    };
  },
  methods: {
    searchProduct(query) {
      this.isProductLoading = true;
      ProductService.find(query)
        .then((response) => (this.productOptions = response.data))
        .then(() => (this.isProductLoading = false))
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>