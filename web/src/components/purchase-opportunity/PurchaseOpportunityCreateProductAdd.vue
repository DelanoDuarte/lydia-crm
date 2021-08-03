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
      <purchase-opportunity-create-product-table
        :products="products"
        @product_selected="addProduct($event)"
      />
    </div>
  </div>
</template>

<script>
import { ProductService } from "../../services/api";
import PurchaseOpportunityCreateProductTable from "./PurchaseOpportunityCreateProductTable.vue";
export default {
  components: {
    PurchaseOpportunityCreateProductTable,
  },
  data() {
    return {
      product: {
        name: "",
        type: {},
      },
      products: [],
      selectedProducts: [],
    };
  },

  methods: {
    queryProducts() {
      ProductService.find(this.product.name).then((response) => {
        const response_data = response.data;
        const productsOnStore = this.selectedProducts;
        if (response_data) {
          if (productsOnStore.length > 0) {
            this.products = this.products.filter(
              (el) => !productsOnStore.includes(el)
            );
          } else {
            this.products = response_data;
          }
        }
      });
    },

    addProduct(product) {
      this.$bvToast.toast("Product Added", {
        title: `Product`,
        variant: "success",
        solid: true,
      });
      this.products.splice(
        this.products.findIndex((p) => p.id === product.id),
        1
      );
      this.selectedProducts.push(product);
      this.$emit("products_changed", this.selectedProducts);
    },
  },
};
</script>

<style>
</style>