<template>
  <div class="row">
    <div class="col-md-2">
      <partner-filter
        :partnerTypes="partner_types"
        v-on:filter-partner="filterPartners($event)"
        v-on:clear-filters="load()"
      />
    </div>
    <div class="col-md-10">
      <div class="row">
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Incoming" subTitle="1581"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Amount" subTitle="2358"> </card-status>
        </div>
        <div class="col-sm-6 col-md-6 col-lg-3">
          <card-status title="Something"> </card-status>
        </div>
      </div>

      <simple-card title="Partners">
        <template v-slot:content>
          <partner-table :partners="partners_data" />
        </template>
      </simple-card>
    </div>
  </div>
</template>

<script>
import { PartnerService, PartnerTypeService } from "../../services/api";
import CardStatus from "../../components/shared/CardStatus.vue";
import SimpleCard from "../../components/shared/SimpleCard.vue";
import PartnerTable from "../../components/partner/PartnerTable.vue";
import PartnerFilter from "../../components/partner/PartnerFilter.vue";
export default {
  components: { CardStatus, SimpleCard, PartnerTable, PartnerFilter },
  data() {
    return {
      partners_data: [],
      partner_types: [],
    };
  },
  mounted() {
    document.title = "Partner | Lydia";
  },

  created: function () {
    this.load();
  },

  methods: {
    load() {
      PartnerService.getAll().then((data) => (this.partners_data = data.data));
      PartnerTypeService.getAll().then(
        (data) => (this.partner_types = data.data)
      );
    },
    filterPartners(data) {
      PartnerService.allByPartnerType(data).then(
        (data) => (this.partners_data = data.data)
      );
    },
  },
};
</script>

<style>
</style>