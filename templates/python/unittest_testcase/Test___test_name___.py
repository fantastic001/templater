
from {{ module_name }} import * 

import unittest 

{% for dependency in dependencies %}
class Mock{{ dependency }}({{ dependency["name"] }}):
    {% for method in dependency["methods"] %}def {{ method["name"] }}(self, {% for p in range(method["param_count"])%}x{{p}}{% endfor%}):
        pass
    {% endfor %}
{% endfor %}

class Test{{ test_name }}(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_basic(self):
        self.assertEqual(1+1, 2)
        self.fail("implement")


