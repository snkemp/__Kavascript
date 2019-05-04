

import os, re, code

from src.utils import *
from src.elements import *


class Token:

    def __init__(self, match):
        self.name = match.lastgroup
        self.literal = match.group(0)

    def __repr__(self):
        return f'<{self.name} : {self.literal}>'


def tokenize(filename, pattern):
    with open(filename, 'r') as f:
        text = f.read()
        return [ Token(match) for match in pattern.finditer(text) ]


def context_free_grammar():

    nodes = {
        'white_space': '\s+',
        'comment': '/\*.*?\*/',

        'atom': '[a-z]\w*',
        'identifier': '#[a-z]\w*',
        'classifier': '-[a-z]\w*',
        'attribute': '@[a-z]\w*',

        'lbrace': '\{',
        'rbrace': '\}',
        'lparen': '\(',
        'rparen': '\)',

        'separator': ',',
        'assignment': ':',
        'terminator': ';',

        'string': '\'([^\']*?)\'',
        'script': '"""([^\"]*?)"""',
    }


    pattern = "|".join('(?P<%s>%s)' % (n, p) for n,p in nodes.items())
    return re.compile(pattern, re.M | re.I)

def parse(filename, port=False, minify=False):

    doc = Document(filename)
    tokens = tokenize(filename, context_free_grammar())
    for t in tokens:
        doc.feed(t)

    doc.write()
    #code.interact(local=locals())


