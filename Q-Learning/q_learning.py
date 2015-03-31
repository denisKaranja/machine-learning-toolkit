#!/usr/bin/python3
"""
Task: Q learning algorithm for machine learning...

Based on Reward and punishment

Date: 18th Feb, 2015 8:35 (pm)
"""

__author__ = "Denis Karanja"
__version__ = "1.0.0"

# Q-learning agent for "trash world"
#
# by Leland Aldridge, Harry Glaser, Tom O'Neill
# for CSC 242 Project 4: Learning
# 4/21/2006
import sys, random
# useful utilities
def debug(s):
	if DEBUG:
		print (s)
def enum(*args):
	g_lobal = globals()
	i = 0
	for arg in args:
		g_lobal[arg] = i
		i += 1
	return i

def Q_Learning():
	Q_Matrix = {}
	R_Matrix = {}



# GLOBALS ###########
NUM_ACTIONS =enum('ACTION_PICKUP',
									'ACTION_NORTH',
									'ACTION_EAST',
									'ACTION_SOUTH',
									'ACTION_WEST')
DEBUG = False
GRID_LENGTH = 4
THRESH = .2
TRASH_CHAR = '1'
CLEAR_CHAR = '-'
Q_INIT = 0

# Learning tables
Q = {}

Nsa = {} 
trash = {}

# Learning parameters
ALPHA = 0.5
GAMMA = 0.5
N = 5

trashes = 0
picked = 0
curPos = (0, 0)
grid = []
actions = 0



