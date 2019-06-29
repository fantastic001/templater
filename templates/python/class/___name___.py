from typing import *
from . import * 
class {{ name }}({% if inherit != ""%}{{ inherit }}{%else%}object{%endif%}):
    def __init__(self{%if create_parametrized_constructor%}{% for field, type in fields.items()%}, {{field}}: {{ type }}{%endfor%}{%endif%}):
        {% for field, type  in fields.items() %}
        self.{{ field }} = {% if create_parametrized_constructor%}{{ field }}{%else%}None{%endif%}
        {% endfor %}
        pass
    {% for method, type in methods.items() %}
    def {{ method }}(self, {% for param, ptype in type.items() %}{% if param != "return"%}{{ param}}: {{ ptype}}{% if not loop.last%}, {%endif%}{%endif%}{% endfor %}) -> {{ type["return"] }}:
        pass
    {%endfor %}  
