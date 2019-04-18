"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'


I also chose to add a serialise function that writes to file for additional functionality"""
import pickle

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(obj):
	filename = "dumpstest"

	infile = open(filename, 'wb')
	pickle.dump(obj, infile, protocol=3, fix_imports=True)
	infile.close()
	return pickle.dumps(obj)

def deserialize(data):
	filename = "dumpstest"

	infile = open(filename, 'rb')
	loadedobj = pickle.load(infile)
	infile.close()
	return loadedobj


node = Node('root', Node('left', Node('left.left')), Node('right'))

print(deserialize(serialize(node)).left.left.val)


#assert deserialize(serialize(node)).left.left.val == 'left.left