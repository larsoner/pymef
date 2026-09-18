#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 12:49:21 2017

setup.py file for pymef3 library

Ing.,Mgr. (MSc.) Jan Cimbálník
Biomedical engineering
International Clinical Research Center
St. Anne's University Hospital in Brno
Czech Republic
&
Mayo systems electrophysiology lab
Mayo Clinic
200 1st St SW
Rochester, MN
United States
"""

import sys

from setuptools import setup, Extension
import numpy

extra_compile_args = ["-O3"]
if sys.platform != "win32":
    # meflib's si1 type is plain char but holds signed values (e.g., RED
    # compression byte differences, encryption levels), so char must be signed.
    # It is by default on x86 and Apple arm64, but not on Linux aarch64.
    extra_compile_args.append("-fsigned-char")

# the c extension module
MEF_FILE_EXT = Extension(
    "pymef.mef_file.pymef3_file",
    ["pymef/mef_file/pymef3_file.c"],
    include_dirs=[
        numpy.get_include(),
        "meflib/meflib",
    ],
    extra_compile_args=extra_compile_args,
)

setup(
    name="pymef",
    zip_safe=False,
    packages=["pymef", "pymef.mef_file"],
    ext_modules=[MEF_FILE_EXT],
)