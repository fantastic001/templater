<script>
import {{ name }}Service from "./service";

export default {
    name: "{{ name }}",
    props: ["{{ name }}"],
    data: function () {
        return {
            data: {},
        }
    },
    mounted: function () 
    {
        {{name }}Service.get(this.{{name }}).then(response => this.data = response.data);
    },
    methods: 
    {
    	deleteItem: function() 
	{
		{{name }}Service.delete(this.{{name }}).then(response => this.data = {});
	}
	// add additional methods here
    }
}
</script>

<template>
    <div class="widget-{{ name }}"> 
    <span class="badge badge-pill badge-info">{{ name }}: </span>

    <div class="card" style="width: 18rem;">
      <p>TOP</p>
      <div class="card-body">
        <h5 class="card-title"></h5>
        <p class="card-text item-description"></p>
      </div>

    
     <ul class="list-group list-group-flush">
        <li class="list-group-item"></li>
     </ul>


    <div class="card-body">
      <button class="btn btn-danger" @click="deleteItem" v-if="true">Delete</button>
      <button class="btn btn-primary" @click="orderItem" v-if="true">Button</button>
    </div>
    </div>
    </div>

</template>

<style scoped> 



</style>
