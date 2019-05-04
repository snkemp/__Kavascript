
from enum import Enum

class KML(Enum):

    A = ('href',)
    ABBR = ('title',)
    ADDRESS = ()
    AREA = ('shape', 'coords', 'href', 'alt')
    ARTICLE = ()
    ASIDE = ()
    AUDIO = ('src', 'controls')

    B = ()
    BASE = ('href',)
    BDI = ()
    BDO = ('dir',)
    BLOCKQUOTE = ('cite',)
    BODY = ('onload',)
    BR = ()
    BUTTON = ('type', 'value')

    CANVAS = ('width', 'height')
    CAPTION = ('align',)
    CITE = ()
    CODE = ()
    COL = ()
    COLGROUP = ()

    DATA = ('value',)
    DATALIST = ()
    DD = ()
    DEL = ('cite',)
    DETAILS = ('open',)
    DFN = ()
    DIALOG = ('open',)
    DIV = ()
    DL = ()
    DT = ()

    EM = ()
    EMBED = ('src', 'type', 'width', 'height')

    FIELDSET = ()
    FIGCAPTION = ()
    FIGURE = ()
    FOOTER = ()
    FORM = ('action', 'method')

    H1 = ()
    H2 = ()
    H3 = ()
    H4 = ()
    H5 = ()
    H6 = ()
    HEAD = ()
    HEADER = ()
    HR = ()
    HTML = ('xmlns',)

    I = ()
    IFRAME = ('src', 'width', 'height')
    IMG = ('src', 'width', 'height', 'alt')
    INPUT = ('type', 'name', 'alt')
    INS = ('cite',)

    KBD = ()

    LABEL = ('for', 'form')
    LEGEND = ()
    LI = ('type', 'value')
    LINK = ('rel', 'type', 'href')

    MAIN = ()
    MAP = ('name',)
    MARK = ()
    META = ()
    METER = ('value', 'min', 'max')

    NAV = ()
    NOSCRIPT = ()

    OBJECT = ('data', 'width', 'height')
    OL = ('type', 'start', 'reversed')
    OPTGROUP = ('label',)
    OPTION = ('label', 'value')
    OUTPUT = ('name', 'for', 'form')

    P = ()
    PARAM = ('name', 'value')
    PICTURE = ()
    PRE = ()
    PROGRESS = ('value', 'max')

    Q = ('cite',)

    RP = ()
    RT = ()
    RUBY = ()

    S = ()
    SAMP = ()
    SCRIPT = ('src', 'type')
    SECTION = ()
    SELECT = ('name',)
    SMALL = ()
    SOURCE = ('src', 'type')
    SPAN = ()
    STRONG = ()
    STYLE = ('src',)
    SUB = ()
    SUMMARY = ()
    SUP = ()
    SVG = ('width', 'height')

    TABLE = ()
    TBODY = ()
    TD = ()
    TEMPLATE = ()
    TEXTAREA = ('cols', 'rows', 'placeholder', 'wrap')
    TFOOT = ()
    TH = ('sorted',)
    THEAD = ()
    TIME = ('datetime',)
    TITLE =  ()
    TR = ()
    TRACK = ('src', 'kind', 'srclang')

    U = ()
    UL = ()

    VAR = ()
    VIDEO = ('src', 'width', 'height', 'controls')

    WBR = ()

    def is_singleton(self):
        return self.name.lower() in ('area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'param', 'source', 'track')

    def to_atom(self, args):
        return zip(self.value, ([a] for a in args))
