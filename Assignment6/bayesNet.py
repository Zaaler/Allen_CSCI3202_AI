#!/usr/bin/env python3

# This code will read in the input arguments from the command line to establish
# the Bayes Network. Then, the requested conditional probabilities will be retu-# rned to the user.


# PRIORS MUST BE PUT IN QUOTATIONS '-p P = .6'
import sys
import argparse
import ipdb
breakP = ipdb.set_trace

class Node():
	def __init__(self,name,prob):
		self.name = name
		self.parents = []
		self.children = []
		self.p = prob

def main():
	# Read in the arguments to the program
	args = readIn()
	
	# Build the Bayes Network provided
	net = buildBayes()
	
	
	# Find which argument was passed in:
	if args.g != None:
		print args.g
	
	elif args.j != None:
		print args.j
	
	elif args.m != None:
		print args.m
	
	elif args.p != None:
		print args.p
		if args.p[0] == P
			snum = args[-2] + args[-1]
			num = float(snum)
			net['P'].p = num
		
	 
def readIn():
	parser = argparse.ArgumentParser()
	parser.add_argument('-g', help="Conditional Probability")
	parser.add_argument('-j', help="Joint Probability")
	parser.add_argument('-m', help="Marginal Probability")
	parser.add_argument('-p', help="Prior")
	args = parser.parse_args()
	return args

def buildBayes():
	net = dict()
	# High Pollution (DENOTED P)
	A1 = Node('P', .1)
	# Smoker True (DENOTED S)
	A2 = Node('S', .3)
	# Cancer Cases (DENOTED AS COMBINATIONS OF P, p, S, s)
	A3 = Node('CPS', .05)
	A3.parents.extend(('P','S'))
	A4 = Node('CPs', .02)
	A4.parents.extend(('P','S'))
	A5 = Node('CpS', .03)
	A5.parents.extend(('P','S'))
	A6 = Node('Cps', .001)
	A6.parents.extend(('P','S'))
	# Xray IF CANCER (T = C, F = c)
	A7 = Node('XC', .9)
	A5.parents.append('C')
	A8 = Node('Xc', .2)
	A5.parents.append('C')
	
	# Dyspnoea IF CANCER (T = C, F = c)
	A9 = Node('DC', .65)
	A5.parents.append('C')
	
	A10 = Node('Dc', .3)
	A5.parents.append('C')
	

	breakP()
	# Constructing the Dictionary
	net = {A1.name: A1, A2.name: A2, A3.name: A3, A4.name: A4, A5.name: A5, A6.name: A6, A7.name: A7, A8.name: A8, A9.name: A9,A10.name: A10}


if __name__ == '__main__':
    sys.exit(main())


# Graph of nodes
# Can hold: name, parent list, child list, and probabilities

# Description of Dictionary
# Each circle is a key in the dictionary
# This key has a list of probabilities
