<template>
  <div class="card mb-4">
    <div class="img-container">
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        background="#ababab"
        style="text-shadow: 1px 1px 2px #333"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <!-- Slides with image only -->

        <b-carousel-slide v-for="image in images" :key="image.id">
          <template #img>
            <img
              class="d-block w-100"
              height="300"
              :src="image.image_url"
              alt="image slot"
            />
          </template>
        </b-carousel-slide>
      </b-carousel>
    </div>
    <div class="product-detail-container">
      <div class="d-flex justify-content-between align-items-center">
        <h6 class="mb-0">{{ title }}</h6>
        <span class="text-danger font-weight-bold">$ {{ price }}</span>
      </div>
      <div class="align-items-center mt-2 mb-2 float-right">
        <a class="badge badge-secondary">{{ category }}</a>
      </div>
      <div class="mt-3">
        <button class="btn btn-success btn-sm btn-block">Details</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    images: {
      type: Array,
    },
    title: {
      type: String,
    },
    price: {
      type: Number,
    },
    category: {
      type: String,
    },
  },
  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart() {
      this.sliding = true;
    },
    onSlideEnd() {
      this.sliding = false;
    },
  },
};
</script>

<style scoped>
.card {
  border-radius: 10px;
  box-shadow: 0px 6px 6px 4px rgb(204 197 185 / 50%);
}

.wishlist {
  height: 40px;
  width: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background-color: #eee;
  padding: 10px;
  cursor: pointer;
}

.img-container {
  position: relative;
}

.img-container .first {
  position: absolute;
  width: 100%;
}

.img-container img {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}

.product-detail-container {
  padding: 10px;
}

.ratings i {
  color: #a9a6a6;
}

.ratings span {
  color: #a9a6a6;
}

label.radio {
  cursor: pointer;
}

label.radio input {
  position: absolute;
  top: 0;
  left: 0;
  visibility: hidden;
  pointer-events: none;
}

label.radio span {
  height: 25px;
  width: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid #dc3545;
  color: #dc3545;
  font-size: 10px;
  border-radius: 50%;
  text-transform: uppercase;
}

label.radio input:checked + span {
  border-color: #dc3545;
  background-color: #dc3545;
  color: #fff;
}
</style>