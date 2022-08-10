<template>
  <spa-header/>
  <orderlist/>
  <spa-footer/>
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
  }
}
</script>

<style>
  @import './assets/styles/bootstrap.css'
</style>
