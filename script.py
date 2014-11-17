#!/usr/bin/python

import sys, getopt, os, re
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
    
    # abs_in is the absolute path of input file
    # abs_out is the absolute path of output folder
    abs_out = os.path.abspath(os.path.dirname(outputdirectory))
    abs_in = os.path.realpath(os.path.join(inputfile))
    cleanup()
    #parser(abs_in, abs_out)
    cleanup()
    get_vgfs("/home/rajat/academics/CL1/project/output/output")


def parser(inp,out):
    outfile = out +'/output'
    openfile = open(inp,'r') 
    for line in openfile:
    	line = line.rstrip('\n')
    	command1 = "echo \"" + line + "\" " + "> temp" 
    	os.system(command1)
    	command2 = "shallow_parser_hin temp > temp2 "
    	os.system(command2)
    	command3 = "sh $setu/bin/sl/fullparser_hin/fullparser_hin_run.sh temp2 >> " +outfile
    	os.system(command3)
    os.system("rm temp2 temp && rm -r OUTPUT.tmp")
    get_vgfs(outfile)



def get_vgfs(inp):
	fo = open(inp, "r")
	strin = fo.read(1000000)
	lines=re.split('\n',strin)
	fl=0
	head=0
	group=[]
	answer=[]
	typ={}
	form={}
	feat={}
	Ldatavalues=[]
	for i in lines:
		data =re.split('\t',i)
		if(data.__len__()==1):
			data.append('')
			data.append('')
			data.append('')
		if(data.__len__()==2):
			data.append('')
			data.append('')
		if(data.__len__()==3):
			data.append('')
		datavalues=[]
		datavalues.append(data[1])
		datavalues.append(data[2])
		datavalues.append(re.split(' ',data[3]))
		for j in xrange(8):
			if ((datavalues[2].__len__())==j):
				for k in xrange(8-j):
					datavalues[2].append("")	
		datavalues[2][1]=re.split(',',datavalues[2][1])
		Ldatavalues.append(datavalues)
		#print datavalues
		#datavalues = ['((', 'NP', ['<fs', ["af='snAna", 'n', 'm', 'sg', '3', 'o', '0_se', "0'"], "head='snAna'", "vpos='vib1_2'", "name='NP10'", "drel='k2:VGF2'>", '', '']]
	#Ldatavalues os list of all  such datavalues lines
	#filetering all VGFs
	verbs=[]
	count=0
	for i in Ldatavalues:
		verb=[]
		if i[1]=="VGF":
			count=count+1
			verb.append(('VGF' + str(count)).strip('1'))
			verb.append(i[2][1][0].strip('"af=').strip("'"))#0 is the verb root
			verb.append(i[2][1][6])#6 is the TAM
			#print verb
			verbs.append(verb)
	#filtering all Kartas
	cases=[]
	for i in Ldatavalues:
		case=[]
		#print str(i[2])
		if "drel='k" in str(i[2]):
			while i[2][-1]=='':
				i[2].pop()
			case.append(i[2][1][0].strip('"af=').strip("'"))#0 is noun root
			if(i[2][1][6]==''):
				i[2][1][6]='0'
			string=i[2][-1]
			string=string.strip('"drel=')
			string=string.strip('>"')
			karak=string.split(':')[0].strip("'")
			verbm=string.split(':')[1].strip("'")
			case.append(karak + '_' + i[2][1][6])#6 is vibhankti
			case.append(verbm)
			#print case
			cases.append(case)		
	cases = sorted(cases, key=lambda case:case[1][1])   # sort by order of kartas, k1,k2,k3,k4,k5,k7
	cases = sorted(cases, key=lambda case:case[1][2])   #to conclude that k7_p comes before k7_t
	for i in cases:
		for j in verbs:
			if j[0]==i[2]:
				j.append([i[0],i[1]])
			
	for i in verbs:
		print i

def cleanup():
    prepend1 = '.txt'
    prepend2 = '.log'
    prepend3 = '.ssf'
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    for file_to_delete in [file for file in os.listdir(PROJECT_ROOT) if (file.endswith(prepend1) or file.endswith(prepend2) or file.endswith(prepend3))]:
        os.remove(file_to_delete)


if __name__ == "__main__":
   main(sys.argv[1:])
