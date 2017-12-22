#!/usr/bin/python

from subprocess import call
import time

EXT = [".aux", ".bbl", ".blg", \
 ".idx", ".lof", ".log", \
".lot", ".nlo", ".out", ".toc"]


def clean(file_name):
  for extension in EXT:
    call(["rm", "./" + file_name + extension])


def build_pdf(name, times=1, clean_up_before=True, clean_up_after=True):
  if clean_up_before:
    clean(name)

  for counter in range(0, times):
    call(["pdflatex", "./" + name + ".tex"])
    time.sleep(2)
    call(["bibtex", "./" + name ])
    time.sleep(2)
    call(["pdflatex", "./" + name + ".tex"])
    time.sleep(2)
    call(["pdflatex", "./" + name + ".tex"])

  if clean_up_after:
    clean(name)

#building
build_pdf("thesis3")


