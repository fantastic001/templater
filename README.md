
# Templater

Tool to easily create boilerplate stuff from templates 


# Writing templates 

# Scripts 

+ `META_PRE.sh` is run before user fills in wizzard 
+ `META_POST.sh` is run after wizzard and has environment variables after wizzard where name of environment variable is the same as in tpc file 


NOTE: `META_PRE.sh` can add additional data to template (which can be overriden by TPS file later on during the process) by outputing to stdout value of wanted variable, i.e.:

    echo TEMPLATE_VAR_myvar=myvalue 

will give variable `myvar` with value `myvalue` in jtemplate files