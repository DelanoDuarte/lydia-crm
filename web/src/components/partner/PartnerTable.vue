<template>
  <table class="table table-hover">
    <thead class="text-secondary">
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Gender</th>
        <th scope="col">Email</th>
        <th scope="col">BirthDate</th>
        <th scope="col">Partner Type</th>
      </tr>
    </thead>
    <tbody>
      <tr
        class="table-row"
        v-for="partner in partners"
        v-bind:key="partner.id"
        @dblclick="$emit('on-row-selected', partner.id)"
      >
        <td>{{ partner.full_name }}</td>
        <td>
          <span class="badge rounded-pill bg-info">
            {{ partner.gender }}
          </span>
        </td>
        <td>{{ partner.email }}</td>
        <td v-if="partner.birthDate">{{ partner.birthDate }}</td>
        <td v-else>*Not Provided</td>
        <td>
          <span class="badge rounded-pill bg-success">
            {{ partner.partnerType.name }}
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    partners: {
      type: Array,
      default: [],
    },
    methods: {},
  },
};
</script>

<style scoped>
.table-row {
  cursor: pointer;
}
</style>