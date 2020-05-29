.PHONY: all clean
.SUFFIXES: .bs .html

all: index.html questionnaire.markdown

clean:
	rm -f index.html *~

.bs.html: Makefile
	bikeshed --die-on=warning spec $< $@

questionnaire.markdown: index.bs
	./generate-markdown.py < $< > $@
