<script setup>
import Background from '../components/Background.vue'
import WelcomeWindow from '@/components/WelcomeWindow.vue';
</script>

<template>
  <Background class="background-container" bottomColor="#ffc7c7" topColor="#ffffff">
    <img class="background-image" src="../assets/cosmicbg.png" />
    <WelcomeWindow class="welcome-window" />
  </Background>
</template>

<style>
.background-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover; /* This will make the image cover the entire container */
}

</style>
