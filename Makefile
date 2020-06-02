specs   = $(patsubst %.bs,build/%.html,$(wildcard *.bs))

.PHONY: all clean
.SUFFIXES: .bs .html

all: build $(specs) questionnaire.markdown

clean:
	rm -rf build questionnaire.markdown *~

build:
	mkdir -p build

build/%.html: %.bs Makefile
	bikeshed --die-on=warning spec $< $@

questionnaire.markdown: index.bs generate-markdown.py
	./generate-markdown.py < $< > $@
