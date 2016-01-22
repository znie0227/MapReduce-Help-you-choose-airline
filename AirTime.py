import sys
import re
import os
i=0;
s='';
list=[];
f=open("airline-2014.txt","r").readlines()
for line in f:
    line=line.strip()
    items=line.split(",")
    if items[14]!="":
        s=items[1]+'\t'+items[14];
        list.append(s);
        i=i+1;
        
list.sort();
file1 = open('test.txt','w');
for j in range(0,i) :
    file1.writelines(list[j]);
    file1.write('\n')
file1.close();
