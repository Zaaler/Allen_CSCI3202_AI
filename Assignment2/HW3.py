# This file will use other functions to construct and complete the assignment
import sys
import Queue
import ipdb
breakP = ipdb.set_trace

def main():
	args = sys.argv
	txtMap = args[1]
	rMap = readMap(txtMap)
	print rMap
	Map = makeMap(rMap)
	findNeighbors(Map)
	path = Astar(Map,3)
		
def readMap(worldname):
	array = []
	filename = open(worldname,'r')
	
   	for lines in filename.read().split('\n'):
		array.append(lines.split(' '))
		
	
	return array[:-2]

def makeMap(readMap):
	for j in range(len(readMap)):
		for i in range(len(readMap[j])):
			if j == 0 and i == len(readMap[j])-1:
				readMap[j][i] = mapNode(i,j,int(3),None)
			else:
				readMap[j][i] = mapNode(i,j,int(readMap[j][i]),None)
	return readMap

class mapNode:
	def __init__(self,x_loc,y_loc,map_type,neighbors):
		self.x = x_loc
		self.y = y_loc
		self.t = map_type
		self.n = []
		self.cost = 0
		self.p = None

# NEIGHBOR FINDING FUNCTION TO BE APPLIED TO THE ENTIRE MAP
def findNeighbors(Map):
	for j in range(0,len(Map)):
		for i in range(0,len(Map[j])):
			# IF IN THE TOP ROW OF THE MAP
			if (j == 0):
				# IF LEFT CORNER
				if (i == 0):
					#breakP()
					Map[j][i].n.append(Map[j][i+1])
					Map[j][i].n.append(Map[j+1][i])
					Map[j][i].n.append(Map[j+1][i+1])
				# IF RIGHT CORNER
				elif (i == len(Map[j])-1):
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
				elif (i == len(Map[j])-1):
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
				if j != 0 or j != len(Map)-1:
					#breakP()
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
				#breakP()
				Map[j][i].n.append(Map[j-1][i-1])
				Map[j][i].n.append(Map[j-1][i])
				Map[j][i].n.append(Map[j-1][i+1])
				Map[j][i].n.append(Map[j][i-1])
				Map[j][i].n.append(Map[j][i+1])
				Map[j][i].n.append(Map[j+1][i-1])
				Map[j][i].n.append(Map[j+1][i])
				Map[j][i].n.append(Map[j+1][i+1])
			#print len(Map[j][i].n),
		#print
	
# FOUND CODE FOR THE ASTAR FUNCTION ON WIKIPEDIA PAGE
def Astar(Map,goal):
    	# Empty Set of already visited
	cset = []    				# The set of nodes already evaluated.
    	# Set of Visited nodes on path
	oset = []	
	# Manhatten Score of first node
	Map[len(Map)-1][0].score = len(Map[0]) + len(Map) - 2
	# Add the start Node into the Map
	oset.append(Map[len(Map)-1][0])   

    	while oset != []:
		miny = 10000000000
		breakP()		
		for j in range(0,len(oset)):
			if oset[j].score < miny:
				mina = oset[j]
		
		current = mina
		if current.t == goal:
			return current
		oset.remove(mina)
        	cset.append(current)
        	
		for i in range(0,len(current.n)):
			neighbor = current.n[i]
            	
			if neighbor in cset:
                		continue
 
            		tentative_g_score = cost(Map,current,neighbor)
			print tentative_g_score
            		if neighbor in oset and tenetative_g_score < neighbor.score:
                		neighbor.p = current
                		neighbor.score = tentative_g_score
                	if neighbor not in oset:
				neighbor.p = current
				neighbor.score = tentative_g_score
                		oset.append(neighbor)
 
    	return failure

def cost(Map, current, neighbor):
	# Diagnol Move
	if (current.x - neighbor.x == (-1 or 1)) and (current.y - neighbor.y == (1 or -1)):
		s = current.score + (len(Map[0])-neighbor.x) + (len(Map)-neighbor.y) + 14
	# Horizontal Move
	elif (current.x - neighbor.x == (-1 or 1)) and (current.y - neighbor.y == 0):
		s = current.score + (len(Map[0])-neighbor.x) + (len(Map)-neighbor.y) + 10 
	# Vertical Move
	elif (current.x - neighbor.x == 0) and (current.y - neighbor.y == (-1 or 1)):
                s = current.score + (len(Map[0])-neighbor.x) + (len(Map)-neighbor.y) + 10
	s = 100000000
	return s

if __name__ == '__main__':
    sys.exit(main())
