
import re


class Conjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Disjunction:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Optional:
    def __init__(self, child):
        self.child = child

class Any:
    def __init__(self, child):
        self.child = child

class Some:
    def __init__(self, child):
        self.child = child

class Node:
    def __init__(self, name):
        self.name = name


class Tree:

    def __init__(self, statement):
        self._output = []
        self._opers = []

        for token in statement:
            self._add_token(token)

        while self._opers:
            self._pop_operator()

        self.head = self._output[0]


    def _add_token(self, token):
        if token == '(':
            self._opers.append(token)

        elif token == ')':
            while self._opers[-1] != '(':
                self._pop_operator()

            self._opers.pop()

        elif token == '?':
            self._output[-1] = Optional(self._output[-1])

        elif token == '*':
            self._output[-1] = Any(self._output[-1])

        elif token == '+':
            self._output[-1] = Some(self._output[-1])

        elif token == '|':
            while self._opers and self._opers[-1] == ',':
                self._pop_operator()

            self._opers.append(token)

        elif token == ',':
            self._opers.append(token)

        else:
            self._output.append(Node(token))


    def _pop_operator(self):

        node = self._opers.pop()
        r = self._output.pop()
        l = self._output.pop()

        if node == ',':
            self._output.append(Conjunction(l, r))
        elif node == '|':
            self._output.append(Disjunction(l, r))
        else:
            raise Exception()


class ContextFreeGrammar(dict):

    def __init__(self, files=[]):
        self._text = ""
        for f in files:
            self._parse(f)


        self._build_grammar()


    def _parse(self, filename):
        with open(filename) as f:

            for line in f.readlines():
                if not line.startswith('#'):
                    self._text += line

    def _build_grammar(self):
        for statement in self._generate_statements():
            name, assign, *args = statement
            self[name] = Tree(args)


    def _generate_statements(self):
        tokens = re.findall('\w+|\'.*?\'|\".*?\"|[^\w\s]', self._text)
        statement = []
        for token in tokens:
            token = token.strip()

            if token == ';':
                if statement:
                    yield statement
                    statement = []
            else:
                statement.append(token)

        if statement:
            return statement





