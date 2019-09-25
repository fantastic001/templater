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
        | "[" list:expr_list "]";
    expr_list = first:expression ["," rest:expr_list] | {};
'''

TEST = """

param : string = "haha"
param2 : integer = 5
param3 : boolean
some_list : [integer]
some_object : {
    a : integer
    b : string
    c : [string]
    d : {
        e : integer
    }
}
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

class String(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        return type(expression.get_type()) == String
    def __repr__(self):
        return "string"

class Integer(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        return type(expression.get_type()) == Integer
    def __repr__(self):
        return "integer"

class Boolean(Type):
    def is_primitive(self):
        return True
    def is_list(self):
        return False
    def is_object(self):
        return False
    def is_compatible(self, expression):
        return type(expression.get_type()) == Boolean
    def __repr__(self):
        return "boolean"

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
        return type(expression.get_type()) == List and expression.get_type().type == self.type

    def __repr__(self):
        return "[%s]" % self.type
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
        return False
    def __repr__(self):
        return "{\n\t" + "\n\t".join(list(str(p) for p in self.params)) + "\n}"

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
        self.val = ast.list
    def get_type(self):
        return List(self.val.first.get_type())
    def evaluate(self):
        return [self.val.first.evaluate()] + self.val.rest.evaluate()


class Parameter:
    def __init__(self, name, ptype, default):
        self.name = name
        self.ptype = ptype
        self.default = default
        print("%s = %s" % (name, default))
        if default is not None and not self.ptype.is_compatible(self.default):
            raise ValueError("%s and %s are not compatible" % (self.default.get_type(), self.ptype))
        if default is not None:
            self.default = default.evaluate()
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
            return ListExpression(ast)
        else:
            raise ValueError("Unknown expression type")
    def object(self, ast):
        return Object(ast)
    def _default(self, ast, *args, **kwargs):
        return ast

def parse_tps(tps_code):
    s = Semantics()
    parser = grako.compile(GRAMMAR)

    ast = parser.parse(tps_code, semantics=s)
    return ast

def parse_tps_file(filename):
    f = open(filename, "r")
    return parse_tps(f.read())