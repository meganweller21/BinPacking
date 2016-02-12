""" ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Ashley Bertrand and Megan Weller
# Last Modified: February 3, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------

Strategy:
Create a dynamically growing square area
Sort objects by width in decreasing order
Build a binary tree
--Each branch contains a rectangle (already placed)
--Each leaf node represents an available space
--Initially the tree just has a root node (all available space)
--Placing a rectangle:
  --Search the tree for unoccupied leaf big enough to hold the rectangle
  --Change that node from a leaf to a branch by setting the rectangle as the node's occupant
  --Give that node two children
  --Left child: remaining space below the rectangle
  --Right child: remaining space to the right of the rectangle

FIND_NAIVE_SOLUTION:
	Line the the top left corners of the rectangles up along
the y = 0 axis starting with (0,0).
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
	w1 = width of rectangle 1,
	l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
		 e.g. [(x1, y1), ... (xn, yn)] where
		 x1 = top left x coordinate of rectangle 1 placement
		 y1 = top left y coordinate of rectangle 1 placement, etc.
"""

import math

def find_naive_solution (rectangles):   
	placement = []
	upper_left_x = 0
	upper_left_y = 0
	
	for rectangle in rectangles:
		width = rectangle[0]
		coordinate = (upper_left_x, upper_left_y)   # make a tuple
		placement.insert(0, coordinate)             # insert tuple at front of list
		upper_left_x = upper_left_x + width
		
	placement.reverse()                             # original order
	return placement

# -----------------------------------------------

"""
FIND_SOLUTION:
	Define this function in bin_packing.py, along with any auxiliary
functions that you need.  Do not change the driver.py file at all.
--------------------------------------------------
rectangles: a list of tuples, e.g. [(w1, l1), ... (wn, ln)] where
	w1 = width of rectangle 1,
	l1 = length of rectangle 1, etc.
--------------------------------------------------
RETURNS: a list of tuples that designate the top left corner placement,
		 e.g. [(x1, y1), ... (xn, yn)] where
		 x1 = top left x coordinate of rectangle 1 placement
		 y1 = top left y coordinate of rectangle 1 placement, etc.
"""

'''

Megan Notes:
Put the largest rectangle remaining into your packed area. If it can't fit anywhere, place it in a place 
that extends the pack region as little as possible. Repeat until you finish with the smallest rectangle.

'''

def find_solution(rectangles):

	areas = []
	solution = []
	areas = sort(rectangles)
	#pack_images(rectangles, 1, 250)
	
	upper_left_x = 0
	upper_left_y = 0

	i = 0
	j = 0

	for rectangle in rectangles:
		tuple = rectangles[j]
		length = tuple[1]

		while(upper_left_x <= int(avgWidth)):
			tuple = rectangles[j]
			width = tuple[0]
			coordinate = (upper_left_x, upper_left_y)   # make a tuple
			solution.insert(0, coordinate)             # insert tuple at front of list
			upper_left_x = upper_left_x + width
			j+1

		upper_left_x = 0
		upper_left_y = upper_left_y + length

	return solution
	#return find_naive_solution(rectangles)  # a working example!

'''
Ashley's find solution:
def find_solution(rectangles):

	sort_by_max_width(rectangles)
	return find_naive_solution(rectangles)  # a working example!
'''


def get_hard_coded():
	hard_coded = [(5,1),(1,6),(3,4),(7,8)]#,(5,8),(4,7),(1,6),(10,2),(9,3),(4,5)]
	return hard_coded

def get_size_of_list(rectangles):
	#rectangles = get_hard_coded()
	num_rectangles = len(rectangles)
	num_in_a_row = int(math.sqrt(num_rectangles))
	print(num_in_a_row)

def find_next_biggest(rectangles):
	rectangles = get_hard_coded()			
	temp = tuple(map(sorted, zip(*rectangles)))
	max_width = temp[0][-1]
	max_height = temp[1][-1]
	if(max_width > max_height):
		return temp[0][-1]
	else:
		return temp[1][-1]

def sort(rectangles):
	rectangles = get_hard_coded()			
	heights = []
	

	#Megan stuff:
	areas = []
	i = 0
	n=0
	width = 0
	global avgWidth 
	avgWidth= 0
	x= 0 

	for rectangle in rectangles:
		width += rectangle[0]
		areas.insert(i, rectangle[x]*rectangle[x+1])

		'''
		#	areas.insert(i, rectangle[0]*rectangle[1])
		heights.insert(i, rectangle[1])
		i+1
	#areas.sort(reverse=True)
	heights.sort(reverse=True)
	#print(heights)
		'''	
		n+=1
		x+2
		i+1
	
	avgWidth = (width)/(n) * math.sqrt(n)
	avgWidth = math.floor(avgWidth)
	areas.sort(reverse=True)

	return areas


def sort_by_max_width(rectangles):
	rectangles = get_hard_coded()
	sorted_rectangles = sorted(rectangles, key=lambda x: (x[0], x[0]))
	sorted_rectangles.reverse()
	#for rectangle in sorted_rectangles:
	#	print(rectangle)
	return sorted_rectangles

def pack_images(rectangles, grow_mode, max_dim):
    root=()
    while rectangles:
        rectangle = rectangles.pop()
        if not root:
            if (grow_mode):
                root = rect_node((), rectangle(0, 0, rectangle[0], rectangle[1]))
            else:
                root = rect_node((), rectangle(0, 0, max_dim[0], max_dim[1]))
            root.split_node(rectangle)
            continue
        leaf = find_empty_leaf(root, rectangle.img)
        if (leaf):
            leaf.split_node(rectangle)
        else:
            if (grow_mode):
                root.grow_node(rectangle)
            else:
                raise Exception("Can't pack images into a %d by %d rectangle." % max_dim)
    return root

def build_tree():
	rectangles = sort_by_max_width()
	
class BinaryTree():

    def __init__(self, width, height, x, y):
      self.left = None
      self.right = None
      self.width = width
      self.height = height
      self.x = x
      self.y = y

	def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self, width, height, x, y):
        self.width = width
        self.height = height
    	self.x = x
    	self.y = y
    def getNodeWidth(self):
        return self.width
    def getNodeHeight(self):
    	return self.height
    def getNodeX(self):
    	return self.x
    def getNodeY(self):
    	return self.y
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())



# test tree

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)

