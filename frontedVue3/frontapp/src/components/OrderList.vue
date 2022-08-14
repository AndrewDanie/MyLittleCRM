<template>
    <table class="table table-hover table-bordered">
        <thead>
            <td>Id Мастера</td>
            <td>Клиент</td>
            <td>Тип устройства</td>
            <td>Дата начала</td>
            <td>Дата окончания</td>
        </thead>
        <tbody>
            <tr v-for="order in orders" :key="order.id" class="mt-3" onclick="window.location.href='https://google.com'; return false">
                <td>{{ order.master_name }}</td>
                <td>{{ order.client_name }}</td>
                <td>{{ order.device_type }}</td>
                <td>{{ order.date_start }}</td>
                <td>{{ order.date_finish }}</td>
            </tr>
        </tbody>
    </table> 
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

<style scoped>
    /* @import '../assets/styles/bootstrap.css' */
</style>