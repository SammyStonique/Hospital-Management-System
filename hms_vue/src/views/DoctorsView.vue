<template>
    <NavBar />
    <SideBar />
    <div class="main-content bg-gray-100 p-4">
        <div class="rounded-lg bg-white w-full p-3">
            <h2 class="text-center font-bold">Doctors Register</h2>
            <div class="md:px-8 py-8 w-full">
                <div class="mb-4">
                    <button class="rounded-lg bg-green-500 text-white p-3">+ New Doctor</button>
                </div>
            <div class="shadow overflow-hidden rounded border-b border-gray-200">
                <table class="min-w-full bg-white">
                <thead class="bg-gray-800 text-white">
                    <tr>
                    <th class="w-1/3 text-left py-3 px-4 uppercase font-semibold text-sm">F. Name</th>
                    <th class="w-1/3 text-left py-3 px-4 uppercase font-semibold text-sm">L. Name</th>
                    <th class="w-1/3 text-left py-3 px-4 uppercase font-semibold text-sm">Email</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Phone No.</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Gender</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Age</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Department</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Specialization</th>
                    <th class="text-left py-3 px-4 uppercase font-semibold text-sm">Rank</th>
                    </tr>
                </thead>
                <tbody class="text-gray-700">
                <tr>
                    <td class="w-1/3 text-left py-3 px-4">Lian</td>
                    <td class="w-1/3 text-left py-3 px-4">Smith</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">Female</td>
                    <td class="text-left py-3 px-4">32</td>
                    <td class="text-left py-3 px-4">E.N.T</td>
                    <td class="text-left py-3 px-4">Throat</td>
                    <td class="text-left py-3 px-4">H.O.D</td>
                </tr>
                <tr class="bg-gray-100">
                    <td class="w-1/3 text-left py-3 px-4">Emma</td>
                    <td class="w-1/3 text-left py-3 px-4">Johnson</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">Female</td>
                    <td class="text-left py-3 px-4">39</td>
                    <td class="text-left py-3 px-4">Surgery</td>
                    <td class="text-left py-3 px-4">Neurosurgeon</td>
                    <td class="text-left py-3 px-4">Resident</td>
                </tr>
                <tr>
                    <td class="w-1/3 text-left py-3 px-4">Oliva</td>
                    <td class="w-1/3 text-left py-3 px-4">Williams</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">Male</td>
                    <td class="text-left py-3 px-4">25</td>
                    <td class="text-left py-3 px-4">Cardiology</td>
                    <td class="text-left py-3 px-4">Cardiologist</td>
                    <td class="text-left py-3 px-4">Resident</td>
                </tr>
                <tr class="bg-gray-100">
                    <td class="w-1/3 text-left py-3 px-4">Isabella</td>
                    <td class="w-1/3 text-left py-3 px-4">Brown</td>
                    <td class="w-1/3 text-left py-3 px-4"><a class="hover:text-blue-500" href="mailto:jonsmith@mail.com">jonsmith@mail.com</a></td>
                    <td class="text-left py-3 px-4"><a class="hover:text-blue-500" href="tel:622322662">0717423651</a></td>
                    <td class="text-left py-3 px-4">Female</td>
                    <td class="text-left py-3 px-4">21</td>
                    <td class="text-left py-3 px-4">Urology</td>
                    <td class="text-left py-3 px-4">Surgeon</td>
                    <td class="text-left py-3 px-4">Resident</td>
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
    name: 'DoctorsView',
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