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
	
	# Problem 1 - USING PRIOR SAMPLING
	s_prob = priorSampling(samples)
	print s_prob

	# A) P(c = true)
	prob = calcProb(s_prob)
	
	print prob

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

def calcProb(results):
	# Different Probabilities
	c = 0
	cs = 0
	csr = 0
	csrwg = 0
	cswg = 0
	cr = 0
	crwg = 0
	cwg = 0
	s = 0
	sr = 0
	srwg = 0
	swg =0
	r = 0
	rwg = 0
	wg = 0

	# Different Variables
	c_count = 0
	s_count = 0
	r_count = 0
	wg_count = 0

	for i in results:
		c_count += 1
		if i[0] == True:
			c += 1
			s_count += 1
			if i[1] == True:
				cs += 1
				r_count += 1
				if i[2] == True:
					csr +=1
					wg_count += 1
					if i[3] == True:
						csrwg += 1
				else:
					wg_count += 1
					if i[3] == True:
						cswg += 1
			else:
				r_count += 1
				if i[2] == True:
					cr += 1
					wg_count += 1
					if i[3] == True:
						crwg += 1
				else:
					wg_count += 1
					if i[3] == True:
						cwg += 1
		else:
			s_count += 1
			if i[1] == True:
				s += 1
				r_count += 1
				if i[2] == True:
					sr += 1
					wg_count += 1
					if i[3] == True:
						srwg += 1
				else:
					wg_count += 1
					if i[3] == True:
						swg += 1
			else:
				r_count += 1
				if i[2] == True:
					r += 1
					wg_count += 1
					if i[3] == True:
						rwg += 1
				else:
					wg_count += 1
					if i[3] == True:
						wg += 1
	totals = ([c, cs, csr, csrwg, crwg, cwg, s, sr, srwg, swg, rwg, wg])
	
	return totals
if __name__ == '__main__':
	sys.exit(main())



