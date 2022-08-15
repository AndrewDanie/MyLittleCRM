<template>
    <div align="right" class="m-3 mt-0">
        <button type="button" class="btn btn-success" @click="addPost">Добавить заказ</button>
    </div>
    <table class="table table-hover table-bordered">
        <thead >
            <td>Id Мастера</td>
            <td>Клиент</td>
            <td>Тип устройства</td>
            <td>Дата начала</td>
            <td>Дата окончания</td>
        </thead>
        <tbody>
            <tr v-for="order in orders" :key="order.id">
                <OrderItem :order="order"/>
            </tr>
        </tbody>
    </table> 
</template>

<script>
import axios from 'axios'
axios.defaults.headers.common['X-CSRF-TOKEN'] = token;
import OrderItem from './OrderItem.vue';
    export default {
    data() {
        return {
            orders: [],
            activeRow: false
        };
    },
    methods: {
        addPost() {
            axios.post(`http://127.0.0.1:8000/api/add_order`, {body: 'hello post!'})
                            .then()
                            .catch(e => {this.errors.push(e)})
        }
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