<template>
  <div class="card p-3 mb-3 bg-body rounded shadow">
    <h5 class="border-bottom p-2 mb-0">{{ title }}</h5>

    <slot name="header"></slot>
    <div class="card-content">
      <slot name="content"></slot>
    </div>

    <div class="p-2 border-top" v-if="$slots['footer']">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
  },
};
</script>

<style scoped>
.card {
  background-color: #fff;
  border: none;
}
.card-content {
  padding: 5px;
}
.card-foorter {
  padding: 2rem 2.25rem;
  background-color: #fff !important;
  border-top: 1px solid #ebedf3;
}
</style>