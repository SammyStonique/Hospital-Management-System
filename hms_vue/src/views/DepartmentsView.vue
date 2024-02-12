<template>
    <NavBar
    :title="title"
    />
    <SideBar />
    <div class="main-content bg-gray-100 px-4 py-4">
        <div class="rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Departments</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="mb-4">
                    <button class="rounded-lg bg-green-500 text-white p-3">+ New Department</button>
                </div>
            <div class="shadow overflow-hidden rounded border-b border-gray-200">
                <table class="min-w-full bg-white">
                <thead class="bg-gray-800 text-white">
                    <tr>
                    <th class="w-1/3 text-left py-3 px-4 uppercase font-semibold text-sm">Name</th>
                    <th class="w-1/3 text-left py-3 px-4 uppercase font-semibold text-sm">H.O.D</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Phone No.</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Date</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Time</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Doctor</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Condition(s)</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">SMS</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Mail</th>
                    </tr>
                </thead>
                <tbody class="text-gray-700">
                <tr>
                    <td class="w-1/3 text-left py-3 px-4">Lian Smith</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">2023-11-08</td>
                    <td class="text-left py-3 px-4">12:00PM</td>
                    <td class="text-left py-3 px-4">Dr. Otieno</td>
                    <td class="text-left py-3 px-4">Malaria</td>
                    <td class="text-left py-3 px-4"><i class="fa fa-commenting" aria-hidden="true"></i></td>
                    <td class="text-left py-3 px-4"><i class="fa fa-envelope" aria-hidden="true"></i></td>
                </tr>
                <tr class="bg-gray-100">
                    <td class="w-1/3 text-left py-3 px-4">Emma Johnson</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">2023-11-08</td>
                    <td class="text-left py-3 px-4">12:00PM</td>
                    <td class="text-left py-3 px-4">Dr. Wachira</td>
                    <td class="text-left py-3 px-4">Hepatitis</td>
                    <td class="text-left py-3 px-4"><i class="fa fa-commenting" aria-hidden="true"></i></td>
                    <td class="text-left py-3 px-4"><i class="fa fa-envelope" aria-hidden="true"></i></td>
                </tr>
                <tr>
                    <td class="w-1/3 text-left py-3 px-4">Oliver Williams</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">2023-11-08</td>
                    <td class="text-left py-3 px-4">12:00PM</td>
                    <td class="text-left py-3 px-4">Dr. Nekesa</td>
                    <td class="text-left py-3 px-4">Antenatal</td>
                    <td class="text-left py-3 px-4"><i class="fa fa-commenting" aria-hidden="true"></i></td>
                    <td class="text-left py-3 px-4"><i class="fa fa-envelope" aria-hidden="true"></i></td>
                </tr>
                <tr class="bg-gray-100">
                    <td class="w-1/3 text-left py-3 px-4">Isabella Brown</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">2023-11-08</td>
                    <td class="text-left py-3 px-4">12:00PM</td>
                    <td class="text-left py-3 px-4">Dr. Awour</td>
                    <td class="text-left py-3 px-4">Physiotherapy</td>
                    <td class="text-left py-3 px-4"><i class="fa fa-commenting" aria-hidden="true"></i></td>
                    <td class="text-left py-3 px-4"><i class="fa fa-envelope" aria-hidden="true"></i></td>
                </tr>
                </tbody>
                </table>
            </div>
            </div>
        </div>
    </div>
</template>

<script>

import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

export default{
    name: 'DepartmentsView',
    data(){
    return{
      title: 'Departments'
    }
  },
    components: {
        NavBar,
        SideBar
    }
}
</script>

<style scoped>
.main-content{
  z-index: -1;
  margin-left: 338px;
  margin-top: 65px;
}
</style>