<template>
  <form>
    <div class="form-row bt-1">
      <div class="form-group col-md-4">
        <label for="purchaseDate" class="font-weight-bold">Date</label>
        <input
          type="date"
          class="form-control"
          v-model="purchase.purchaseDate"
          id="purchaseDate"
        />
      </div>
      <div class="form-group col-md-4">
        <label for="partner" class="font-weight-bold">Partner</label>
        <multiselect
          v-model="purchase.partner"
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
        ></multiselect>
      </div>
    </div>
  </form>
</template>

<script>
import { PartnerService } from "../../services/api";
export default {
  data() {
    return {
      isPartnerSearchLoading: false,
      partners: [],
      purchase: {
        purchaseDate: undefined,
        products: [],
        partner: undefined,
        status: undefined,
      },
    };
  },

  methods: {
    searchPartner(query) {
      this.isPartnerSearchLoading = true;
      PartnerService.find(query)
        .then((response) => (this.partners = response.data))
        .then(() => (this.isPartnerSearchLoading = false))
        .catch((error) => console.error(error));
    },
  },
};
</script>

<style>
</style>