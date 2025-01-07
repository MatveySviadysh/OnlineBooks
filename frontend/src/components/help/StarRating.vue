<template>
    <div class="star-rating">
      <span v-for="index in 5" :key="index" class="star">
        <i :class="[
          'fas fa-star',
          { 'filled': index <= rating, 'empty': index > rating }
        ]"></i>
      </span>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StarRating',
    props: {
      rating: {
        type: Number,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .star-rating {
    display: flex;
    gap: 1px;
    margin-top: 3px;
  }
  
  .star {
    font-size: 0.7rem;
  }
  
  .filled {
    color: black;
  }
  
  .empty {
    color: white;
    -webkit-text-stroke: 0.3px black;
  }
  </style>