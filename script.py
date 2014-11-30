#!/usr/bin/python

import sys, getopt, os, re
import subprocess
from verbframe import *

def main(argv):
    inputfile = ''
    outputdirectory = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print './script.py -i <inputfile> -o <outputdirectory>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print './script.py -i <inputfile> -o <outputdirectory>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputdirectory = arg
    
    # abs_in is the absolute path of input file
    # abs_out is the absolute path of output folder
    abs_out = os.path.abspath(os.path.dirname(outputdirectory))
    abs_in = os.path.realpath(os.path.join(inputfile))
    cleanup()
    parser(abs_in, abs_out)
    cleanup()
    #process_output("/home/rajat/academics/CL1/project/output/output",abs_out)


def parser(inp,out):
    outfile = out +'/fulloutput'
    shallowoutput = out + '/shallowoutput'
    openfile = open(inp,'r') 
    for line in openfile:
    	line = line.rstrip('\n')
        if len(line.split()) > 30:
            continue
        print "Number of word : " + str(len(line.split()))
    	command1 = "echo \"" + line + "\" " + "> temp" 
    	os.system(command1)
    	command2 = "shallow_parser_hin --out_encoding=wx temp > temp2 "
    	os.system(command2)
        command4 = "cat temp2 >> " + shallowoutput
        os.system(command4)
    	command3 = "sh $setu/bin/sl/fullparser_hin/fullparser_hin_run.sh temp2 >> " +outfile
    	os.system(command3)
    os.system("rm temp2 temp && rm -r OUTPUT.tmp")
    process_output(outfile,out)

def process_output(inp,out):
	process(inp,out)

def cleanup():
    prepend1 = '.txt'
    prepend2 = '.log'
    prepend3 = '.ssf'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    for file_to_delete in [file for file in os.listdir(PROJECT_ROOT) if (file.endswith(prepend1) or file.endswith(prepend2) or file.endswith(prepend3))]:
        os.remove(file_to_delete)


if __name__ == "__main__":
   main(sys.argv[1:])
