#!/usr/bin/env python3

import sys
import collections
import ipdb
breakP = ipdb.set_trace

def main():
	fn = 'typos20.data'
	(s, e) = readData(fn)
	p_emission = analyze_se(s,e)
	o_p_emit = collections.OrderedDict(sorted(p_emission.items()))
	sum_ps = printDict(o_p_emit)
	printSumP(sum_ps)
	transP = analyze_s2s(s,e)
	o_transP = collections.OrderedDict(sorted(transP.items()))
	sum_ps = printDict(o_transP)
	printSumP(sum_ps)

def readData(fn):
	filename = open(fn,'r')
    	state = []
	evidence = []
	for i in filename:
		state.append(i[0])
		evidence.append(i[2])
	return state, evidence

def analyze_se(s,e):
	p_ex = {}
	#total = 0
	count_e = 0
	count_s = 0
	chars = 'abcdefghijklmnopqrstuvwxyz'
	for k in range(0,len(chars)):
		# Choose evidence observed
		given = chars[k]
		# Now look at what was acutually typed
		for i in range(0,len(chars)):
			# CORRECT CHARACTER
			evidence = chars[i]
			# SEE HOW MANY TIMES THIS EVENT ARISES IN TEXT FILE
			#print evidence+given
			for j in range(0,len(s)):
				# CHECK THE CURRENT CORRECT CHARACTER 
				# DOES STATE MATCH THE STATE UNDER EXAMINATION
				if s[j] == given:
					#breakP()
					# RECORD THAT STATE MATCHES GIVEN
					count_s += 1
					# DOES THIS ERROR MATCH EVIDENCE
					if e[j] == evidence:
						if count_e == 0:
							pass
							#print e[j] + s[j]
						# THIS EVIDENCE GIVEN COMBO OCCURRED
						count_e += 1
			#total = total + count_e
			#if total == count_s:
			#	total = 0
			#	print "ITS GOOD"
			p_ex[given+evidence] = float(1+count_e)/(26+count_s)
			#breakP()
			print "P(", evidence, "|", given, ") =", float(1+count_e)/(26+count_s)
			count_e = 0
			count_s = 0
	return p_ex	

def analyze_s2s(s,e):
	ss = {}
	count_ss = 0
        count_s = 0
        chars = '_abcdefghijklmnopqrstuvwxyz'
        for k in range(0,len(chars)):
                # Choose evidence observed
                state1 = chars[k]
                # Now look at what was acutually typed
                for i in range(0,len(chars)):
                        # CORRECT CHARACTER
                        state2 = chars[i]
                        # SEE HOW MANY TIMES THIS EVENT ARISES IN TEXT FILE
                        for j in range(0,len(s)-1):
                                # CHECK THE CURRENT CORRECT CHARACTER 
                                # DOES STATE MATCH THE STATE UNDER EXAMINATION
                                if state1 == s[j]:
				#	if state1 == 'z'
                                        # RECORD THAT STATE MATCHES GIVEN
                                        count_s += 1
                                        # DOES THIS ERROR MATCH EVIDENCE
                                        if state2 == s[j+1]:
                                #                breakP()
						# THIS EVIDENCE GIVEN COMBO OCCURRED
                                                count_ss += 1
        
                        ss[state1+state2] = float(1+count_ss)/(27+count_s)
			print "P(", state2, "|", state1, ") =", float(1+count_ss)/(27+count_s)
                        #print evidence, given
                        count_ss = 0
                        count_s = 0

	return ss

def printSumP(sump):
	chars = 'abcdefghijklmnopqrstuvwxyz'
	if len(sump) == 27:
		chars = '_abcdefghijklmnopqrstuvwxyz'
	for i in range(0,len(chars)):
		print 'P(', chars[i], ') =', sump[i]

def printDict(dictionary):
	#breakP()
	sum_ps = []
	total = 0
	count = 0
	counter = 0
	letters = 26
	chars = 'abcdefghijklmnopqrstuvwxyz'
	if len(dictionary) == 729:
		chars = '_abcdefghijklmnopqrstuvwxyz'
		letters = 27
	#for j in range(0,len(chars)):
	#	print '    ',chars[j],'  ',
	#print
	for i in dictionary:
		count += 1
		if count % letters == 1:
	#		print  chars[counter],
			counter += 1
	#	print " %.3f " % dictionary[i]," ",
		total += dictionary[i]
		if count % letters == 0:
			sum_ps.append(total)
			total = 0
	#		print
	#breakP()
	return sum_ps

if __name__ == '__main__':
    	sys.exit(main())

