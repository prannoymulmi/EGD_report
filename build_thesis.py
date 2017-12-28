#!/usr/bin/python
# Copyright 

import os

EXT = [".atl", ".aux", ".bbl", ".blg", \
".fls", ".idx", ".ilg", ".lof", ".log", \
".lot", ".nlo", ".out", ".toc", ".fdb_latexmk", ".synctex(busy)"]


def clean(file_name):
  for extension in EXT:
        try:
          os.remove(file_name + extension)
        except Exception:
          #Error handling when the 
          print("error")  


def build_pdf(name, times=2, clean_up_before=True, clean_up_after=True):
  COMMANDS = ["pdflatex", "bibtex", "pdflatex", "pdflatex"]    
  if clean_up_before:
    clean(name)

  os.system("pdflatex " + name + ".tex")
  os.system("bibtex "  + name)
  for counter in range(0, times):
    os.system("pdflatex " + name + ".tex")

  if clean_up_after:
    clean(name)

#building
build_pdf("thesis3")


