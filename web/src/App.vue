<template>
  <div>
    <nav-bar />
    <main class="container-fluid">
      <div class="content">
        <router-view class="animate__animated animate__fadeIn" />
      </div>
    </main>
  </div>
</template>

<script>
import NavBar from "@/components/navigation/NavBar.vue";
export default {
  components: { NavBar },
  mounted() {
    document.title = "Home | Lydia";
    document
      .querySelector("body")
      .setAttribute("style", "background-color:#f4f3ef");
  },
};
</script>

<style>
body {
  background-color: #f4f3ef;
  color: #2c2c2c;
  font-size: 14px !important;
  font-family: "Montserrat", "Helvetica Neue", Arial, sans-serif;
}
.content {
  padding-top: 90px;
}

footer {
  background-color: #fff !important;
}

.table {
  border-spacing: 2px;
  border-color: gray !important;
}

.form-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: #525f7f;
}

label {
  display: inline-block;
  margin-bottom: 0.5rem;
}

.modal-backdrop {
  opacity: 0.5 !important;
}
</style>
