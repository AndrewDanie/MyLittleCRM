<template>
  <div class="container col-12">
    <spa-header class="text-bg-primary p-3"/>
    <SideMenu></SideMenu>
    <my-dashcard/>
    <order-add-button/>
    <orderlist/>
    <spa-footer class="text-bg-primary p-3"/>
  </div>
</template>

<script>
import SpaHeader from './components/SpaHeader.vue'
import OrderList from './components/OrderList.vue'
import Spafooter from './components/SpaFooter.vue'
import MyDashcard from './components/MyDashcard.vue'
import OrderAddButton from './components/OrderAddButton.vue'
import SideMenu from './components/SideMenu.vue'

export default {
  name: 'App',
  components: {
    "spa-header": SpaHeader,
    "orderlist": OrderList,
    "spa-footer": Spafooter,
    "my-dashcard": MyDashcard,
    "order-add-button": OrderAddButton,
    SideMenu
},
  
}
</script>

<style>

</style>
