"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
	/ \
   1   0
  / \
 1   1"""

 #CURRENT VERSINO STILL BUGGY. WORK IN PROGRESS
import copy

class Node (object):
	numunival = 0 # this is a static class variable.
	nodedesignation = 0
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None
		Node.nodedesignation +=1
		self.designation = copy.deepcopy(Node.nodedesignation)
		print (self.designation)

	def addrightNode(self, value):
		self.right = Node(value)

	def addleftNode(self, value):
		self.left = Node(value)	

	def find_unival_trees(self):
		return self.unival_helper(self.value)

	def unival_helper(self, value):
		if self.right == None and self.left == None:
			print("HIT FROM NODE " + str(self.nodedesignation) + "_WITH NO CHILD NODES")
			Node.numunival +=1
			return True

		if self.value == value:
			print("test")
			if (self.left.unival_helper(value) and self.right.unival_helper(value)) == True :
				print("HIT FROM NODE " + str(self.nodedesignation) + "_WITH TWO CHILD NODES")
				Node.numunival +=1
				return True
			if (self.left == None and self.right.unival_helper(value)) == True:
				print("HIT FROM NODE " + str(self.nodedesignation) + "_ WITH ONLY RIGHT CHILD NODE")
				Node.numunival +=1
				return True
			if (self.right == None and self.left.unival_helper(value)) == True:
				print("HIT FROM NODE" + str(self.nodedesignation) + "_WITH ONLY LEFT CHILD NODE")
				Node.numunival +=1 
				return True
		else:
			if self.right != None:
				print("is happening RIGHT")
				self.right.unival_helper(self.right.value)
			if self.left != None:
				return self.left.unival_helper(self.left.value)
				print("is happening LEFT")
		return False

#generating the tree from the example
tree = Node('0')
tree.addleftNode('1')
tree.addrightNode('0')
tree.right.addrightNode('0')
tree.right.addleftNode('1')
tree.right.left.addleftNode('1')
tree.right.left.addrightNode('1')

print(tree.find_unival_trees())
print(tree.numunival)