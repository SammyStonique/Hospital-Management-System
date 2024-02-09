<template>
    <div class="login">
        <div class="w-full h-screen bg-slate-700 grid place-items-center">
            <div class="w-1/2 h-80 bg-white p-4 rounded-lg">
                <div class="text-center grid place-items-center">
                    <div class="flex w-36">
                    <div class="w-1/2 rounded-full">
                        <img src="@/assets/download.png" alt="Logo" class="">
                    </div>
                    <div class="w-1/2 pl-2">
                        <h4 class="text-2xl py-4">K.H.S</h4>
                    </div>
                </div>
                </div>
                <div class="py-4 px-8">
                    <form action="">
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Username:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="text" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg">
                            </div>
                        </div>
                        <div class="py-3 px-3 flex">
                            <div class="w-1/4 grid justify-items-end place-items-center">
                                <label for="">Password:</label>
                            </div>
                            <div class="w-3/4">
                                <input type="password" name="" id="" class="ml-4 w-3/4 rounded-lg border-gray-500 border-2 p-2 text-lg">
                            </div>
                        </div>
                        <div class="mt-3 grid justify-items-end">
                            <div class="pr-24">
                                <button class="bg-green-300 px-6 py-2 rounded-lg w-32">Login</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

export default {
  name: 'LoginView',
  components: {
    
  }
}
</script>