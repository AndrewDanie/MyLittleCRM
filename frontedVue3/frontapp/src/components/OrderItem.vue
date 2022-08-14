<template @mouseover="activeRow = true" @mouseleave="activeRow = false">
    <td>{{ order.master_name }}</td>
    <td>{{ order.client_name }}</td>
    <td>{{ order.device_type }}</td>
    <td>{{ order.date_start }}</td>
    <td>{{ order.date_finish }}</td>
    <td><button type="button" 
                class="btn-close" 
                aria-label="Close"
                v-show="activeRow">
        </button>
    </td>
</template>

<script>
    export default {
        props: {
            order: Object,
        },
        data() {
            return{
                activeRow: false
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>