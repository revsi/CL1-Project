#!/usr/bin/python
import ast
def sorting(inp, out):
    A=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    outfile = out +'/pruned'
    f_read = open(inp, "r")
    for line in f_read:
        line = ast.literal_eval(line)
        print str(line) + " : "+str(len(line))



    #contents = f.readlines()
    #contents.insert(index, value)
    #f_write = open(out, "w")
    #contents = "".join(contents)
    #f_write.write(contents)
    #f_read.close()
    #f_write.close()

sorting("/home/rajat/academics/CL1/project/corpus/test/verbframes", "/home/rajat/academics/CL1/project/output/")