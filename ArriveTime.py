import sys


i=0
s=''
list=[]
f=open("airline-2014.txt","r").readlines()
for line in f:
    
    line = line.strip()
    
    items = line.split(",")
    
    
    delay=0;
    
    if items[12]!="\"\"" and items[11]!=items[12]:
        crsHour=items[11][1:3]
        crsMin=items[11][3:5]
        depHour=items[12][1:3]
        depMin=items[12][3:5]
        delay=(int(depHour)-int(crsHour))*60+(int(depMin)-int(crsMin))
        if (delay<=0):
            #print '%s\t%s' %(items[1],delay)
            s=items[1]+'\t'+'1'
            list.append(s)
            i=i+1
       
       
    
list.sort();
file1 = open('ArriveTime.txt','w');
for j in range(0,i) :
#     print list[j];
    file1.writelines(list[j]);
    file1.write('\n')
file1.close();

