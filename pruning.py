#!/usr/bin/python
import ast
def pruning(inp,out):
    f_read = open(inp, "r")
    lines = [ast.literal_eval(line) for line in f_read if line.strip()]
    f_read.close()
    lines.sort(key=lambda line: len(line))
    f_write = open(inp,'w')
    for line in lines:
        f_write.write(str(line)+"\n")
    process(lines,out)

def process(lines,out):
    for line1 in lines:
        for line2 in lines:
            if len(line2)!=len(line1):
                continue
            for i in range(len(line1)-3):
                if line1[i+3][1]==line2[i+3][1]:
                    print line1[i+3][1]

        



pruning("/home/rajat/academics/CL1/project/output/verbframes","/home/rajat/academics/CL1/project/output/")



