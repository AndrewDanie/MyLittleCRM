<template>
    <table class="table table-hover table-bordered">
        <thead >
            <td>Id Мастера</td>
            <td>Клиент</td>
            <td>Тип устройства</td>
            <td>Дата начала</td>
            <td>Дата окончания</td>
        </thead>
        <tbody>
            <tr v-for="order in orders" :key="order.id" class="mt-3"  >
                <OrderItem :order="order"/>
            </tr>
        </tbody>
    </table> 
</template>

<script>
import axios from 'axios'
import OrderItem from './OrderItem.vue';
    export default {
    data() {
        return {
            orders: [],
            activeRow: false
        };
    },
    mounted() {
        axios
            .get("http://127.0.0.1:8000/api/orderlist")
            .then(response => (this.orders = response.data));
    },
    components: { OrderItem }
}
</script>

<style scoped>
    /* @import '../assets/styles/bootstrap.css' */
</style>