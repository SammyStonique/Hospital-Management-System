<template>
    <div class="flex mt-6">
        <div class="basis-1/2 flex text-left">
            <div class="border-2 border-gray-200">
                <button class=" px-4 py-3 border-r-2 border-gray-200 hover:bg-slate-800 hover:text-white" @click="firstPage"><i class="fa fa-angle-double-left" aria-hidden="true"></i></button>
                <div class="hidden">{{ showPreviousBtn }}</div>
                <button class=" px-4 py-3 border-r-2 border-gray-200 hover:bg-slate-800 hover:text-white" @click="loadPrev" v-if="showPreviousBtn">Previous</button>
                <button class=" px-4 py-3 border-r-2 border-gray-200 hover:bg-slate-800 hover:text-white">{{currentPage}}</button>
                <button class=" px-4 py-3 border-r-2 border-gray-200 hover:bg-slate-800 hover:text-white" @click="loadNext" v-if="showNextBtn">Next</button>
                <div class="hidden">{{ showNextBtn }}</div>
                <button class="px-4 py-3 hover:bg-slate-800 hover:text-white" @click="lastPage"><i class="fa fa-angle-double-right" aria-hidden="true"></i></button>
            </div>
        </div>
        <div class="basis-1/2 text-right">
            <p style="font-size: 12px">
                Showing {{ result }} records  of {{ count }} 
            </p>
        </div>
    </div>
</template>

<script>
export default{
    props:['currentPage','count','nextPage','prevPage','result','firstPage','lastPage','showPreviousBtn','showNextBtn'],
    data(){
        return{
    
        }
    },
    methods:{
        loadPrev(){
            this.$emit("loadPrev");
        },
        loadNext(){
            this.$emit("loadNext");
        },
        firstPage(){
            this.$emit("firstPage");
        },
        lastPage(){
            this.$emit("lastPage");
        },
    },
    mounted(){
        
    }
}
</script>

<style>
</style>