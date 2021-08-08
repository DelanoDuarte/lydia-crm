<template>
  <div class="row">
    <div class="col-md-2">
      <simple-card title="Filters"> </simple-card>
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
import SimpleCard from "../../components/shared/SimpleCard.vue";
import { ProductService } from "../../services/api";
export default {
  components: { SimpleCard, CardProductCatalog },
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