<template >
  <div class="container">
    <spa-header class="text-bg-primary p-3"/>
    <orderlist/>
    <spa-footer class="text-bg-primary p-3"/>
  </div>
</template>

<script>
import SpaHeader from './components/SpaHeader.vue'
import OrderList from './components/OrderList.vue'
import Spafooter from './components/SpaFooter.vue'

export default {
  name: 'App',
  components: {
    'spa-header': SpaHeader,
    'orderlist': OrderList,
    'spa-footer': Spafooter,
  },
  
}
</script>

<style>
  @import './assets/styles/bootstrap.css'
</style>
