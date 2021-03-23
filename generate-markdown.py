#!/usr/bin/env python3

import sys

class MarkdownGenerator:
    def __init__(self):
        self.in_question = False
        self.first_line_in_question = False
        self.prefix = ""
        self.qnum = 0

    def process_line(self, line, outfile):
        if self.in_question:
            if not line.startswith("</h3>"):
                line = line.lstrip()
                if self.first_line_in_question:
                    self.qnum += 1
                    self.prefix = "> %02d. " % self.qnum
                    self.first_line_in_question = False
                print("%s%s" % (self.prefix, line), end='', file=outfile)
                self.prefix = ">     "
            else:
                self.in_question = False
        elif line.startswith("<h3 class=question id="):
            self.in_question = True
            self.first_line_in_question = True

    def generate_markdown(self, infile=sys.stdin, outfile=sys.stdout):
        print("""# [Self-Review Questionnaire: Security and Privacy](https://w3ctag.github.io/security-questionnaire/)

This questionnaire has [moved](https://w3ctag.github.io/security-questionnaire/).

For your convenience, a copy of the questionnaire's questions is quoted here in Markdown, so you can easily include your answers in an [explainer](https://github.com/w3ctag/w3ctag.github.io/blob/master/explainers.md).
""", file=outfile)
        [self.process_line(line, outfile) for line in infile]

if __name__ == '__main__':
    MarkdownGenerator().generate_markdown()
