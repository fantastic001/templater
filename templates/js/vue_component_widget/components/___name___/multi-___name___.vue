<script>
import {{name }}Service from "./service";
import {{ name }} from "./{{ name }}.vue";


export default {
    name: "multi-{{ name }}",
    props: {
        filter: {
            type: Function,
            default: (x => true)
        }
    },
    data: function () {
        return {
            items: []
        }
    },
    mounted: function () 
    {
        {{ name }}Service.list().then(response => this.items = response.data);
    },
    components: {
    	"{{ name }}": {{ name }}
    }
}
</script>

<template>
    <div class="multi-{{name}}"> 
      <{{name}}
      	v-for="item in items.filter(filter)"
      	:id="item.id"
      	:key="item.id"
        :{{name}}="item.id"
          />
    </div>

</template>

<style scoped> 



</style>
