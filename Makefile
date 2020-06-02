specs   = $(patsubst %.bs,build/%.html,$(wildcard *.bs))

.PHONY: all clean pristine
.SUFFIXES: .bs .html

all: build $(specs) questionnaire.markdown

clean:
	rm -f $(specs) questionnaire.markdown *~

pristine: clean
	rm -rf build

build:
	mkdir -p build

build/%.html: %.bs Makefile
	bikeshed --die-on=warning spec $< $@

questionnaire.markdown: index.bs generate-markdown.py
	./generate-markdown.py < $< > $@
