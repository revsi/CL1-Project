#!/usr/bin/python
import ast
import sys, getopt, os, re
import subprocess
from pruning import *
def foroneline(strin,outfile):
	target = open(outfile,'a') 
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
		#datavalues = ['((', 'NP', ['<fs', ["af='snAna", 'n', 'm', 'sg', '3', 'o', '0_se', "0'"], "head='snAna'", "vpos='vib1_2'", "name='NP10'", "drel='k2:VGF2'>", '', '']]
	#Ldatavalues os list of all  such datavalues lines


	#filetering all VGFs
	verbs=[]
	cases=[]
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
		case=[]
	#print str(i[2])
		if "drel='k" in str(i[2]):
			while i[2][-1]=='':
				i[2].pop()
			#print str(i[2][2].strip("head='").strip("'"))
			#print i[2][2] + "into"
			for j in i[2]:
				if(j[0]=='h'):
					b=j.strip("head=").strip("'")
					if(len(b)>=2):
						if(b[-1].isdigit()==True and b[-2].isdigit()==False):
							b = b[:-1]
					case.append(b)#0 is noun 
				#print i[2][2].strip("head=").strip("'")
			#0 is noun
			#print i[2][2].strip("head=").strip("'")
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
	cases = sorted(cases, key=lambda case:case[1][2])   #to conclude that k7_p comes before k7_t always
	for i in cases:
		for j in verbs:
			if j[0]==i[2]:
				j.append([i[0],i[1]])
		
	for i in verbs:
		target.writelines([str(i),"\n"])
			
def process(filename,out):
    fo = open(filename).read()
    outfile = out +'/verbframes'
    sentences=fo.split("<Sentence id='1'>")
    for t in sentences:
        foroneline(t,outfile)
    pruning(outfile,out)

