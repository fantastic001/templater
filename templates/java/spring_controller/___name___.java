package {{package }};

import {{ service_package }}.{{ service_name }};

import java.util.List;

import {{ model_package }}.{{ model_name }};

import {{ dto_package }}.{{ dto_name }};

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestBody;

@RestController
@RequestMapping(value = "{{ endpoint }}")
public class {{ name }} {
	
	@Autowired 
	{{ service_name }} {{ service_name[0].lower() + service_name[1:] }};
		
	
	@GetMapping(value="/")
	public ResponseEntity<List<{{ model_name }}>> findAll(){
		return new ResponseEntity<>({{ service_name[0].lower() + service_name[1:] }}.findAll(), HttpStatus.OK);
	}
	
	@GetMapping(value="/{id}")
	public ResponseEntity<{{ model_name }}> findOneByid(@PathVariable("id") Long id){
		return new ResponseEntity<>({{ service_name[0].lower() + service_name[1:] }}.findOneByid(id), HttpStatus.OK);
	}
	
	@PostMapping(consumes = "application/json")
	public ResponseEntity<Long> save(@RequestBody {{ dto_name }} dto){
		
		{{ model_name }} {{ model_name[0].lower() + model_name[1:] }} = {{ service_name[0].lower() + service_name[1:] }}.save(dto);
		return new ResponseEntity<>({{ model_name[0].lower() + model_name[1:] }}.getId(),HttpStatus.OK);
	}
	
	
	@PostMapping(value="/{id}", consumes = "application/json")
	public ResponseEntity<Long> update(@RequestBody {{ dto_name }} dto){
		
		{{ model_name }} data = {{ service_name[0].lower() + service_name[1:] }}.save(dto);
		return new ResponseEntity<>(data.getId(),HttpStatus.OK);
	}
}
