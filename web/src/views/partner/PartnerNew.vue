<template>
  <div>
    <div class="row pb-3">
      <div class="col-md-6">
        <h4>New Partner</h4>
      </div>

      <div class="col-md-6">
        <button @click="create()" class="btn btn-success btn-md float-right">
          Save Partner
        </button>
      </div>
    </div>
    <div class="col-md-12">
      <partner-form ref="partnerForm" />
    </div>
  </div>
</template>

<script>
import PartnerForm from "../../components/partner/PartnerForm.vue";
import { PartnerService, PartnerTypeService } from "../../services/api";
export default {
  components: { PartnerForm },
  data() {
    return {
      partnerTypes: [],
    };
  },
  mounted() {
    document.title = "Create | Partner";
  },
  methods: {
    load() {
      PartnerTypeService.getAll().then(
        (types) => (this.partnerTypes = types.data)
      );
    },

    create() {
      const partner = this.$refs.partnerForm.partner;
      PartnerService.create(partner).then(() => {
        console.log("Partner Created");
        this.$router.push({ name: "partner-list" });
      });
    },
  },
};
</script>

<style>
</style>