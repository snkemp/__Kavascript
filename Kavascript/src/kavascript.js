/**
 * Kavascript
 *
 * snkemp
 * Feb 2019
 *
**/


function kavascript(script='index.ks') {

    source = document.getElementById(script).innerHTML

    kdoc = KDocument(document)

    for( token of tokenize(source) )
        kdoc.feed(token)

}


function* tokenize(source) {
    definitions = {
        'word': '[a-zA-Z]\w*',
        'id': '#',
        'class': '-',
        'terminator': ';',
        'lbrace': '\{',
        'rbrace': '\}',
        'expression': '.*?'
    }

    pattern = ""
    for( def in definitions )
        pattern += `(?P<${def}>${definitions[def]})`

    lexer = new RegExp(pattern)
    while true {
        match = lexer.match(source)
        if(!match)
            break

        yield match
    }
}





class KDocument {

    constructor(dom) {
        this.head = dom
    }

    feed(token) {


    }
}

