<script>
import {{ name }}Service from "./service";

export default {
    name: "{{ name }}",
    data: function () {
        return {
            data: {
	    },

        };
    },
    methods: {
    	submit: function() 
	{
		{{ name }}Service.submit(this.data).then(response => {
			if (response.data.code == 0) this.data.success = true;
			else this.data.success = false;

		});
	}
    }
}
</script>

<template>
    <div class="form-{{ name}}"> 
        <div class="success-box" v-if="success">{{ success_message }}</div>
	<div v-if="!success"> 
		
		{% for field in fields %}
		<p>
		<input type="{{ field["type"]}}" class="form-control" placeholder="{{ field["title"]}}" v-model="data.{{field["name"]}}" />
		</p>
		{% endfor %}

		<button type="button" class="btn btn-primary btn-lg btn-block" v-on:click="submit">Submit</button>
	</div>
    </div>

</template>

<style scoped> 

.form-{{ name }} {

}

.success-box 
{
	backgrund-color: #dfd;
	color: #0f0;
	padding: 5px;
}

</style>
