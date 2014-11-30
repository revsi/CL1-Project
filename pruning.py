#!/usr/bin/python
import ast
def sorting(inp,out):
    f_read = open(inp, "r")
    output = out + "out"
    lines = [ast.literal_eval(line) for line in f_read if line.strip()]
    f_read.close()
    lines.sort(key=lambda line: len(line))
    f_write = open(output,'w')
    for line in lines:
        f_write.write(str(line)+"\n")



#f = open("path_to_file", "r")
#contents = f.readlines()
#f.close()

#contents.insert(index, value)

#f = open("path_to_file", "w")
#contents = "".join(contents)
#f.write(contents)
#f.close()

sorting("/home/rajat/academics/CL1/project/corpus/test/verbframes","/home/rajat/academics/CL1/project/corpus/test/")