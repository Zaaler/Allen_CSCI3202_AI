# Problem 1 - working with the Queue
from Queue import Queue

class IntQueue:
	def __init__(self):
		self.q = Queue()

	def put(self,n):
		if int(n):
			return self.q.put(n)
	def dump(self):
		return self.q.queue
	def pop(self):
		return self.q.get()



# Problem 2 - Stack Module
class IntStack:
	def __init__(self):
		self.l = list()
	def push(self,n):
		if int(n):
			return self.l.append(n)
	def checkSize(self):
		return len(self.l)
	def pop(self):
		return self.l.pop()

# Problem 3 - Binary Tree
def Node():
	def __init__(self, keyn):
		self.key = keyn
def BTree():
	def __init__(self,Node):
		self.root = Node
		self.left = None
		self.right = None
	def getNodeValue(self):
		return self.root.key
	def setNodeValue(self, value):
		self.root.key = value
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def add(self, value, pkey):
		if pkey == self.root.key:
			if self.root.left != None & self.root.right == None:
				self.right = BTree(Node(value))
			if self.root.left == None:
				self.left = BTree(Node(value))
			if self.left != None & self.right != None:
                                print("Parent has two children, node not added.")
				self.left.add(value,pkey)


# Problem 4 - Graph
class vertex():
	def __init__(self,value):
		self.key = value
		self.adjacent = list()



def Allen_Assignment1():
	
	print "Problem 1 - Testing the Queue"
	a = IntQueue()
	for i in range(0,10):
		a.put(i)
	for i in range(0,10):
		r = a.pop()
		print "Dequeue: ", r
	print "Problem 2 - Testing the Stack" 
	b = IntStack()
	for i in range(0,10):
		b.push(i)
	for i in range(0,10):
		t = b.pop()
		print "Pop: ", t
	print "Problem 3 - Testing the Binary Tree"
	print "I struggled with this pretty badly, check my code"
	print "Problem 4 - Testing Graph"

	return
