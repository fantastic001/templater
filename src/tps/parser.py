import grako 

__all__ = [
    "parse_tps",
    "parse_tps_file"
]

GRAMMAR = '''
    @@grammar::Calc

    start = object $ ;
    object = params:{parameter_specification};
    parameter_specification = name:parameter_name ":" type:parameter_type ["=" default:expression];
    parameter_name = /[_a-zA-Z][_a-zA-Z0-9]*/;
    parameter_type =
        type:"string"
        | type:"integer"
        | type:"boolean" 
        | "[" list_type:parameter_type "]" 
        | "{" object_type:object "}" ; 
    expression = number:/\\d+/
        | logical:"true" | logical:"false" 
        | '"' text:/[^"]*/ '"' 
        | "[" list:expr_list "]"
        | "(" obj:param_list ")";
    expr_list = first:expression ["," rest:expr_list] | {};
    param_list = first:obj_param ["," rest:param_list] | {};
    obj_param = name:parameter_name "=" expr:expression;
'''

TEST = """

param : string = "haha"
param2 : integer = 5
param3 : boolean
some_list : [integer] = [1,2,3]
some_object : {
    a : integer = 5
    b : string
    c : [string]
    d : {
        e : integer
    }
}
obj_list : [{a : string b : integer}] = [(a="a", b=1), (a ="AS", b = 2)]
l : [integer] = []
l2 : [{a : string}] = []
"""

class Type:
    def is_primitive(self):
        raise NotImplementedError("override!")
    def is_list(self):
        raise NotImplementedError("override!")
    def is_object(self):
        raise NotImplementedError("override!")
    def is_compatible(self, expression):
        raise NotImplementedError("override!")
    def __hash__(self):
        return 0

class String(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        print("Checking if compatible with String type")
        return type(expression.get_type()) == String
    def __repr__(self):
        return "string"
    def __eq__(self, other):
        return type(self) == type(other)
    def __hash__(self):
        return 1

class Integer(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        print("Checking if compatible with Integer type")
        return type(expression.get_type()) == Integer
    def __repr__(self):
        return "integer"
    def __eq__(self, other):
        return type(self) == type(other)
    def __hash__(self):
        return 2

class Boolean(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        print("Checking if compatible with Boolean type")
        return type(expression.get_type()) == Boolean
    def __repr__(self):
        return "boolean"
    def __eq__(self, other):
        return type(self) == type(other)
    def __hash__(self):
        return 3

class List(Type):
    def __init__(self, ptype):
        self.type = ptype
    def is_primitive(self):
        return False
    def is_list(self):
        return True
    def is_object(self):
        return False
    def is_compatible(self, expression):
        print("Checking type compatibility with list for expression")
        if type(expression.get_type()) == List:
            print("Expression list ... OK")
        if expression is None:
            return True # using default value
        if expression.evaluate() == []:
            return True # all empty lists are compatible
        print("t = %s" % expression.get_type().type)
        print("s = %s" % self.type)
        if expression.get_type().type == self.type:
            print("Subtypes match ... OK")
            return True
        return False
    def __repr__(self):
        return "[%s]" % self.type
    def __eq__(self, other):
        return type(self) == type(other)
    def __hash__(self):
        return 10*hash(self.type)
class Object(Type):
    def __init__(self, ast):
        self.params = ast.params
    def is_primitive(self):
        return False
    def is_list(self):
        return False
    def is_object(self):
        return True
    def is_compatible(self, expression):
        print("Checking type compatibility with Object for expression")
        return type(expression.get_type()) == Object
    def __eq__(self, other):
        if other is None:
            return False
        if not other.is_object():
            return False
        p1 = set((p.name, p.ptype) for p in self.params)
        p2 = set((p.name, p.ptype) for p in other.params)
        return p1 == p2
    def __repr__(self):
        return "{\n\t" + "\n\t".join(list(str(p) for p in self.params)) + "\n}"
    def __hash__(self):
        return 100 * hash(self.params)
    
    def evaluate(self):
        return {str(p.name): p.default for p in self.params}

class Expression:
    def get_type(self):
        raise NotImplementedError()
    def evaluate(self):
        return None
    def __repr__(self):
        return str(self.evaluate())

class NumberExpression(Expression):
    def __init__(self, ast):
        self.num = ast.number 
    def get_type(self):
        return Integer()
    def evaluate(self):
        return float(self.num)

class LogicalExpression(Expression):
    def __init__(self, ast):
        self.val = ast.logical
    def get_type(self):
        return Boolean()
    def evaluate(self):
        if self.val == "true":
            return True
        elif self.val == "false":
            return False
        raise ValueError("Wrong boolean value")
        

class StringExpression(Expression):
    def __init__(self, ast):
        self.val = ast.text
    def get_type(self):
        return String()
    def evaluate(self):
        return self.val

class ListExpression(Expression):
    def __init__(self, ast):
        self.val = ast
    def get_type(self):
        if self.val == []:
            return None # we do not know type of empty list
        return List(self.val.first.get_type())
    def evaluate(self):
        if self.val == []:
            return []
        if self.val.rest is None:
            return [self.val.first.evaluate()]
        print(self.val.first)
        print(self.val.rest)
        return [self.val.first.evaluate()] + ListExpression(self.val.rest).evaluate()

class ObjectExpression(Expression):
    def __init__(self, ast):
        self.obj = ast
        self.params = list(Parameter(name, e.get_type(), e) for name, e in self.obj.items())
    def get_type(self):
        return Object(self)
    def evaluate(self):
        d = {name: e.evaluate() for name, e in self.obj.items()}
        return d

class Parameter:
    def __init__(self, name, ptype, default):
        print("Interpreting parameter %s" % name)
        self.name = name
        self.ptype = ptype
        self.default = default
        if default is not None and not self.ptype.is_compatible(self.default):
            raise ValueError("%s and %s are not compatible" % (self.default.get_type(), self.ptype))
        if default is not None:
            self.default = default.evaluate()
        else:
            if ptype.is_object():
                self.default = self.ptype.evaluate()
            else:
                self.default = None

    def is_primitive(self):
        return self.ptype.is_primitive()

    def is_list(self):
        return self.ptype.is_list()

    def is_object(self):
        return self.ptype.is_object()
    def __repr__(self):
        return "%s : %s = %s" % (self.name, self.ptype, self.default) if self.default is not None else "%s : %s" % (self.name, self.ptype)

class Semantics:
    def parameter_type(self, ast):
        if ast.type == "string":
            return String()
        elif ast.type == "integer":
            return Integer()
        elif ast.type == "boolean":
            return Boolean()
        elif ast.list_type != None:
            return List(ast.list_type)
        elif ast.object_type != None:
            return Object(ast.object_type)
        else:
            raise ValueError("Unknown type: ^s" % ast)
    def parameter_specification(self, ast):
        p = Parameter(ast.name, ast.type, ast.default)
        return p
    def expression(self, ast):
        if ast.number != None:
            return NumberExpression(ast)
        elif ast.text != None:
            return StringExpression(ast)
        elif ast.logical != None:
            return LogicalExpression(ast)
        elif ast.list != None:
            return ListExpression(ast.list)
        elif ast.obj is not None:
            return ObjectExpression(ast.obj)
        else:
            raise ValueError("Unknown expression type")
    def object(self, ast):
        return Object(ast)
    def obj_param(self, ast):
        return {ast.name: ast.expr}
    def param_list(self, ast):
        if ast.first is None:
            return {}
        if ast.rest is None:
            return ast.first
        return dict(**ast.first, **ast.rest)
    def _default(self, ast, *args, **kwargs):
        print("No special rule for this: %s" % ast)
        return ast

def parse_tps(tps_code):
    s = Semantics()
    parser = grako.compile(GRAMMAR)

    ast = parser.parse(tps_code, semantics=s)
    return ast

def parse_tps_file(filename):
    f = open(filename, "r")
    return parse_tps(f.read())
