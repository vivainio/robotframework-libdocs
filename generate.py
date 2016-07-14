import robot.libdoc
import sys
import os
import subprocess

docdir = os.path.abspath("./doc")

def c(s):
    print ">", s
    os.system(s)

# or use "ipy" for ironpython

python_bin = "python"

def run(lib, outpath):
    c("ipy -m robot.libdoc %s %s" % (lib, outpath))

def gen_doc(lib):

    run(lib, r'%s\%s.html' % (docdir, lib))
    run(lib, r'%s\%s.xml' % (docdir, lib))

libs = [s.strip() for s in """\
BuiltIn
Collections
String
OperatingSystem
""".splitlines()]

for l in libs:
    gen_doc(l)