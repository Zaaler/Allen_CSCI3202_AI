#!/usr/bin/env python3

# This code will read in the input arguments from the command line to establish
# the Bayes Network. Then, the requested conditional probabilities will be retu-# rned to the user.

import sys
import getopt

def main():
	read()
	

def read():
	try:
		(opts, args) = getopt.getopt(sys.argv[1:], "gjmp:v", ["Conditional Probability:", "Joint Probability:", "Marginal Probability:", "Prior:"])
	except getopt.GetoptError as err:
		# Print Help Information and Exit:
		# Print if option or arg not recognized is not recognized
		print str(err)
		usage()
		sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o == "-g":
			# Implement or pass to conditional probability
			pass
		elif o == "-j":
			# Implement joint probability
			pass
		elif o == "-m":
			# Implement marginal probability
			pass
		elif o == "p":
			# Set a prior for Pollution or Smoking
			pass
		else:
			assert False, "unhandled option"



if __name__ == '__main__':
    sys.exit(main())
 
