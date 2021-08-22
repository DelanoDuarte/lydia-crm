<template>
  <form>
    <div class="form-row bt-1">
      <div class="form-group col-md-4">
        <label for="paymentDate" class="font-weight-bold">Date</label>
        <input
          type="date"
          class="form-control"
          v-model="payment.paymentDate"
          id="paymentDate"
        />
      </div>
      <div class="form-group col-md-4">
        <label for="paymentNumber" class="font-weight-bold"
          >Payment Number</label
        >
        <input
          type="text"
          class="form-control"
          v-model="payment.paymentNumber"
          id="paymentNumber"
        />
      </div>
    </div>

    <div class="form-row bt-1">
      <div class="form-group col-md-4">
        <label for="paymentPartner" class="font-weight-bold">Partner</label>
        <multiselect
          v-model="payment.partner"
          open-direction="bottom"
          :options="partners"
          :custom-label="partnerName"
          placeholder="Select Partner"
          label="full_name"
          track-by="id"
          :multiple="false"
          :searchable="true"
          :loading="isPartnerSearchLoading"
          :internal-search="false"
          :clear-on-select="true"
          :close-on-select="true"
          :options-limit="10"
          :limit="3"
          @search-change="searchPartner"
          @select="onSelectPartner"
        ></multiselect>
      </div>
      <div class="form-group col-md-4">
        <label for="paymentPurchase" class="font-weight-bold">Purchase</label>
        <multiselect
          v-model="payment.purchase"
          open-direction="bottom"
          :options="purchases"
          :custom-label="purchaseLabel"
          placeholder="Select Purchase"
          track-by="id"
          :multiple="false"
          :searchable="true"
          :disabled="isPurchaseSelectDisabled"
          :loading="isPurchaseSearchLoading"
          :internal-search="false"
          :clear-on-select="true"
          :close-on-select="true"
          :options-limit="10"
          :limit="3"
        >
          <template slot="singleLabel" slot-scope="props"
            ><span class="option__desc"
              ><span class="option__title"
                >{{ props.option.partner.full_name }} -
                {{ props.option.purchaseDate }}
              </span>
              <span class="option__small">
                ( € {{ props.option.amount }} )
              </span>
            </span></template
          >

          <template slot="option" slot-scope="props">
            <div class="option__desc">
              <span class="option__title"
                >{{ props.option.partner.full_name }} -
                {{ props.option.purchaseDate }}
              </span>
              <span class="option__small">
                ( € {{ props.option.amount }} )
              </span>
            </div>
          </template>
        </multiselect>
      </div>
    </div>

    <div class="form-row bt-1">
      <div class="form-group col-md-4">
        <label for="paymentAmount" class="font-weight-bold">Amount</label>
        <input
          type="number"
          class="form-control"
          v-model="payment.amount"
          id="paymentAmount"
        />
      </div>
      <div class="form-group col-md-4">
        <label for="paymentMode" class="font-weight-bold">Payment Mode</label>
        <multiselect
          v-model="payment.mode"
          open-direction="bottom"
          :options="paymentModes"
          :custom-label="paymentModelLabel"
          placeholder="Select Payment Mode"
          track-by="id"
          :multiple="false"
          :searchable="true"
          :internal-search="true"
          :clear-on-select="true"
          :close-on-select="true"
        >
        </multiselect>
      </div>
    </div>
  </form>
</template>

<script>
import {
  PartnerService,
  PaymentModeService,
  PurchaseService,
} from "../../services/api";
export default {
  data() {
    return {
      partners: [],
      purchases: [],
      paymentModes: [],
      isPartnerSearchLoading: false,
      isPurchaseSearchLoading: false,
      isPurchaseSelectDisabled: true,
      payment: {
        paymentNumber: undefined,
        paymentDate: undefined,
        partner: undefined,
        purchase: undefined,
        mode: undefined,
        amount: undefined,
      },
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      PaymentModeService.all()
        .then((response) => (this.paymentModes = response.data))
        .catch((error) => console.log(error));
    },

    partnerName({ full_name }) {
      if (full_name) {
        return `${full_name}`;
      }
    },
    purchaseLabel({ status, purchaseDate, partner }) {
      if (status) {
        return `${status} - (${purchaseDate}) - ${partner.full_name}`;
      }
    },

    paymentModelLabel({ name }) {
      return `${name}`;
    },

    searchPartner(query) {
      this.isPartnerSearchLoading = true;
      PartnerService.find(query)
        .then((response) => (this.partners = response.data))
        .then(() => (this.isPartnerSearchLoading = false))
        .catch((error) => console.error(error));
    },

    /** Get the Purchases of the Partner */
    onSelectPartner(partner) {
      this.purchases = [];
      if (partner) {
        this.isPurchaseSelectDisabled = false;
        PurchaseService.allByPartner(partner.id)
          .then((response) => (this.purchases = response.data))
          .then((error) => console.log(error));
      }
    },
  },
};
</script>

<style>
</style>