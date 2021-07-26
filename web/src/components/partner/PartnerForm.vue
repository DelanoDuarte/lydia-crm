<template>
  <form>
    <div class="row">
      <div class="col-md-8">
        <simple-card title="Basic Info">
          <template #content>
            <div class="row g-3 p-2">
              <div class="col-6">
                <label for="inputFirstName" class="form-label"
                  >First Name</label
                >
                <input
                  required
                  type="text"
                  class="form-control form-control-sm"
                  v-model="partner.firstName"
                  id="inputFirstName"
                />
              </div>

              <div class="col-6">
                <label for="inputLastName" class="form-label">Last Name</label>
                <input
                  required
                  type="text"
                  class="form-control form-control-sm"
                  id="inputLastName"
                  v-model="partner.lastName"
                />
              </div>
            </div>
            <div class="row g-3 p-2">
              <div class="col-md-3">
                <label for="inputPartnerGender" class="form-label"
                  >Gender</label
                >
                <select
                  required
                  id="inputPartnerGender"
                  class="form-select form-select-sm"
                  v-model="partner.gender"
                >
                  <option
                    v-for="gender in genders"
                    :key="gender"
                    :value="gender"
                  >
                    {{ gender }}
                  </option>
                </select>
              </div>
              <div class="col-md-3">
                <label for="inputPartnerType" class="form-label"
                  >Partner Type</label
                >
                <select
                  required
                  id="inputPartnerType"
                  class="form-select form-select-sm"
                  v-model="partner.partnerType"
                >
                  <option :value="null" selected>Partner Types</option>
                  <option
                    v-for="pt in partnerTypes"
                    :key="pt.id"
                    :value="pt.id"
                  >
                    {{ pt.name }}
                  </option>
                </select>
              </div>
            </div>
            <div class="row g-3 p-2">
              <div class="col-4">
                <label for="inputBirthDate" class="form-label">BirthDate</label>
                <input
                  required
                  type="date"
                  class="form-control form-control-sm"
                  id="inputBirthDate"
                  v-model="partner.birthDate"
                />
              </div>

              <div class="col-8">
                <label for="inputEmail" class="form-label">Email</label>
                <input
                  required
                  type="email"
                  class="form-control form-control-sm"
                  id="inputEmail"
                  v-model="partner.email"
                />
              </div>
            </div>

            <div class="row g-3 p-2">
              <div class="col-4">
                <label for="inputPhoneNumber" class="form-label"
                  >Phone Number</label
                >
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputPhoneNumber"
                  v-model="partner.phone"
                />
              </div>

              <div class="col-4">
                <label for="inputMobile" class="form-label">Mobile</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputMobile"
                  v-model="partner.mobile"
                />
              </div>
            </div>

            <div class="row g-3 p-2">
              <div class="col-12">
                <label for="inputComments" class="form-label">Comments</label>
                <textarea
                  class="form-control form-control-sm"
                  id="inputComments"
                  v-model="partner.comments"
                />
              </div>
            </div>
          </template>
        </simple-card>
      </div>
      <div class="col-md-4">
        <simple-card title="Address">
          <template #content>
            <div class="col-12 g-3 p-2">
              <label for="inputAddress" class="form-label">Main Address</label>
              <input
                type="text"
                class="form-control form-control-sm"
                id="inputAddress"
                placeholder="1234 Main St"
                v-model="partner.address.mainAddress"
              />
            </div>
            <div class="col-12 g-3 p-2">
              <label for="inputAddress2" class="form-label"
                >Additional Address</label
              >
              <input
                type="text"
                class="form-control form-control-sm"
                id="inputAddress2"
                placeholder="Apartment, studio, or floor"
                v-model="partner.address.additionalAddress"
              />
            </div>
            <div class="row g-3 p-2">
              <div class="col-md-5">
                <label for="inputCity" class="form-label">City</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputCity"
                  v-model="partner.address.city"
                />
              </div>
              <div class="col-md-5">
                <label for="inputZip" class="form-label">Zip</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputZip"
                  v-model="partner.address.zip"
                />
              </div>
            </div>
            <div class="row g-3 p-2">
              <div class="col-md-5">
                <label for="inputState" class="form-label">State</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputState"
                  v-model="partner.address.state"
                />
              </div>
              <div class="col-md-5">
                <label for="inputCountry" class="form-label">Country</label>
                <select id="inputCountry" class="form-select form-select-sm">
                  <option selected>Choose...</option>
                  <option>...</option>
                </select>
              </div>
            </div>
          </template>
        </simple-card>
      </div>
    </div>
  </form>
</template>

<script>
import { PartnerService, PartnerTypeService } from "../../services/api";
import SimpleCard from "../shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
  data() {
    return {
      partnerTypes: [],
      genders: [],
      partner: {
        firstName: undefined,
        lastName: undefined,
        gender: undefined,
        birthDate: undefined,
        mobile: undefined,
        phone: undefined,
        email: undefined,
        comments: undefined,
        partnerType: undefined,
        address: {
          mainAddress: undefined,
          additionalAddress: undefined,
          city: undefined,
          state: undefined,
          zip: undefined,
        },
      },
    };
  },
  mounted() {
    this.load();
  },
  methods: {
    load() {
      PartnerTypeService.getAll().then(
        (response) => (this.partnerTypes = response.data)
      );
      PartnerService.genders().then((response) => {
        this.genders = response.data;
      });
    },
  },
};
</script>

<style>
</style>