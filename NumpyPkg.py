__author__ = 'nehaavishwa'
import pkgutil as pu
import pydoc as pd
import matplotlib as mp
import scipy as sci
import numpy as np
import sys


print("numpy", np.__version__)
print("matplotlib", mp.__version__)
print("scipy", sci.__version__)

def clean(astr):
      s = astr
      # remove multiple spaces
      s = ' '.join(s.split())
      s = s.replace('=','')
      return s

def print_desc(prefix, pkg_path):
    for pkg in pu.iter_modules(pkg_path):
        name = prefix+"."+pkg[1]

        if (pkg[2] == True):
            try:
                print(pd.plain(pd.render_doc(name)))
                docstr = pd.plain(pd.render_doc(name))
                docstr = clean(docstr)
                start = docstr.find("DESCRIPTION")
                docstr = docstr[start: start + 140]
                print(name, docstr)
            except:
                print("UnexpectedError", sys.exc_info()[0])
                continue


#print_desc("numpy", np.__path__)
print_desc("scipy", sci.__path__)