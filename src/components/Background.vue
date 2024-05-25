<template>
    <div :style="gradientStyle" class="background">
        <slot></slot>
    </div>
</template>
  
<script>
  export default {
    name: 'Background',
    props: {
      bottomColor: {
        type: String,
        required: true
      },
      topColor: {
        type: String,
        required: true
      }
    },
    computed: {
      gradientStyle() {
        return {
          background: `linear-gradient(to bottom, ${this.topColor}, ${this.bottomColor})`
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .background {
    width: 100vw;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  </style>
  