#!/usr/bin/env python3
 
bad_entry = False
print("======================================")
print("************************")
print("* Reverse Complementer *")
print("*   By Omar Tibi V.1   *")
print("************************")
 
while bad_entry == False:
 seq = input("Please input a valid oligo sequence: ")
 l = len(seq)
 a = seq.count("A")
 t = seq.count("T")
 c = seq.count("C")
 g = seq.count("G")
 nl = a + t + c + g
 if l == nl: #Personally find it easier/simpler than regex
  oseq = seq[::-1]
  oseq = oseq.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
  oseq = oseq.upper()
  print("Reverse complement: " + oseq)
  print("Please enter the next oligo below.")
 else:
  bad_entry = True
  print("Invalid character in user input, please try again.")
  print("----------------------------------------------------")
