package com.stefan.prodex.data;

import java.util.Date;

public class {{ name }} {
	
	{% for field, type in fields.items() %}
	private {{ type }} {{ field}}; 
	{% endfor %}
	public {{ name }}() 
	{
	}
	public {{ name }}({% for field, type in fields.items() %}{{ type }} _{{ field }}{% if not loop.last %}, {% endif %}{% endfor %}) {
		super();
		{% for field, type in fields.items() %} 
		this.{{ field }} = _{{ field }};
		{% endfor %}
	}
	
	{% for field, type in fields.items() %} 
	public {{type}} get{{field[0].capitalize() + field[1:] }}() 
	{
		return this.{{ field }};
	}

	public void set{{field[0].capitalize() + field[1:] }}({{ type }} newValue) 
	{
		this.{{ field}} = newValue;
	}
	{% endfor %}
}
