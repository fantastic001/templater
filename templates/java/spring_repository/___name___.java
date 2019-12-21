package {{ package }};

import java.util.List;

import {{ model_package }}.{{ model_name }};
import org.springframework.data.jpa.repository.JpaRepository;

public interface {{ name }} extends JpaRepository<{{ model_name }}, Long> {

	
	public {{ model_name }} findOneByid(Long id);
	
	public List<{{ model_name }}> findAll();
	
}
