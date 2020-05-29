#!/usr/bin/env python3

import sys

class MarkdownGenerator:
    def __init__(self):
        self.in_question = False
        self.first_line_in_question = False
        self.prefix = ""

    def process_line(self, line, outfile):
        if self.in_question:
            if not line.startswith("  </h3>"):
                line = line.lstrip()
                if self.first_line_in_question:
                    self.prefix = "1. "
                    self.first_line_in_question = False
                print("%s%s" % (self.prefix, line), end='', file=outfile)
                self.prefix = "   "
            else:
                self.in_question = False
        elif line.startswith("  <h3 class=question id="):
            self.in_question = True
            self.first_line_in_question = True

    def generateMarkdown(self, infile=sys.stdin, outfile=sys.stdout):
        [self.process_line(line, outfile) for line in infile]

if __name__ == '__main__':
    MarkdownGenerator().generateMarkdown()
