#!/usr/bin/python
import ast
from vectorise import *
def pruning(inp,out):
    f_read = open(inp, "r")
    lines = [ast.literal_eval(line) for line in f_read if line.strip()]
    f_read.close()
    lines.sort(key=lambda line: len(line)) #converting stored string into python list
    f_write = open(inp,'w')
    for line in lines:
        f_write.write(str(line)+"\n")
    outfile = out +'/prunedOutput'
    process_pruning(lines,outfile)

def process_pruning(lines,outfile):
    i=-1
    j=0
    target = open(outfile,'a') 
    while(i<len(lines)):
        i=i+1
        j=i
        if(i==len(lines)):
            break
        while(j<len(lines)):
            j=j+1
            if (j==len(lines)):
                break
            line1=lines[i]
            line2=lines[j]
            if len(line2)<len(line1):
                continue
            if len(line2)>len(line1):
                break
            nk=len(line1)
            flag=True
            if line1[1]==line2[1] and line1[2]==line2[2]:
                for k in xrange(3,nk):
                    if line1[k][1]==line2[k][1]:
                        flag=True
                    else:
                        flag=False
                        break
                if flag == True:
                    for k in xrange(3,nk):
                        if type(line1[k][0]) != list:
                            temp = line1[k][0]
                            new = [temp]
                            line1[k][0]=new
                        line1[k][0].append(line2[k][0]) #adding words of same verb,karakas
                        line1[k][0]=list(set(line1[k][0]))
                    del lines[j] # removing the verb frame after adding above
                    j=j-1


    lines.sort(key=lambda line:(line[1],line[2]))
    x=0
    for i in lines:
        if len(i)>3:
            x=x+1
            i[0]=x
            target.writelines([str(i),"\n"])
                            
        




