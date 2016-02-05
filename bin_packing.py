# ----------------------------------------------
# CSCI 338, Spring 2016, Bin Packing Assignment
# Author: Ashley Bertrand and Megan Weller
# Last Modified: February 3, 2016
# ----------------------------------------------
# Modified to include find_naive_solution so that
# driver does not need to be imported.  You may delete
# find_naive_solution from your submission.
# ----------------------------------------------
# Strategy:
# Create a dynamically growing square area
# Sort objects by area in decreasing order
# Build a binary tree
# --Each branch contains a rectangle (already placed)
# --Each leaf node represents an available space
# --Initially the tree just has a root node (all available space)
# --Placing a rectangle:
#   --Search the tree for unoccupied leaf big enough to hold the rectangle
#   --Change that node from a leaf to a branch by setting the rectangle as the node's occupant
#   --Give that node two children
#   --Left child: remaining space below the rectangle
#   --Right child: remaining space to the right of the rectangle

"""
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

def find_solution(rectangles):
    sort()
    pack_images(rectangles, 1, 250)
    return find_naive_solution(rectangles)  # a working example!

def get_hard_coded():
	hard_coded = [(5,6),(1,2),(3,4),(7,8)]
	return hard_coded

def sort():
	rectangles = get_hard_coded()			# used for testing purposes
	areas = []
	i = 0
	for rectangle in rectangles:
		areas.insert(i, rectangle[0]*rectangle[1])
		i+1
	areas.sort(reverse=True)

def pack_images(named_images, grow_mode, max_dim):
    root=()
    while named_images:
        named_image = named_images.pop()
        if not root:
            if (grow_mode):
                root = rect_node((), rectangle(0, 0, named_image.img.size[0], named_image.img.size[1]))
            else:
                root = rect_node((), rectangle(0, 0, max_dim[0], max_dim[1]))
            root.split_node(named_image)
            continue
        leaf = find_empty_leaf(root, named_image.img)
        if (leaf):
            leaf.split_node(named_image)
        else:
            if (grow_mode):
                root.grow_node(named_image)
            else:
                raise Exception("Can't pack images into a %d by %d rectangle." % max_dim)
    return root
