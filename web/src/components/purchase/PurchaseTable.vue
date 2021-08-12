<template>
  <b-table striped hover :items="items" :fields="fields"></b-table>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      fields: ["Partner", ""],
    };
  },
};
</script>

<style>
</style>