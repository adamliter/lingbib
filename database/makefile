#
# Makefile for Lingbib database generation
#
# To generate the end-user database, run `make` from the directory containing
# the makefile.
#
# The generated files should not be under version control.
# To clean up all generated files, run `make clean`.
#
# If you want to keep the new generated database, run `make release`.
# You should only do this after checking the results of a regular `make` run.
#

SCRIPT_DIR = ../scripts

SRC_DIR = src
SRC_FILE = ${SRC_DIR}/database.yaml
# SRC_STRINGS = ${SRC_DIR}/strings_*.bib
# SRC_METADATA = ${SRC_DIR}/metadata_*.bib
# SRC_ENTRIES = ${SRC_DIR}/entries.bib
# SRC_ALL = ${SRC_STRINGS} ${SRC_METADATA} ${SRC_ENTRIES}

OUT_DIR = out
OUT_FILE = ${OUT_DIR}/lingbib.biblatex.bib

RELEASE_DIR = ../release


all: $(OUT_FILE)

$(OUT_FILE): $(SRC_FILE) $(OUT_DIR)
	# convert source file to a usable Biblatex BIB file
	$(SCRIPT_DIR)/yaml2bib.py $(SRC_FILE) $(OUT_FILE)

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

release: $(OUT_FILE) $(RELEASE_DIR)
	cp $(OUT_FILE) $(RELEASE_DIR)

$(RELEASE_DIR):
	mkdir -p $(RELEASE_DIR)

.PHONY: clean
clean:
	rm -rf $(OUT_DIR)
