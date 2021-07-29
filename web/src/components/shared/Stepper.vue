<template>
  <div class="text-center mt-3">
    <ul id="progressbar">
      <li
        id="account"
        v-for="step in steps"
        :key="step"
        v-bind:class="{ active: active_step === step }"
      >
        <strong>{{ step }} </strong>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  props: {
    steps: [],
    active_step: {
      type: String,
      default: "",
    },
  },
};
</script>

<style scoped>
.steper-content {
  position: relative;
}

#progressbar {
  overflow: hidden;
  color: lightgrey;
}

#progressbar .active {
  color: #000000;
}

#progressbar li {
  list-style-type: none;
  font-size: 12px;
  width: 15%;
  float: left;
  position: relative;
}

#progressbar #account:before {
  font-family: FontAwesome;
  content: "\f023";
}

#progressbar #personal:before {
  font-family: FontAwesome;
  content: "\f007";
}

#progressbar #payment:before {
  font-family: FontAwesome;
  content: "\f09d";
}

#progressbar #confirm:before {
  font-family: FontAwesome;
  content: "\f00c";
}

#progressbar li:before {
  width: 50px;
  height: 50px;
  line-height: 45px;
  display: block;
  font-size: 18px;
  color: #ffffff;
  background: lightgray;
  border-radius: 50%;
  margin: 0 auto 10px auto;
  padding: 2px;
}

#progressbar li:after {
  content: "";
  width: 100%;
  height: 2px;
  background: lightgray;
  position: absolute;
  left: 0;
  top: 25px;
  z-index: -1;
}

#progressbar li.active:before,
#progressbar li.active:after {
  background: skyblue;
}
</style>