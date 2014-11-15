#!/usr/bin/python

import sys, getopt, os
import subprocess

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
    
    cleanup('.txt')
    cleanup('.log')
    
    #subprocess.call(["rm *.log"])
    #subprocess.call(["rm -rf OUTPUT.tmp"])


    # abs_in is the absolute path of input file
    # abs_out is the absolute path of output folder
    abs_out = os.path.abspath(os.path.dirname(outputdirectory))
    abs_in = os.path.realpath(os.path.join(inputfile))
    shallow_parser(abs_in, abs_out)

def shallow_parser(inp,out):
    outfile = out +'/outputofshallowparser'
    subprocess.call(["shallow_parser_hin", inp, outfile])
    full_parser(outfile,out)

def full_parser(inp,out):
    outfile = out +'/output_of_fullparser'
    command = "sh $setu/bin/sl/fullparser_hin/fullparser_hin_run.sh " + inp + " >> "
    command = command + outfile
    os.system(command)

def cleanup(prepend):
    prepend = str(prepend)
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    for file_to_delete in [file for file in os.listdir(PROJECT_ROOT) if file.endswith(prepend)]:
        os.remove(file_to_delete)

if __name__ == "__main__":
   main(sys.argv[1:])