#!/usr/bin/python
import ast
import gensim
import numpy
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
	for line in lines:
		nk=len(line)
		for k in xrange(3,nk):
			if type(line[k][0]) != list:
				word = line[k][0]
				line[k][0]=model[word]
			else:
				temp=[0]*200
				for word in line[k][0]:
					temp = numpy.sum([temp,model[word]],axis=0)
				line[k][0]=temp

	for i in lines:
		target.writelines([str(i),"\n"])

def getTop20(lines):
	pass
#cosine_similarity = numpy.dot(model['spain'], model['france'])/(numpy.linalg.norm(model['spain'])* numpy.linalg.norm(model['france']))

vectorise("/home/rajat/academics/CL1/project/test/prunedOutput","/home/rajat/academics/CL1/project/test")



