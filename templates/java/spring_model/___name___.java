package {{ package }};

import java.time.LocalDateTime;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToOne;
import javax.persistence.OneToMany;
import javax.persistence.ManyToMany;

@Entity
public class {{ name }} {

	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
    	private Long id;
	
	{% for field in fields %}
	{% if field["bind"] in ["OneToOne", "ManyToOne", "OneToMany", "ManyToMany"]%}@{{ field["bind"]}}{% endif %}
    	{% if field["join_column"] %}@JoinColumn{%endif%}
	private {{ field["type"] }} {{ field["name"] }};
	{% endfor %}
	
	public {{ name }}() 
	{
	}
	public {{ name }}({% for field in fields + [{"name": "id", "type": "Long"}] 
		%}{{ field["type"] }} _{{ field["name"] }}{% if not loop.last %}, {% endif %}{% endfor %}) {
		super();
		{% for field in fields + [{"name": "id", "type": "Long"}] %} 
		this.{{ field["name"] }} = _{{ field["name"] }};
		{% endfor %}
	}
	
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
