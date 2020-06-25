# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:46:11 2020

@author: qtckp
"""

import io
import re
import regex

with io.open('vocab3000_3.txt','r', encoding='utf-8') as f:
    lines = f.readlines()


lines = [l.strip() for l in lines]

lines = [l for l in lines if len(l)>0]

lines = [l for l in lines if not l.startswith('T&P') and not l.isdigit()]




with io.open('vocab3000_3_better.txt','w', encoding='utf-8') as f:
    for line in lines:
        f.write(line+'\n')

for i in range(len(lines)):
    if lines[i].startswith('('):
        lines[i-1]+=lines[i]
        lines.pop(i)



f = open('vocab3000_3_better.txt','r')
tmp = []
for line in lines:
    if re.match(r"\d+\..*", line):
        print(line)
        f.close()
        f = io.open(f'{line}.tsv','w', encoding='utf-8')
        f.write("Russian\tPronouncing\tFarsi\n")
        tmp=[]
    else:
        tmp.append(line)
    
    if len(tmp)==3:
        #if regex.match('\p{IsCyrillic}',tmp[0]):# and regex.match(r"^[\u0600-\u06FF\s]*",tmp[2][:-1]) :
        tmp[2]=tmp[2][::-1]
        f.write('\t'.join(tmp)+'\n')
        #else:
        #    print(f'\t\t\t {tmp}')
            
        tmp=[]
    
f.close()






