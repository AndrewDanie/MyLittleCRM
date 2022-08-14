<tr v-for="order in orders" :key="order.id" class="mt-3">
    <td>Id Мастера: {{ order.master_name }}</td>
    <td>Клиент: {{ order.client_name }}</td>
    <td>Тип устройства: {{ order.device_type }}</td>
    <td>Дата начала: {{ order.date_start }}</td>
    <td>Дата окончания: {{ order.date_finish }}</td>
</tr>