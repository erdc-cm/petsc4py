#! /usr/bin/env python

# --------------------------------------------------------------------

from petsc4py import PETSc
try:
    from signal import signal, SIGPIPE, SIG_IGN
    signal(SIGPIPE, SIG_IGN)
except ImportError:
    pass

# --------------------------------------------------------------------

try:
    from docutils.nodes import NodeVisitor
    def unknown_visit(self, node):
        'Ignore all unknown nodes'
    NodeVisitor.unknown_visit = lambda self, node: None
    NodeVisitor.unknown_departure =  lambda self, node: None
except ImportError:
    pass

# --------------------------------------------------------------------

import re

_SIGNATURE_RE = re.compile(
    # Class name (for builtin methods)
    r'^\s*((?P<class>\w+)\.)?' +
    # The function name
    r'(?P<func>\w+)' +
    # The parameters
    r'\(((?P<self>(?:self|cls|mcs)),?)?(?P<params>.*)\)' +
    # The return value (optional)
    r'(\s*(->)\s*(?P<return>\S.*?))?'+
    # The end marker
    r'\s*(\n|\s+(--|<=+>)\s+|$|\.\s+|\.\n)')

from epydoc import docstringparser as dsp
dsp._SIGNATURE_RE = _SIGNATURE_RE

# --------------------------------------------------------------------

import sys, os
import epydoc.cli

def epydocify():
    dirname = os.path.dirname(__file__)
    config = os.path.join(dirname, 'epydoc.cfg')
    sys.argv.append('--config=' + config)
    epydoc.cli.cli()

if __name__ == '__main__':
    epydocify()

# --------------------------------------------------------------------