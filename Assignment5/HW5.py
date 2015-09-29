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
	
	breakP()
	# Now, convert the integer version into a list of nodes
	Map = makeMap(rMap)
	
	breakP()
	# Establish all the nodes neighbors
	findNeighbors(Map)
	
	breakP()	

# CONVERT THE GIVEN TEXT VERSION INTO MORE READABLE VERSION
def readMap(worldname):
	array = []
	filename = open(worldname,'r')
	
   	for lines in filename.read().split('\n'):
		array.append(lines.split(' '))
		
	
	return array[:-2]

# CLASS FOR THE NODES OF THE MAP
class mapNode:
	def __init__(self,x_loc,y_loc,map_type,neighbors):
		
		# This is the location of the node
		self.x = x_loc
		self.y = y_loc
		
		# This is the integer value of the map location
		self.t = map_type
		
		# Is this a wall
		if (self.t == 2 | self.t == 3):
			self.walkable = False
		else:
			self.walkable = True

		# DESIGNATE REWARD BASED ON MAP TYPE
		if (self.t == 1):
			# MOUNTAIN
			self.reward = -1
		if (self.t == 4):
			# BARN
			self.reward = 1
		if (self.t == 50):
			# APPLE
			self.reward = 50
		if (self.t == 0):
			# ANY WALKABLE 
			self.reward = 0	
		if (self.t == 2):
			# ANY WALL
			self.reward = 0
		if (self.t == 3):
			# ANY SNAKE HAS NO REWARD
			self.reward = 0

		# Establish all nodes at 0 utility	
		self.utility = 0
		
		# Establish a neighbors array
		self.n = []
		
		# Establish a parent array
		self.p = []

# MAKE THE MAP FROM THE INTEGER REPRESENTATION
def makeMap(readMap):
	for j in range(len(readMap)):
		for i in range(len(readMap[j])):
			readMap[j][i] = mapNode(i,j,int(readMap[j][i]),None)
	return readMap



# NEIGHBOR FINDING FUNCTION TO BE APPLIED TO THE ENTIRE MAP
def findNeighbors(Map):
	for j in range(len(Map)):
		for i in range(len(Map[j])):
			# IF IN THE TOP ROW OF THE MAP
			if (j == 0):
				# IF LEFT CORNER
				if (i == 0):
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
