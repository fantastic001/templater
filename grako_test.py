import grako 

GRAMMAR = '''
    @@grammar::Calc

    start = object $ ;
    object = {parameter_specification};
    parameter_specification = name:parameter_name ":" type:parameter_type ["=" default:expression];
    parameter_name = /[_a-zA-Z][_a-zA-Z0-9]*/;
    parameter_type =
        "string"
        | "integer"
        | "boolean" 
        | "[" parameter_type "]" 
        | "{" object "}" ; 
    expression = /\d+/
        | "true" | "false"
        | "[" expr_list "]";
    expr_list = expression ["," expr_list] | {};
'''

TEST = """

param : string
param2 : integer
param3 : boolean
some_list : [integer]
some_dict : {
    p1 : string
    p2 : integer
}
"""


class Semantics:
    def parameter_specification(self, ast):
        print(ast.name)
        return ast
    def _default(self, ast, *args, **kwargs):
        return ast
s = Semantics()
parser = grako.compile(GRAMMAR)

ast = parser.parse(TEST, semantics=s)

