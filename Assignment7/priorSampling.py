#!/bin/usr/env python3

import sys
import ipdb
breakP = ipdb.set_trace

def main():
	samples = [0.82,  0.56,   0.08,   0.81,   0.34,   0.22,   0.37,   0.99,   0.55,   0.61,   0.31,   0.66,   0.28,   1.00,   0.95,
	0.71,   0.14,   0.10,   1.00,   0.71,   0.10,   0.60,   0.64,   0.73,   0.39,   0.03,   0.99,   1.00,   0.97,   0.54,   0.8,
	0.97,   0.07,   0.69,   0.43,   0.29,   0.61,   0.03,   0.13,   0.14,   0.13,   0.40,   0.94,   0.19,   0.60,   0.68,   0.36,
	0.67,   0.12,   0.38,   0.42,   0.81,   0.00,   0.20,   0.85,   0.01,   0.55,   0.30,   0.30,   0.11,   0.83,   0.96,   0.41,
	0.65,   0.29,   0.40,   0.54,   0.23,   0.74,   0.65,   0.38,   0.41,   0.82,   0.08,   0.39,   0.97,   0.95,   0.01,   0.62,
	0.32,   0.56,   0.68,   0.32,   0.27,   0.77,   0.74,   0.79,   0.11,   0.29,   0.69,   0.99,   0.79,   0.21,   0.20,   0.43,
	0.81,   0.90,   0.00,   0.91,   0.01]
	
	print ""
	# Problem 1 - USING PRIOR SAMPLING
	print "PROBLEM #1 SOLUTIONS"
	print ""
	s_prob = priorSampling(samples)
	#print s_prob
	priorProb(s_prob)
	print ""
	# Problem 3 - Rejection Sampling
	print "PROBLEM #3 SOLUTIONS"
	print ""
	rejectPc(samples)
	rejectPc_r(samples)
	rejectPs_wg(samples)
	rejectPs_cwg(samples)
	print ""


def priorSampling(samples):
	results = []
	pointer = 0
	while pointer < len(samples):
		
		# CLOUDY DATA POINT
		point = samples[pointer]
		
		# CLOUDY IS TRUE
		if point < .5:
			cloud = True
	
			# SPRINKLER DATA POINT
			pointer += 1
			point = samples[pointer]

			# LOOK AT SPRINKLER
			if point < .1:
				sprinkler = True
			else:
				sprinkler = False

			# RAIN DATA POINT
			pointer += 1
			point = samples[pointer]
			
			# LOOK AT RAIN
			if point < .8:
				rain = True
			else:
				rain = False
			
			# WET GRASS DATA POINT
			pointer += 1
			point = samples[pointer]
			
			# LOOK AT WET GRASS 
			if rain and sprinkler:
				if point < .99:
					wetgrass = True
				else:
					wetgrass = False

			elif rain and (not sprinkler):
				if point < .9:
					wetgrass = True
				else:
					wetgrass = False

			elif (not rain) and sprinkler:
				if point < .9:
					wetgrass = True
				else:
					wetgrass = False

			elif (not rain) and (not rain):
				wetgrass = False
			
			# ITERATE DATA SAMPLE FOR NEXT ROUND
			pointer += 1
		else:
                	# CLOUDY IS FALSE
                        cloud = False

                        # SPRINKLER DATA POINT
                        pointer += 1
                        point = samples[pointer]

                        # LOOK AT SPRINKLER
                        if point < .5:
                                sprinkler = True
                        else:
                                sprinkler = False

                        # RAIN DATA POINT
                        pointer += 1
                        point = samples[pointer]

                        # LOOK AT RAIN
                        if point < .2:
                                rain = True
                        else:
                                rain = False

                        # WET GRASS DATA POINT
                        pointer += 1
                        point = samples[pointer]

                        # LOOK AT WET GRASS 
                        if rain and sprinkler:
                                if point < .99:
                                        wetgrass = True
                                else:
                                        wetgrass = False

                        elif rain and (not sprinkler):
                                if point < .9:
                                        wetgrass = True
                                else:
                                        wetgrass = False

                        elif (not rain) and sprinkler:
                                if point < .9:
                                        wetgrass = True
                                else:
                                        wetgrass = False

                        elif (not rain) and (not rain):
                                wetgrass = False

                        # ITERATE DATA SAMPLE FOR NEXT ROUND
                       	pointer += 1
		#breakP()
		results.append(([cloud, sprinkler, rain, wetgrass]))
	return results

def priorProb(results):
	# Different Probabilities
	c = 0
	s = 0
	r = 0
	wg = 0
	cr = 0
	rc = 0
	swg = 0
	wgc = 0
	wgcs = 0
	count = 0

	for i in results:
		# Cloudy True
		if i[0] == True:
			c += 1
			if i[2] == True:
				cr += 1
		if i[1] == True:
			s += 1
			if i[3] == True:
				swg += 1
		if i[2] == True:
			r += 1
			if i[0] == True:
				rc += 1
		if i[3] == True:
			wg += 1
			if i[0] == True:
				wgc += 1
				if i[1] == True:
					wgcs += 1
		count += 1
	
	# Print out results
	print "Probability Cloudy is True:", float(c)/count
	print "Probability Cloudy given Rain:", float(rc)/r
	print "Probability Sprinklers given Wet Grass:", float(swg)/wg
	print "Probability Sprinklers given Cloudy and Wet Grass:", float(wgcs)/wgc

def rejectPc(samples):
	c = 0
	cr = 0
	count = 0
	for i in samples:
		if i < .5:
			#print i
			c += 1
		count += 1
	print "Rejection Probability of Clouds:", float(c)/count

def rejectPc_r(samples):
	cr = 0
	r = 0
	count = 0
	i = 0
	while i < len(samples)-1:
		# CLOUDY TRUE
		if samples[i] < .5:
			i += 1
			# RAINY TRUE
			if samples[i] < .8:
				cr += 1
		# CLOUDY FALSE only care about the times that cloudy is true given rain true
		else:
			i += 1
			if samples[i] < .2:
				r += 1
	count = cr + r		
	print "Rejection Probabilty of Clouds given Rain:", float(cr)/count

def rejectPs_wg(samples):
	swg = 0
	wg = 0
        # Need to sample all 4 fields for wg
        results = priorSampling(samples)
        i = 0
        while i < len(results):
                # WETGRASS TRUE
                if results[i][3] == True:
                        wg += 1
                        #print results[i]
                        if results[i][1] == True:
                                swg += 1
                i += 1
        #print scwg
        #print cwg
        print "Rejection Probability of Sprinklers given Wet Grass:", float(swg)/wg




def rejectPs_cwg(samples):
	cwg = 0
	scwg = 0
	# Need to sample all 4 fields for wg
	results = priorSampling(samples)	
	# Place to hold appropriate samples
	i = 0
	while i < len(results):
		# CLOUDS OR WETGRASS TRUE
		if (results[i][0] == True) and (results[i][3] == True):
			cwg += 1
			#print results[i]
			if results[i][1] == True:
				scwg += 1
		i += 1
	#print scwg
	#print cwg
	print "Rejection Probability of Sprinklers given Cloudy and Wet Grass:", float(scwg)/cwg





if __name__ == '__main__':
	sys.exit(main())



