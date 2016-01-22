import sys


i=0
s=''
list=[]
f=open("airline-2014.txt","r").readlines()
for line in f:
    
    line = line.strip()
    
    items = line.split(",")
    
    delay=0;
    
    
    
    if items[10]!="\"\"" and items[9]!=items[10]:
        crsHour=items[9][1:3]
        crsMin=items[9][3:5]
        depHour=items[10][1:3]
        depMin=items[10][3:5]
        delay=(int(depHour)-int(crsHour))*60+(int(depMin)-int(crsMin))
        if (delay>60):
            s=items[1]+'\t'+'1'
            list.append(s)
            i=i+1
            #print '%s\t%s' %(items[1],"1")
list.sort()
file1=open("PercentageDelay.txt","w")
for j in range(0,i):
    file1.writelines(list[j])
    file1.write('\n')
file1.close()
    
