#!/usr/bin/env python3

# This code will read in the input arguments from the command line to establish
# the Bayes Network. Then, the requested conditional probabilities will be retu-# rned to the user.


# PRIORS MUST BE PUT IN QUOTATIONS '-p P = .6'
import sys
import argparse
import ipdb
from sortedcontainers import SortedDict
breakP = ipdb.set_trace

class node():
	def __init__(self,name):
		# Name of Bayes Node
		self.name = name
		
		# Parent Connections of Bayes Node
		self.parents = []
	
		# Children Connections of Bayes Node
		self.children = []

		# Dictionary to hold probabilities
		self.p = {}

def main():
	# Read in the arguments to the program
	args = readIn()
	
	# Build the Bayes Network provided
	net = buildBayes()
	
	# add the necessary probabilities
	pnet = addProb(net)
	
	# Show the PRobability Chart:
	#breakP()
	showNet(pnet)

	# Find which argument was passed in:
        if args.p != None:
                parse = parser(args.p)
		print parse
		#breakP()
		doPrior(pnet,parse)

	# Show the updated Probability Chart:
	showNet(pnet)
	
	if args.j != None:
		parse = parser(args.j)
		#breakP()
		joint = doJoint(pnet,parse)
		print "Joint Probability is: ", joint
	
	elif args.m != None:
		parse = parser(args.m)
		#breakP()
		marg = doMarginal(pnet,parse)
		print "Marginal Probability is: ", marg
	
	elif args.g != None:
                # Parse the arguments from args
                parse = parser(args.g)
		breakP()
		cond = doConditional(net,parse)
		print "Conditional Probability is: ", cond	


 
def readIn():
	parser = argparse.ArgumentParser()
	parser.add_argument('-g', help="Conditional Probability")
	parser.add_argument('-j', help="Joint Probability")
	parser.add_argument('-m', help="Marginal Probability")
	parser.add_argument('-p', help="Prior")
	args = parser.parse_args()
	return args

def parser(args):
	no = False
	ans = []
	for i in args:
		if i.isupper():
			ans.append((i,"dist"))
		else:
			if i == '~':
				no = True
			else:
				if no == True:
					ans.append((i,"false"))
					no = False
				else:
					ans.append((i,"true"))
	return ans

def buildBayes():
	
	# Nodes of the Bayes Net
	P = node("Polution")
	S = node("Smoking")
	C = node("Cancer")
	X = node("Xray")
	D = node("Dyspnoea")
	
	# Structure of the Bayes Net
	P.children.append(C)
	S.children.append(C)
	C.parents.append(P)
	C.parents.append(S)
	C.children.append(X)
	C.children.append(D)
	X.parents.append(C)
	D.parents.append(C)

	# Store the nodes into a list
	net = [P, S, C, X, D]
	
	# Return Bayes Net construction
	return net

def addProb(net):
	
	# High Pollution (DENOTED P)
	net[0].p = {'pH': .1, 'pL': .9}
	
	# Smoker True (DENOTED S)
	net[1].p = {'sT': .3, 'sF': .7}
	
	# Cancer Cases (DENOTED AS COMBINATIONS OF P, p, S, s)
	net[2].p = {'CpHsF':.02, 'CpHsT':.05, 'CpLsF':.001,'CpLsT':.03}
	
	# Xray IF CANCER (T = C, F = c)
	net[3].p = {'XcT':.9, 'XcF':.2}
	
	# Dyspnoea IF CANCER (T = C, F = c)
	net[4].p = {'DcT':.65,'DcF':.3}

	return net


def doPrior(net,args):
	# WHICH RANDOM VARIABLE
	var = args[0][0]
	
	# WHICH RANDOM VARIABLE CONDITON
	yes_or_no = args[0][1]
	
	# WHAT NUMBER IS REPLACING IT
	# IF ARGS = 4 changing by a tenth
	# IF ARGS = 5 changing by a hundredth
	if len(args) == 4:
		num = float(args[-2][0] + args[-1][0])
	else:
		num = float(args[-3][0] + args[-2][0] + args[-1][0])
	if var == 'p':
		if yes_or_no == 'true':
			net[0].p['pL'] = num
			net[0].p['pH'] = 1-num
		else:
			net[0].p['pH'] = num
			net[0].p['pL'] = 1-num
	elif var == 's':
		if yes_or_no == 'true':
			net[1].p['sF'] = num
			net[1].p['sT'] = 1-num
		else:
			net[1].p['sT'] = num 
			net[1].p['sF'] = 1-num
	else:
		raise Exception("CAN ONLY SET PRIORS OF POLLUTION AND SMOKING")

def doMarginal(net,argies):
	prob = 0
	for i in argies:
		# First argument Variable
		var = i[0]
		# First argument state
		state = i[1]
		# Base Cases for Marginal Recursion
		if var == 'p':
			if state == 'true':
				prob += net[0].p['pL']
			else:
				prob += net[0].p['pH']
		if var == 's':
			if state == 'true':
				prob += net[1].p['sT']
			else:
				prob += net[1].p['sF']
		if var == 'c':
			pars = net[2].parents
			a = SortedDict(net[2].p)
			b = SortedDict(pars[0].p)
			c = SortedDict(pars[1].p)
			# MARGINAL LOGIC
			if state == 'true':
				for combos in a.keys():
					for combo1 in b.keys():
						for combo2 in c.keys():
							if combo1 in combos and combo2 in combos:
								prob += net[2].p[combos]*pars[0].p[combo1]*pars[1].p[combo2]
			elif state == 'false':
				prob = 1 - doMarginal(net,[('c', 'true')])
			
			# CONDITIONALS FROM CLASS 
			elif state == 'sT':
				for combos in a.keys():
                                        for combo1 in b.keys():
                                                for combo2 in c.keys():
                                                        if combo2 == 'sT' and combo1 in combos and combo2 in combos:
                                                                breakP()
								prob += net[2].p[combos]*pars[0].p[combo1]*pars[1].p[combo2]	
			
			elif state == 'sF':
				for combos in a.keys():
                                        for combo1 in b.keys():
                                                for combo2 in c.keys():
                                                        if combo2 == 'sF' and combo1 in combos and combo2 in combos:
                                                                breakP()
								prob += net[2].p[combos]*pars[0].p[combo1]*pars[1].p[combo2]	
			elif state == 'pH':
				for combos in a.keys():
                                        for combo1 in b.keys():
                                                for combo2 in c.keys():
                                                        if combo1 == 'pH' and combo1 in combos and combo2 in combos:
                                                                breakP()
								prob += net[2].p[combos]*pars[0].p[combo1]*pars[1].p[combo2]	
			
			elif state == 'pL':
				for combos in a.keys():
                                        for combo1 in b.keys():
                                                for combo2 in c.keys():
                                                        if combo1 == 'pL' and combo1 in combos and combo2 in combos:
                                                                breakP()
								prob += net[2].p[combos]*pars[0].p[combo1]*pars[1].p[combo2]	
			else:
				raise Exception('CANCER CANT BE DETERMINED FROM XRAY OR DYSPNOEA BECAUSE THEY DEPEND ON CANCER OUTPUT')
		if var == 'x':
			pars = net[3].parents
			a = SortedDict(net[3].p)
			b = SortedDict(pars[0].p)
			if state == 'true':
				for combos in a.keys():
					for combo1 in b.keys():
						if combos == 'XcT':
							prob += net[3].p[combos]*pars[0].p[combo1]
	

			#if state == 'true':
			#	prob += net[2].p['CpHsT']*net[0].['pH']*net[1].['sT']
			#	prob += net[2].p['CpLsT']*net[0].['pL']*net[1].['sT']
			#	prob += net[2].p['Cp


	return prob



def doConditional(net,argies):
	prob = 0
	var = []
	first = ''
	state = []
	count = 0
	conditions = []
	offon = []
	for i in argies:
		if count == 0:
			first = i[count]
		var.append(i[0])
		state.append(i[1])
		if var[count] == '|':
			index = count
			conds = len(argies) - index - 1
		count += 1
	for a in range(conds):
		conditions += var[-a-1]
		offon.append(state[-a-1])
	breakP()
	if first == ['c']:
		if conditions == ['p']:
			if offon == ['false']:
				prob_candpH = doMarginal(net,[('c','pH')])
				prob_pH = doMarginal(net,[('p','false')])
				prob = prob_candpH/prob_pH
			if offon == ['true']:
				prob_candpL = doMarginal(net,[('c','pL')])
				prob_pL = doMarginal(net,[('p','true')])
				prob = prob_candpL/prob_pL
		if conditions == ['s']:
			if offon == ['true']: 
				prob_candsT = doMarginal(net,[('c','sT')])
				prob_sT = doMarginal(net,[('s','true')])
				prob = prob_candsT/prob_sT
			if offon ==['false']:
				prob_candsF = doMarginal(net,[('c','sF')])
				prob_sF = doMarginal(net,[('s','false')])
				prob = prob_candsF/prob_sF
	if first == ['s']:
		if conditions == ['x']:
			if offon == ['true']:
				prob_sandxT = doMarginal(net,[('x','sT')])
				prob_s = doMarginal(net,[('s','true')])
				prob = prob_sandxT/prob_s
			if offon == ['false']:
				prob_sandxF = doMarginal(net,[('x','sF')])
				prob_s = doMarginal(net,[('s','false')])
				prob = prob_sandxT/prob_s
				
				
	return prob

def doJoint(net,argies):
	prob = 1
	for i in argies:
		var = i[0]
		state = i[1]
		prob = prob*doMarginal(net,[(var,state)])
	return prob
			


def showNet(net):
	for i in net:
		print "Probabilities for:", i.name
		for j in i.p.keys():
			print j, " = ", i.p[j]

if __name__ == '__main__':
    sys.exit(main())


# Graph of nodes
# Can hold: name, parent list, child list, and probabilities

# Description of Dictionary
# Each circle is a key in the dictionary
# This key has a list of probabilities
