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
	coords = []
	solution = []
	sortedRectangles = []
	sortedRectangles = sort(rectangles)
	sortedRectangles.reverse();
	upper_left_x = 0
	upper_left_y = 0
	new_Y = 1
	i = 0
	
	for sortedRectangle in sortedRectangles:

				
				length = sortedRectangle[1]
				new_Y = 0
			if(upper_left_x <= int(avgWidth) | upper_left_x == 0):
				width = sortedRectangle[0]
				coordinate = (upper_left_x, upper_left_y)   # make a tuple
				coords.insert(0, (coordinate, sortedRectangle[2]))          # insert tuple at front of list
				upper_left_x = upper_left_x + width
				print str(sortedRectangle[0]) + '  ' + str(sortedRectangle[1])
				#print str(upper_left_x) + '  ' + str(upper_left_y)
			else:
				upper_left_y = upper_left_y - length
				upper_left_x  = 0
				coordinate = (upper_left_x, upper_left_y)
				width = sortedRectangle[0]
				upper_left_x = width
				coords.insert(0, (coordinate, sortedRectangle[2]))
				new_Y = 1
				print str(sortedRectangle[0]) + '  ' + str(sortedRectangle[1])
				#print str(upper_left_x) + '  ' + str(upper_left_y)
		
		
	coords.sort(key=lambda tup: tup[1])
	coords.reverse()

	i = 0 
	for coord in coords:
		solution.insert(i, coord[0])
		i+1
	
	return solution
	#return find_naive_solution(rectangles)  # a working example!


def sort(rectangles):
	areas = []
	sortedRect = []
	width = 0
	lenth = 0
	n = 0
	i = 0
	sumWidth = 0
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
	areas.sort(key=lambda tup: tup[2], reverse=True)

	j = 0
	for area in areas:
		sortedRect.insert(j, (area[1], area[2], area[3]))
		j+1
		#print str(area[1]) + '  ' + str(area[2])


	return sortedRect

