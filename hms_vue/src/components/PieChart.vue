<template>
    <div class="h-48">
        <Pie id="my-chart-id" :options="chartOptions" :data="chartData"  />
    </div>
</template>

<script>
//PieChart
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
ChartJS.register(ArcElement, Tooltip, Legend)

export default{
    name: 'PieChart',
    components: { Pie },
    data() {
        return {
            chartData: {
                datasets: [
                    {
                        backgroundColor: ['#41B883', '#E46651', '#00D8FF'],
                        data: [40, 20, 80]
                    }
                ],
                labels: ['Cardiology','Neurology','Dermatology']
            },
            chartOptions: {
                responsive: true
            },
        }
    }
}
</script>