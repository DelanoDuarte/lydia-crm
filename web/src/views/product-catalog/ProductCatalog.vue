<template>
  <div class="row">
    <div class="col-md-2">
      <product-catalog-filters> </product-catalog-filters>
    </div>

    <div class="col-md-10">
      <simple-card title="Product Catalog">
        <template #content>
          <div class="row p-2">
            <div
              class="col-md-4"
              v-for="product in products"
              v-bind:key="product.id"
            >
              <card-product-catalog
                :images="product.images"
                :title="product.name"
                :price="product.unit_price"
                :category="product.product_category.name"
              >
              </card-product-catalog>
            </div>
          </div>
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import CardProductCatalog from "../../components/product/CardProductCatalog.vue";
import ProductCatalogFilters from "../../components/product/ProductCatalogFilters.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { ProductService } from "../../services/api";
export default {
  components: { SimpleCard, CardProductCatalog, ProductCatalogFilters },
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      ProductService.all()
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>

<style>
</style>