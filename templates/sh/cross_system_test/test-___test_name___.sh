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
	return 0 # test failed
}

log_error() 
{
	echo "TEST FAILED: {{test_name}}:$TESTCASE" >> $LOG_FILE
	{% for variable in variables%} 
	echo "    | {{variable.upper()}} = ${{variable.upper()}}" >> $LOG_FILE
	{% endfor %}
	
}

do_clean_failed() 
{
	echo "$TESTCASE: Clean up"
}

do_clean_success() 
{
	echo "$TESTCASE: Clean up"
	
}

echo "Executing test {{ test_name }}"
echo > $LOG_FILE

{% for testcase in testcases %}
export TESTCASE="{{ loop.index }}"
{% for variable in variables %}
export {{ variable.upper() }}="{{ testcase.get(variable, "") }}"
{% endfor %}
do_test
if check_error; then
	log_error
	do_clean_failed
else
	do_clean_success
fi

{% endfor %}
