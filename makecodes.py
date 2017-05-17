from __future__ import print_function
import sys
import numpy
import hashlib
import time

seed = time.clock()




if len(sys.argv) < 4:
    print("""Usage:  {} classlist.txt filename.tex filename.tsv
    """.format(sys.argv[0]))
    sys.exit(1)

cls = open(sys.argv[1], "r")
tex = open(sys.argv[2], "w")
tsv = open(sys.argv[3], "w")

tex.write("""\\pdfoutput=1
\\documentclass[extrafontsizes,36pt,oneside,letterpaper]{memoir}
\\usepackage{microtype}
\\usepackage{tikz}
\\usepackage[margin=1in]{geometry}
\\pagestyle{empty}
\\begin{document}
\\vspace{2in}
\\begin{center}

\\newcommand{\\A}[1]{%
   \\begin{tikzpicture}
     \\node[draw,circle,inner sep=1pt] {#1};
   \\end{tikzpicture}}
\\newcommand{\\E}[1]{%
   \\begin{tikzpicture}
     \\node[draw,rectangle, inner sep=5pt] {#1};
   \\end{tikzpicture}}
""")

tsv.write("Name\tAuthorCode\tRefereeCode\n")

codes = []

for name in cls:
    name = name.strip()
    nameb = bytes(name, 'utf-8')
    myhash = numpy.fromstring(hashlib.sha512(nameb).digest(), dtype='uint16')
    autcode = str(myhash[0]).zfill(5)
    refcode = str(myhash[-1]).zfill(5)[1:]
    tex.write("{\\tiny \\today }\\\\\n")
    tex.write("{}\\\\\n".format(name))
    tex.write("\\vspace{2in}\n")
    tex.write("{\\large Author Code:\\hfill")
    for c in autcode:
        tex.write("\\A{}".format(c))
    tex.write("}\\vspace{2in}\n")
    tex.write("{\\normalsize Keep this page.  You need it to submit your grades!}\n")
    tex.write("\\vfill\n")
    tex.write("{\\normalsize Referee Code:\\hfill")
    for c in refcode:
        tex.write("\\E{}".format(c))
    tex.write("}\\newpage\n")
    tsv.write("{}\t{}\t{}\n".format(name, autcode, refcode))
    codes.append(autcode)
    codes.append(refcode)

tex.write("\\end{center}\\end{document}")
tex.close()
tsv.close()
cls.close()

assert len(set(codes)) == 2*len(cls), "DUPLICATE FOUND!  RE-RUN!"
