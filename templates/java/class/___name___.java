package {{ package }};

import java.util.Date;

public class {{ name }} {
	
	{% for field in fields %}
	private {{ field["type"] }} {{ field["name"] }}; 
	{% endfor %}
	public {{ name }}() 
	{
	}
	public {{ name }}({% for field in fields %}{{ field["type"] }} _{{ field["name"] }}{% if not loop.last %}, {% endif %}{% endfor %}) {
		super();
		{% for field in fields %} 
		this.{{ field["name"] }} = _{{ field["name"] }};
		{% endfor %}
	}
	
	{% for field in fields %} 
	public {{field["type"]}} get{{field["name"][0].capitalize() + field["name"][1:] }}() 
	{
		return this.{{ field["name"] }};
	}

	public void set{{field["name"][0].capitalize() + field["name"][1:] }}({{ field["type"] }} newValue) 
	{
		this.{{ field["name"] }} = newValue;
	}
	{% endfor %}
}
