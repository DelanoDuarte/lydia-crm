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
      <div class="col-md-8">
        <simple-card title="New Purchase">
          <template #content>
            <purchase-form ref="purchaseForm" />
          </template>
        </simple-card>

        <simple-card title="Products">
          <template #content>
            <simple-card v-for="(p, index) in products" :key="index">
              <template #content>
                <purchase-new-add-product
                  v-on:remove_product="removeProduct(index)"
                  v-on:product_selected="onSelectProduct(index, $event)"
                />
              </template>
            </simple-card>
          </template>
          <template #footer>
            <button
              type="button"
              @click.prevent="add"
              class="btn btn-outline-success btn-sm btn-block"
            >
              Add Item
            </button>
          </template>
        </simple-card>
      </div>

      <div class="col-md-4">
        <simple-card title="Purchase Total">
          <template #content>
            <div class="d-flex justify-content-between">
              <label
                class="text-sm font-semibold leading-5 text-gray-500 uppercase"
                >Sub Total</label
              >
              <label
                class="
                  flex
                  items-center
                  justify-center
                  m-0
                  text-lg text-black
                  uppercase
                "
                ><div>
                  <span style="font-family: sans-serif">€ </span> {{ subTotal }}
                </div></label
              >
            </div>

            <div class="d-flex justify-content-between">
              <label
                class="text-sm font-semibold leading-5 text-gray-500 uppercase"
                >Discount</label
              >
              <label
                class="
                  flex
                  items-center
                  justify-center
                  m-0
                  text-lg text-black
                  uppercase
                "
                ><div>
                  <input
                    type="number"
                    class="form-control form-control-sm"
                    id="discount"
                  /></div
              ></label>
            </div>
          </template>
          <template #footer>
            <div class="d-flex justify-content-between">
              <label
                class="
                  text-md
                  font-weight-bold
                  leading-5
                  text-gray-500 text-uppercase
                "
                >Total</label
              >
              <label
                class="
                  flex
                  items-center
                  justify-center
                  m-0
                  text-lg text-black
                  font-weight-bold
                "
                ><div>
                  <span style="font-family: sans-serif">€ </span> {{ total }}
                </div></label
              >
            </div>
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
import { PurchaseService } from "../../services/api";
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
      total: 0,
      subTotal: 0,
    };
  },
  computed: {},
  methods: {
    create() {
      const purchaseData = this.$refs.purchaseForm.purchase;
      const purchase = {
        partner: purchaseData.partner.id,
        purchaseDate: purchaseData.purchaseDate,
        products: this.products.map((p) => p.id),
        comments: purchaseData.comments,
        amount: this.total,
      };
      PurchaseService.create(purchase)
        .then(() => {
          this.$bvToast.toast("New Purchase sucessfully created.", {
            title: `Purchase`,
            variant: "success",
            solid: true,
          });
        })
        .then(() => this.$router.push({ name: "purchase-index" }))
        .catch((error) => console.log(error));
    },
    add() {
      const product = {};
      this.products.push(product);
    },
    removeProduct(index) {
      const product = this.products[index];
      if (product) {
        this.products.splice(index, 1);
        this.total -= product.unit_price;
        this.subTotal -= product.unit_price;
      }
    },
    onSelectProduct(index, product) {
      this.products[index] = product;
      this.total += product.unit_price;
      this.subTotal += product.unit_price;
    },
  },
};
</script>

<style>
</style>