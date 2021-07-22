<template>
  <div class="p-3 mb-3 bg-body rounded shadow">
    <slot name="header" class="header"></slot>
    <h5 class="border-bottom p-2 mb-0">{{ title }}</h5>
    <slot name="content" class="content mt-3"></slot>
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
.header {
  margin-bottom: 0;
  padding: 1.25rem 1.5rem;
  border-bottom: 1px solid rgba(0, 0, 0, 0.05);
}
.content {
  margin-bottom: 20px;
}
</style>