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
Our find_solution:
Pass the rectangles array into the sorting method, which will bring back a sorted list of largest height to smallest in
sortedRectangle[]. Keep track of the length of the far left box to add onto the length later. Begin by packing the 
rectangles in (x, 0) until we reach our avgWidth. Once that is complete, assign a new length by adding the length of the
far left rectangle to the length and assign upper_left_x to 0. Add that box to it's new position and repeat until the bin
is packed.

Sort the rectangles by their token to match the dimenions in the squares.txt file. And finally, add the coordinates
to solution[] and return the optimized bin packing solution.

'''

def find_solution(rectangles):
	#make arrays here
	coords = []
	solution = []
	sortedRectangles = []
	keepY = []
	sortedRectangles = sort(rectangles)

	#reverse the array so we start off at 0
	sortedRectangles.reverse();

	#initialize variables, our x and y and the array index
	upper_left_x = 0
	upper_left_y = 0
	j = 0

	for sortedRectangle in sortedRectangles:

			#finds the length of the rectangle and puts it in an array list
			length = sortedRectangle[1]		
			keepY.insert(j, length)
			#if x is less than out set width, assign coordinates to rectangles
			if(upper_left_x <= int(avgWidth)):		
				width = sortedRectangle[0]
				coordinate = (upper_left_x, upper_left_y)   # make a tuple
				coords.insert(0, (coordinate, sortedRectangle[2]))          # insert tuple at front of list
				upper_left_x = upper_left_x + width 						# assign new width
				#print statements to check
				#print str(sortedRectangle[0]) + '  ' + str(sortedRectangle[1])
				#print str(upper_left_x) + '  ' + str(upper_left_y)
				j+1
			#once we reach the x limit, add to (0, length)	
			else:
				#grab the 0th index (the y we need)
				keepY.reverse()
				upper_left_y = upper_left_y - keepY[0]	#subtracting to make sense of an x/y coordinate
				
				upper_left_x  = 0
				coordinate = (upper_left_x, upper_left_y)	# make a tuple
				width = sortedRectangle[0]
				upper_left_x = width 						#reassign x
				coords.insert(0, (coordinate, sortedRectangle[2]))	 # insert tuple at front of list
				#reset the array point
				j = 0

				#print statements to check
				#print str(sortedRectangle[0]) + '  ' + str(sortedRectangle[1])
				#print str(upper_left_x) + '  ' + str(upper_left_y)
		
	#I am sorting by the "token", when calculating the corner coordinates, it was not using the right dimensions
	coords.sort(key=lambda tup: tup[1])
	coords.reverse()

	#only insert our coordinates into the solution
	i = 0 
	for coord in coords:
		solution.insert(i, coord[0])
		i+1
	
	return solution

'''
Sort:
We started sorting by the largest area to the smallest, but ended up using the height, the first sorting for loop
is unncessary, but is there if needed. Begin by calculating the area of weight and length and add it to a coordinate.
N is the token, or the spot in the text file, it comes from. We were having issues with it not calculating the corner
coordinates in the driver.

Also, keep track of the total sum of all of the widths.

Calculate the avgWidth that we want to work with by dividing n boxes by the sumWidth and multiply the square root of n.
This will give us a sqaure that we will pack into when we find the solution.

Finally, add the width, length, and token into sortedRect and return the sorted array.
'''
def sort(rectangles):
	#intilize arrays
	areas = []
	sortedRect = []

	#initalize variables
	width = 0
	lenth = 0
	n = 0
	i = 0
	sumWidth = 0
	#global variable to use in packing
	global avgWidth 
	avgWidth= 0

	#n is my token to keep track of the specific rectangle
	
	for rectangle in rectangles:
		width = rectangle[0]
		length = rectangle[1]
		sumWidth += rectangle[0]
		coordinates = (width*length, width, length, n)
		areas.insert(i, coordinates)
		n+=1
		i+1

	avgWidth = (sumWidth)/(n) * math.sqrt(n)
	avgWidth = math.floor(avgWidth)
	#sort by heights
	areas.sort(key=lambda tup: tup[2], reverse=True)

	j = 0
	#insert only the coordinates and the token
	for area in areas:
		sortedRect.insert(j, (area[1], area[2], area[3]))
		j+1
		#print str(area[1]) + '  ' + str(area[2])


	return sortedRect

