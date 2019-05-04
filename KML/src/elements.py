
from src.tags import KML

class Atom:

    def __init__(self, name):
        self.name = name
        self.args = None
        self.attributes = {}
        self.children = []

    def set_id(self, _id):
        self.attributes['id'] = [String(_id.strip('#'))]

    def add_class(self, _class):
        if 'class' not in self.attributes:
            self.attributes['class'] = []
        self.attributes['class'].append(String(_class.strip('-')))

    def add_attribute(self, attribute):
        self.attributes[attribute.name] = attribute.value

    def add_child(self, child):
        self.children.append(child)

    def set_args(self, arguments):
        self.args = arguments.args

    def set_value(self, assignment):
        self.children = assignment.value


    def __call__(self, scope=0, port=False, minify=False):
        indent = '\n' + '\t'*scope

        node = KML[self.name.upper()]
        if self.args:
            self.attributes.update(node.to_atom(self.args))


        if self.name == 'meta':
            return self.meta(indent)

        print(self.attributes)
        header = indent + f'<{self.name} '
        attributes = ' '.join('%s=%s' % (name, ' '.join(map(lambda x: f'"{repr(x)}"', val))) for name, val in self.attributes.items())
        premid = '>'

        if node.is_singleton():
            return header + attributes + premid

        innerHTML = ''.join(child(scope=scope+1, port=port, minify=minify) for child in self.children)
        if innerHTML:
            innerHTML += indent

        footer =  f'</{self.name}>'

        return header + attributes + premid + innerHTML + footer


    def meta(self, indent):
        return indent + indent.join('<meta name="%s" content=%s>' % (name, ' '.join(map(lambda x: f'"{repr(x)}"', val))) for name, val in self.attributes.items())



class Attribute:

    def __init__(self, name):
        self.name = name.strip('@')
        self.value = True

    def set_value(self, assignment):
        self.value = assignment.value



class Arguments:

    def __init__(self):
        self.args = []

    def add_child(self, argument):
        self.args.append(argument)



class Assignment:

    def __init__(self):
        self.value = []

    def add_child(self, child):
        self.value.append(child)


class String:
    def __init__(self, value):
        self.value = value.strip('\'\" ')

    def __call__(self, scope=0, port=False, minify=False):
        return self.value

    def __repr__(self):
        return self.value

class Script(String):
    pass



class Document(Atom):
    def __init__(self, name):
        super().__init__(name)
        self.stack = [ self ]

    def write(self):
        with open(self.name + '.html', 'w') as f:
            f.write('<!doctype html>\n' + self.children[0]())

    def feed(self, token):
        getattr(self, token.name)(token.literal)


    def white_space(self, literal):
        pass

    def comment(self, literal):
        pass

    def atom(self, literal):
        self.stack.append(Atom(literal))

    def identifier(self, literal):
        self.stack[-1].set_id(literal)

    def classifier(self, literal):
        self.stack[-1].add_class(literal)

    def attribute(self, literal):
        self.stack.append(Attribute(literal))

    def lbrace(self, literal):
        pass

    def rbrace(self, literal):
        node = self.stack.pop()
        self.stack[-1].add_child(node)

    def lparen(self, literal):
        self.stack.append(Arguments())

    def rparen(self, literal):
        args = self.stack.pop()
        self.stack[-1].set_args(args)

    def separator(self, literal):
        pass

    def assignment(self, literal):
        self.stack.append(Assignment())

    def terminator(self, literal):
        while True:
            node = self.stack.pop()
            if isinstance(node, Atom):
                self.stack[-1].add_child(node)
                break
            elif isinstance(node, Attribute):
                self.stack[-1].add_attribute(node)
                break
            else:
                self.stack[-1].set_value(node)


    def string(self, literal):
        self.stack[-1].add_child(String(literal))

    def script(self, literal):
        self.stack[-1].add_child(Script(literal))







