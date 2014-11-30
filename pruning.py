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
    for line in lines:
        l=len(line)-3
        



pruning("/home/rajat/academics/CL1/project/output/verbframes","/home/rajat/academics/CL1/project/output/")



