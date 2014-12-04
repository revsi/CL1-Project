#!/usr/bin/python
import ast
import gensim
import numpy
import mmap
import re
from scipy.spatial.distance import cosine
def vectorise(inp,out):
    f_read = open(inp, "r")
    lines = [ast.literal_eval(line) for line in f_read if line.strip()]
    f_read.close()
    outfile = out +'/vectoriseOutput'
    ################
    #word2vec model#
    ################
    modelfile = out + '/modelw2v2'
    model = ""
    model = gensim.models.Word2Vec.load_word2vec_format(modelfile, binary=True)
    process_vectorise(lines,outfile,model)

def process_vectorise(lines,outfile,model):
	target = open(outfile,'a')
	dummy = [0]*200
	for line in lines:
		nk=len(line)
		for k in xrange(3,nk):
				if type(line[k][0]) != list:
					word = line[k][0]
					try :
						line[k][0]=model[word]
					except Exception as e:
						line[k][0]=dummy
				else:
					temp=dummy
					n=len(line[k][0])
					for word in line[k][0]:
						try :
							temp = numpy.sum([temp,model[word]],axis=0)
						except Exception as e:
							temp = numpy.sum([temp,dummy],axis=0)
					line[k][0]=temp/n

	for i in lines:
		target.writelines([str(i),"\n"])

	#getTop20(lines,model)

def getTop20(lines,model):
	#cosine(numpy.array([1,1]), numpy.array([1,1]))
	n=len(model.index2word)
	count = 0
	for line in lines:
		nk=len(line)
		for k in xrange(3,nk):
			pass



