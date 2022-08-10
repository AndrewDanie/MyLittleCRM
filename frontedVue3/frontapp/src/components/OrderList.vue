<template>
    <div v-for="order in orders" :key="order.id" class="m-4 p-2 text-bg-info">
        <div>{{ order.master_name }}</div>
        <div>{{ order.client_name }}</div>
        <div>{{ order.device_type }}</div>
        <div>{{ order.date_start }}</div>
        <div>{{ order.date_finish }}</div>
    </div>
</template>

<script>
import axios from 'axios'
    export default {
        data() {
            return {
            orders: []
            };
        },
        mounted() {
            axios
            .get('http://127.0.0.1:8000/api/orderlist')
            .then(response => (this.orders = response.data));
        }
    }
    
</script>

<style lang="scss" scoped>

</style>