<template>
  <NavBar
  :title="title"
   />
  <SideBar />
  <div class="main-content bg-gray-100 px-4 py-4">
    <div class="flex w-full">
      <div class="w-3/4 mr-3">
        <div class="flex mb-3">
          <div class="w-1/2 rounded-lg py-3 px-2 bg-white mr-2">
            <h1 class="font-bold mb-2">Activity Overview</h1>
            <div class="flex w-full mb-3">
              <div class="w-1/2 rounded-lg h-16 border-2 p-2 mr-4">
                <div class="w-full flex">
                  <div class="w-1/4 rounded-lg bg-cyan-600 h-10 grid place-items-center">
                    <i class="fa fa-calendar" aria-hidden="true"></i>
                  </div>
                  <div class="w-3/4 px-2">
                    <p class="font-bold">500</p>
                    <p class="font-light text-sm">Appointments</p>
                  </div>
                </div>
              </div>
              <div class="w-1/2 rounded-lg h-16 border-2 p-2">
                <div class="w-full flex">
                  <div class="w-1/4 rounded-lg bg-orange-400 h-10 grid place-items-center">
                    <i class="fa fa-scissors" aria-hidden="true"></i>
                  </div>
                  <div class="w-3/4 px-2">
                    <p class="font-bold">400</p>
                    <p class="font-light text-sm">Operations</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="flex w-full mb-3">
              <div class="w-1/2 rounded-lg h-16 border-2 p-2 mr-4">
                <div class="w-full flex">
                  <div class="w-1/4 rounded-lg bg-indigo-600 h-10 grid place-items-center">
                    <i class="fa fa-bed" aria-hidden="true"></i>
                  </div>
                  <div class="w-3/4 px-2">
                    <p class="font-bold">150</p>
                    <p class="font-light text-sm">New Patients</p>
                  </div>
                </div>
              </div>
              <div class="w-1/2 rounded-lg h-16 border-2 p-2">
                <div class="w-full flex">
                  <div class="w-1/4 rounded-lg bg-rose-600 h-10 grid place-items-center">
                    <i class="fa fa-user-md" aria-hidden="true"></i>
                  </div>
                  <div class="w-3/4 px-2">
                    <p class="font-bold">60</p>
                    <p class="font-light text-sm">Doctors</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="w-1/2 rounded-lg py-3 px-2 bg-white">
            <h1 class="font-bold mb-2">Patient Visit By Department</h1>
            <div class="">
              <PieChart />
            </div>
          </div>
        </div>
        <div class="w-full rounded-lg py-3 px-2 bg-white h-56 mb-3">
          <h1 class="font-bold">Hospital Survey</h1>
        </div>
        <div class="w-full rounded-lg py-3 px-2 bg-white h-56">
          <h1 class="font-bold mb-3">Appointment Activity</h1>
          <table class="table-auto border-collapse w-full">
            <thead class="border-b border-slate-500 font-thin text-sm bg-gray-100">
            <th>Name</th>
            <th>Email</th>
            <th>Date</th>
            <th>Visit Time</th>
            <th>Doctor</th>
            <th>Condition(s)</th>
          </thead>
          <tbody class="text-sm py-2">
            <tr class="py-8">
              <td>Glenn R. Green</td>
              <td>glenngreen@armyspy.com</td>
              <td>12-09-2023</td>
              <td>11:52 AM</td>
              <td>Dr. Otieno</td>
              <td>Malaria</td>
            </tr>
            <tr class="py-4">
              <td>Marguerite W. Miller</td>
              <td>margueritemiller@rhyta.com</td>
              <td>31-08-2023</td>
              <td>02:17 PM</td>
              <td>Dr. Omondi</td>
              <td>Epilepsy</td>
            </tr>
            <tr class="py-4">
              <td>Marguerite W. Miller</td>
              <td>margueritemiller@rhyta.com</td>
              <td>31-08-2023</td>
              <td>02:17 PM</td>
              <td>Dr. Omondi</td>
              <td>Epilepsy</td>
            </tr>
          </tbody>
          </table>
        </div>
      </div>
      <div class="w-1/4">
        <div class="rounded-lg bg-blue-900 h-64 p-2 mb-3 text-white">
          <h1 class="font-bold mb-2">Popular Doctors List</h1>
          <div class="flex text-xs">
            <div class="w-3/4">
              <h1 class="text-xs mb-2">Doctor Name</h1>
              <div class="flex mb-2">
                <div class="w-1/4 mr-3">
                  <div class="rounded-full h-11 w-11  mr-3 overflow-hidden border-2 border-white hover:border-2 hover:border-blue-400 hover:opacity-50 hover:shadow-2 hover:shadow-2xl">
                      <button>
                        <img src="./../assets/freddy-review.jpeg" alt="Profile Pic" class="w-full h-full object-cover"/>
                      </button>
                  </div>
                </div>
                <div class="w-3/4 flex items-center">
                  <p>Dr. Omondi</p>
                </div>
                
              </div>
              <div class="flex mb-2">
                <div class="w-1/4 mr-3">
                  <div class="rounded-full h-11 w-11  mr-3 overflow-hidden border-2 border-white hover:border-2 hover:border-blue-400 hover:opacity-50 hover:shadow-2 hover:shadow-2xl">
                      <button>
                        <img src="./../assets/mercy.jpg" alt="Profile Pic" class="w-full h-full object-cover"/>
                      </button>
                  </div>
                </div>
                <div class="w-3/4 flex items-center">
                  <p>Dr. Aoko</p>
                </div>
                
              </div>
              <div class="flex">
                <div class="w-1/4 mr-3">
                  <div class="rounded-full h-11 w-11  mr-3 overflow-hidden border-2 border-white hover:border-2 hover:border-blue-400 hover:opacity-50 hover:shadow-2 hover:shadow-2xl">
                      <button>
                        <img src="./../assets/lavender.jpg" alt="Profile Pic" class="w-full h-full object-cover"/>
                      </button>
                  </div>
                </div>
                <div class="w-3/4 flex items-center">
                  <p>Dr. Atieno</p>
                </div>
                
              </div>
            </div>
            <div class="w-1/4">
              <h1 class="text-xs mb-2">Status</h1>
              <div class="mb-6">
                <button class="rounded-full w-full bg-white p-1.5 text-green-800">Available</button>
              </div>
              <div class="mb-6">
                <button class="rounded-full w-full bg-white p-1.5 text-red-800">Absent</button>
              </div>
              <div class="">
                <button class="rounded-full w-full bg-white p-1.5 text-yellow-800">Occupied</button>
              </div>
            </div>
          </div>
        </div>
        <div class="rounded-lg bg-white h-56 p-2 mb-3">
          <h1 class="font-bold">Average Patient Visits</h1>
        </div>
        <div class="rounded-lg bg-white h-56 p-2">
          <h1 class="font-bold">Employees</h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PieChart from '@/components/PieChart.vue'
import NavBar from '@/components/NavBar.vue'
import SideBar from '@/components/SideBar.vue'

export default {
  name: 'HomeView',
  data(){
    return{
      title: 'Dashboard'
    }
  },

  mounted(){
  },
  components: {
    PieChart,
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
  /* margin-left: 350px;
  margin-top: 95px; */
}
</style>
