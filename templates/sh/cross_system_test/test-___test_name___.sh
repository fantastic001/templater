LOG_FILE="logs/{{  test_name}}.log"
do_test() 
{
	{% for variable in variables%} 
	echo "{{variable.upper()}} = ${{variable.upper()}}"
	{% endfor %}
	echo "__________________________"
}

check_error() 
{
	return 1 # test failed
}

log_error() 
{
	echo "TEST FAILED: {{test_name}}" >> $LOG_FILE
	{% for variable in variables%} 
	echo "    | {{variable.upper()}} = ${{variable.upper()}}" >> $LOG_FILE
	{% endfor %}
	
}

echo "Executing test {{ test_name }}"
echo > $LOG_FILE

{% for testcase in testcases%}


{% for variable in variables %}
export {{ variable.upper() }}="{{ testcase.get(variable, "") }}"
{% endfor %}
do_test
if check_error; then
	log_error
fi
{% endfor %}
