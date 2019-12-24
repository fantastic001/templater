package {{ package }};

import java.util.List;

import {{ model_package }}.{{ model_name }};
import {{ repository_package }}.{{ repository_name }};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class {{ name }} {

	
	@Autowired
	{{ repository_name }} {{ repository_name[0].lower() + repository_name[1:] }};
	
	
	public {{ model_name }} findOneByid(Long id) {
		return {{ repository_name[0].lower() + repository_name[1:] }}.findOneByid(id);
	}
	
	public List<{{ model_name }}> findAll() {
		return {{ repository_name[0].lower() + repository_name[1:] }}.findAll();
	}
}
