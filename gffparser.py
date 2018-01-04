#!/usr/bin/env python3
 
import argparse
import re
 
parser = argparse.ArgumentParser("GFF3 file exporter")
parser.add_argument("--source_gff")
parser.add_argument("--type")
parser.add_argument("--attribute")
parser.add_argument("--value")
arg = parser.parse_args()
 
sq = arg.attribute + "=" + arg.value
fswtch = False
mswtch = False
fterm = ''
sp = ''
ep = ''
rc = ''
chl = 60
mcheck = 0
 
ifl = open(arg.source_gff)
 
for line in ifl:
 ps = re.search(sq, line)
 ts = re.search(arg.type, line)
 if ps and ts:
  fswtch = True
  data = line.split()
  fterm = ">"+ data[0]
  sp = int(data[3])
  ep = int(data[4])
  rc = data[6]
  rterm = re.escape(fterm)+"[\n](.*[\n])+>"
  fs = re.search(rterm, ifl.read()).group()
  fs = re.sub(r">.*[\n]", "", fs)
  fs = re.sub(r"\n","", fs)
  fs = re.sub(r">","", fs)
  i = sp
  print(">"+ arg.type + ":" + arg.attribute + ":" + arg.value)
  if rc == "+":
   while i < ep:
    if ep-i >= 60:
     print(fs[i:i+60])
    else:
     print(fs[i:ep])
    i += 60
  else:
   fs = fs[::-1]
   fs = fs.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
   fs = fs.upper()
   while i < ep:
    if ep-i >= 60:
     print(fs[i:i+60])
    else:
     print(fs[i:ep])
    i += 60
 
if fswtch == False:
 print("Query not found, please try again.")
