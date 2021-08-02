<template>
  <div class="p-2">
    <div class="pb-2">
      <form @submit.prevent="queryProducts()">
        <div class="form-row gap-3">
          <div class="col-md-8 p-2">
            <label for="productName">Name</label>
            <input
              id="productName"
              type="text"
              class="form-control"
              placeholder="Residence 00001"
              min="3"
              v-model="product.name"
            />
            <small
              id="productNameHelp"
              class="form-text text-muted"
              v-if="product.name.length < 3"
              >Type at lest 3 characteres.</small
            >
          </div>
        </div>
        <div class="pb-2 float-right">
          <button type="submit" class="btn btn-success btn-sm mr-1">
            Search
          </button>
          <button type="reset" class="btn btn-warning btn-sm">Clear</button>
        </div>
      </form>
    </div>
    <div class="pb-2">
      <purchase-opportunity-product-table :products="products" />
    </div>
  </div>
</template>

<script>
import { ProductService } from "../../services/api";
import PurchaseOpportunityProductTable from "./PurchaseOpportunityProductTable.vue";
export default {
  components: { PurchaseOpportunityProductTable },
  data() {
    return {
      product: {
        name: "",
        type: Object,
      },
      products: [],
    };
  },

  methods: {
    queryProducts() {
      ProductService.find(this.product.name).then(
        (response) => (this.products = response.data)
      );
    },
  },
};
</script>

<style>
</style>