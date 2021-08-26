<template>
  <div>
    <div class="row pb-2">
      <div class="col">
        <h4>New Purchase</h4>
      </div>
      <div class="col">
        <button class="btn btn-success float-right" @click.prevent="create()">
          Create Purchase
        </button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-2">
        <simple-card title="Actions">
          <template #content> </template>
        </simple-card>
      </div>
      <div class="col-md-10">
        <simple-card title="New Purchase">
          <template #content>
            <purchase-form />
          </template>
        </simple-card>

        <simple-card title="Products">
          <template #content>
            <simple-card v-for="(p, index) in products" :key="index">
              <template #content>
                <purchase-new-add-product
                  v-on:remove_product="removeProduct(index)"
                  v-on:search_product="searchProduct"
                  v-on:product_selected="onSelectProduct(index, $event)"
                />
              </template>
            </simple-card>
          </template>
          <template #footer>
            <button
              class="btn btn-success btn-sm float-right"
              @click.prevent="add"
            >
              Add
            </button>
          </template>
        </simple-card>
      </div>
    </div>
  </div>
</template>

<script>
import PurchaseForm from "../../components/purchase/PurchaseForm.vue";
import PurchaseNewAddProduct from "../../components/purchase/PurchaseNewAddProduct.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard, PurchaseForm, PurchaseNewAddProduct },
  data() {
    return {
      isProductLoading: false,
      product: {
        name: undefined,
        price: undefined,
      },
      products: [],
    };
  },
  methods: {
    create() {},
    add() {
      const product = {};
      this.products.push(product);
    },
    removeProduct(index) {
      const index_arr = this.products[index];
      if (index_arr) {
        this.products.splice(index, 1);
      }
    },
    onSelectProduct(index, product) {
      this.products[index] = product;
    },
  },
};
</script>

<style>
</style>