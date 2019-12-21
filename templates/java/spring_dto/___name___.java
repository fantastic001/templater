package {{ package }};

import {{ model_package }}.{{ model_name}};

public class {{ name }} {
	private Long id;

	{% for reference in foreign_references %}
	private Long {{ reference }}Id;
	{% endfor %}
	
	{% for field in fields %}
	private {{ field["type"] }} {{ field["name"] }};
	{% endfor %}
	
	public {{ name }}({{ model_name }} {{model_name[0].lower() + model_name[1:] }}) {
		// implement 
	}
	
	{% for reference in foreign_references %}
	public Long get{{ reference[0].upper() + reference[1:] }}Id() {
		return {{ reference }}Id;
	}
	public void set{{ reference[0].upper() + reference[1:]}}Id(Long {{ reference }}Id) {
		this.{{ reference }}Id = {{ reference }}Id;
	}
	{% endfor %}
	
	{% for field in fields %}
	public {{ field["type"] }} get{{ field["name"][0].upper() + field["name"][1:] }}() {
		return {{ field["name"] }};
	}
	public void set{{ field["name"][0].upper() + field["name"][1:]}}({{ field["type"] }} {{ field["name"] }}) {
		this.{{ field["name"] }} = {{ field["name"] }};
	}
	{% endfor %}

	public Long getId() {
		return this.id;
	}

	public void setId(Long id) {
		this.id = id;
	}
	
}
