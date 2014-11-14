#!/usr/bin/python

import sys, getopt, os

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
    shallow_parser(abs_in, abs_out)

def shallow_parser(inp,out):
    import subprocess
    out = out +'/outputofshallowparser'
    subprocess.call(["shallow_parser_hin", inp, out])


if __name__ == "__main__":
   main(sys.argv[1:])