import io
from clint.textui import puts, indent, colored
from coref import *
from consolemd import Renderer

def nsHelp(ns, path):
    help = nsGet(ns, path)
    if isNothing(help):
        help = colored.red("Help not found")
    r = Renderer()
    out = io.StringIO()
    r.render(help.value, output=out)
    help = out.getvalue()
    out.close()
    with indent(4, quote=colored.blue(' > ')):
        for h in help.split('\n'):
            puts(h)
    return ns
