<template>
    <div class="searchable-dropdown">
      <input type="text" v-model="searchQuery" @input="filterOptions" :placeholder="searchPlaceholder" class="rounded border border-gray-600 bg-white pl-2" :style="{width: this.dropdownWidth, height:this.dropdownHeight}">
      <button type="button" class="show-dropdown" @click="toggleDropdown" v-if="!dropdown_active"><i class="fa fa-caret-down" aria-hidden="true"></i></button>
      <button type="button" class="show-dropdown" @click="resetDropdown" v-else><i class="fa fa-times" aria-hidden="true"></i></button>
      <ul v-if="isOpen" class="dropdown-list">
        <li v-for="(option, index) in filteredOptions" :key="index" @click="selectOption(option)" :style="{fontSize: this.fontSize}">
          {{ option }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    props:['options','dropdownWidth','dropdownHeight','searchPlaceholder','fontSize','updateValue','updateVal'],
    data() {
      return {
        isOpen: false,
        searchQuery: '',
        dropdown_active: false,
        filteredOptions: []
      };
    },
    created() {
      this.searchQuery = this.updateValue;
      this.dropdown_active = false;
    },
    methods: {
      toggleDropdown() {
        this.isOpen = true;
        if(this.isOpen){
          this.filteredOptions = this.options;
        }
        this.dropdown_active = true;
      },
      selectOption(option) {
        this.searchQuery = option;
        this.toggleDropdown();
        this.$emit('option-selected', option);
        this.isOpen = false;
      },
      filterOptions() {
        this.dropdown_active = true;
        this.isOpen = true;
        this.filteredOptions = this.options.filter(option => {
          return option.toLowerCase().includes(this.searchQuery.toLowerCase());
        });
      },
      resetDropdown(){
        this.isOpen = false;
        this.searchQuery = "";
        this.dropdown_active = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .searchable-dropdown {
    position: relative;
    display: inline-block;
  }
  .searchable-dropdown input[type="text"] {
      width: 100%;
      padding: 2px;
      border: 1px solid #ccc;
      border-radius: 4px;
  }
  .dropdown-list {
    position: absolute;
    top: 10;
    left: 10;
    z-index: 1001;
    background-color: white;
    border: 1px solid #ccc;
    list-style: none;
    padding: 0;
    margin: 0;
    width: 100%;
    max-height: 200px;
    overflow-y: auto;
    display:block
  }
  
  .dropdown-list li {
    padding: 3px;
    cursor: pointer;
    overflow: hidden;
  }
  
  .dropdown-list li:hover {
    background-color: #f0f0f0;
  }
  .show-dropdown{
    float: right;
    margin-top: 3px;
    margin-left: -20px;
    position: absolute;
    z-index: 1;
    cursor:pointer;
    border:0px;
    background-color: inherit;
    color:black;
}
.show-dropdown:focus{
    outline: none;
}
  </style>
  