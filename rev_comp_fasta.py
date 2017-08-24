#!/usr/bin/env python
#simple reverse complement script for use in UNIX

import sys

inFasta = sys.stdin.read()
header = ""
seqDat = ""

for line in inFasta:
 if line.find(">") > 0:
  header = line
 else:
  line = line.replace("\n", "")
  seqdat = seqdat + line

seqdat = seqdat[::-1]
seqdat = seqdat.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
seqdat = seqdat.upper()
l = len(seqdat)

print(header)
i = 0
while i < l:
 if l-i >= 60:
  print(seqdat[i:i+60]
 else:
  print(seqdat[i:l])
 i += 60