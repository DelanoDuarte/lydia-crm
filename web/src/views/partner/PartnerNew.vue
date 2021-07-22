<template>
  <div>
    <div class="row pb-3">
      <div class="col-md-6">
        <h4>New Partner</h4>
      </div>

      <div class="col-md-6">
        <button class="btn btn-success btn-lg float-end">Save Partner</button>
      </div>
    </div>
    <div class="row">
      <div class="col-md-8">
        <simple-card title="Basic Info">
          <template #content>
            <form class="row g-3">
              <div class="col-12">
                <label for="inputFirstName" class="form-label"
                  >First Name</label
                >
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputFirstName"
                />
              </div>
              <div class="col-12">
                <label for="inputLastName" class="form-label">Last Name</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputLastName"
                />
              </div>
            </form>
          </template>
        </simple-card>
      </div>
      <div class="col-md-4">
        <simple-card title="Address">
          <template #content>
            <form class="row g-3">
              <div class="col-12">
                <label for="inputAddress" class="form-label"
                  >Main Address</label
                >
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputAddress"
                  placeholder="1234 Main St"
                />
              </div>
              <div class="col-12">
                <label for="inputAddress2" class="form-label"
                  >Additional Address</label
                >
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputAddress2"
                  placeholder="Apartment, studio, or floor"
                />
              </div>
              <div class="col-md-3">
                <label for="inputCity" class="form-label">City</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputCity"
                />
              </div>
              <!-- <div class="col-md-4">
                <label for="inputState" class="form-label">State</label>
                <select id="inputState" class="form-select form-select-sm">
                  <option selected>Choose...</option>
                  <option>...</option>
                </select>
              </div> -->
              <div class="col-md-4">
                <label for="inputCountry" class="form-label">Country</label>
                <select id="inputCountry" class="form-select form-select-sm">
                  <option selected>Choose...</option>
                  <option>...</option>
                </select>
              </div>
              <div class="col-md-4">
                <label for="inputZip" class="form-label">Zip</label>
                <input
                  type="text"
                  class="form-control form-control-sm"
                  id="inputZip"
                />
              </div>
            </form>
          </template>
        </simple-card>
      </div>
    </div>
  </div>
</template>

<script>
import SimpleCard from "../../components/shared/SimpleCard.vue";
export default {
  components: { SimpleCard },
};
</script>

<style>
</style>