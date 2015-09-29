#!/usr/bin/env python3

import sys
import ipdb
breakP = ipdb.set_trace

# This is the main script for Homework #5
def main():
	args = sys.argv

	# 1st argument is the text document containing the map
	txtMap = args[1]

	# 2nd argument is the acceptable error level
	e = args[2]

	# First, create an integer version of the map
	rMap = readMap(txtMap)
	print rMap

	# Now, convert the integer version into a list of nodes
	Map = makeMap(rMap)

	# Establish all the nodes neighbors
	findNeighbors(Map)
	
	

def readMap(worldname):
	array = []
	filename = open(worldname,'r')
	
   	for lines in filename.read().split('\n'):
		array.append(lines.split(' '))
		
	
	return array[:-2]

class mapNode:
	def __init__(self,x_loc,y_loc,map_type,neighbors):
		self.x = x_loc
		self.y = y_loc
		self.t = map_type
		self.n = []
		self.cost = 0
		self.p = None


def makeMap(readMap):
	for j in range(len(readMap)):
		for i in range(len(readMap[j])):
			if j == 0 and i == len(readMap[j])-1:
				readMap[j][i] = mapNode(i,j,int(3),None)
			else:
				readMap[j][i] = mapNode(i,j,int(readMap[j][i]),None)
	return readMap

# NEIGHBOR FINDING FUNCTION TO BE APPLIED TO THE ENTIRE MAP
def findNeighbors(Map):
	for j in range(len(Map)):
		for i in range(len(Map[j])):
			# IF IN THE TOP ROW OF THE MAP
			if (j == 0):
				# IF LEFT CORNER
				if (i == 0) :
					Map[j][i].n.append(Map[j][i+1])
					Map[j][i].n.append(Map[j+1][i])
					Map[j][i].n.append(Map[j+1][i+1])
				# IF RIGHT CORNER
				if (i == len(Map[j])-1):
					Map[j][i].n.append(Map[j][i-1])
					Map[j][i].n.append(Map[j+1][i])
					Map[j][i].n.append(Map[j+1][i-1])
				# NOT CORNERS => MUST BE CENTER
				else:
					Map[j][i].n.append(Map[j][i-1])
					Map[j][i].n.append(Map[j+1][i-1])
					Map[j][i].n.append(Map[j+1][i])
					Map[j][i].n.append(Map[j+1][i+1])
					Map[j][i].n.append(Map[j][i+1])
			# ELSE IF LAST ROW
			elif (j == len(Map)-1):
				# IF BOTTOM LEFT CORNER
				if (i == 0):
					Map[j][i].n.append(Map[j-1][i])
					Map[j][i].n.append(Map[j][i+1])
					Map[j][i].n.append(Map[j-1][i+1])
				# IF BOTTOM RIGHT CORNER
				if (i == len(Map[j])-1):
					Map[j][i].n.append(Map[j-1][i])
					Map[j][i].n.append(Map[j][i-1])
					Map[j][i].n.append(Map[j-1][i-1])
				# NOT CORNERS => MUST BE CENTER
				else:
                                        Map[j][i].n.append(Map[j][i-1])
                                        Map[j][i].n.append(Map[j-1][i-1])
                                        Map[j][i].n.append(Map[j-1][i])
                                        Map[j][i].n.append(Map[j-1][i+1])
                                        Map[j][i].n.append(Map[j][i+1])
			# IF IT IS NOT THE TOP OR BOTTOM ROW
			# IF IT IS LEFT SIDE
			elif (i == 0):
				Map[j][i].n.append(Map[j-1][i])
				Map[j][i].n.append(Map[j-1][i+1])
				Map[j][i].n.append(Map[j][i+1])
				Map[j][i].n.append(Map[j+1][i+1])
				Map[j][i].n.append(Map[j+1][i])
			# IF IT IS RIGHT SIDE
			elif (i == len(Map[j])-1):
				Map[j][i].n.append(Map[j-1][i])
				Map[j][i].n.append(Map[j-1][i-1])
				Map[j][i].n.append(Map[j][i-1])
				Map[j][i].n.append(Map[j+1][i-1])
				Map[j][i].n.append(Map[j+1][i])
			# ELSE IT IS IN THE CENTER OF THE MAP
			else:
				Map[j][i].n.append(Map[j-1][i-1])
				Map[j][i].n.append(Map[j-1][i])
				Map[j][i].n.append(Map[j-1][i+1])
				Map[j][i].n.append(Map[j][i-1])
				Map[j][i].n.append(Map[j][i+1])
				Map[j][i].n.append(Map[j+1][i-1])
				Map[j][i].n.append(Map[j+1][i])
				Map[j][i].n.append(Map[j+1][i+1])

if __name__ == '__main__':
    sys.exit(main())
