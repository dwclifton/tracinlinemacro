""" @package InlineMacro
    @file macro.py
    @brief The InlineMacro class

    Return raw, inline XHTML markup that has been validated and sanitized.

    @author Douglas Clifton <dwclifton@gmail.com>
    @date December, 2008
    @version 0.11.0
"""

from trac.core import *
from trac.wiki.macros import WikiMacroBase
from trac.wiki.formatter import system_message
from trac.util.html import TracHTMLSanitizer
from trac.wiki.api import parse_args

from genshi.input import HTMLParser, ParseError
from genshi.core import Stream, escape

from StringIO import StringIO

__all__ = ['InlineMacro']

class InlineMacro(WikiMacroBase):
    """Return raw, inline XHTML markup that has been validated and sanitized."""

    def expand_macro(self, formatter, macro, args):

        args, kw = parse_args(args)

        try:
            source = args.pop(0).strip()
        except NameError:
            return system_message('%s: Missing HTML source argument.' % macro)

        try:
            stream = Stream(HTMLParser(StringIO(source)))
            return (stream | TracHTMLSanitizer()).render('xhtml', encoding=None)
        except ParseError, e:
            self.env.log.warn(e)
            return system_message('%s: HTML parse error: %s.' % (macro, escape(e.msg)))
