<template>
    <div class="searchable-dropdown">
      <input type="text" v-model="searchQuery" @input="filterOptions" placeholder="Search..." class="rounded border border-gray-600 bg-white text-lg pl-2 pt-2 w-60">
      <ul v-if="isOpen" class="dropdown-list">
        <li v-for="(option, index) in filteredOptions" :key="index" @click="selectOption(option)">
          {{ option }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isOpen: false,
        searchQuery: '',
        options: ['Option 1', 'Option 2', 'Option 3', 'Option 4'], // Replace with your options
        filteredOptions: []
      };
    },
    methods: {
      toggleDropdown() {
        this.isOpen = !this.isOpen;
      },
      selectOption(option) {
        this.searchQuery = option;
        this.toggleDropdown();
      },
      filterOptions() {
        this.filteredOptions = this.options.filter(option => {
          return option.toLowerCase().includes(this.searchQuery.toLowerCase());
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .searchable-dropdown {
    position: relative;
  }
  
  .dropdown-list {
    position: absolute;
    top: 100%;
    left: 0;
    z-index: 1000;
    background-color: white;
    border: 1px solid #ccc;
    list-style: none;
    padding: 0;
    margin: 0;
    max-height: 200px;
    overflow-y: auto;
  }
  
  .dropdown-list li {
    padding: 5px;
    cursor: pointer;
  }
  
  .dropdown-list li:hover {
    background-color: #f0f0f0;
  }
  </style>
  