#!/usr/bin/python3
"""
A Machine learning algorithm for K mean clustering.
Date: 15th Feb, 2015 10:31pm
"""
__author__ = "Denis Karanja"
__version__ = "1.0.0"

import random

def euclidean_distance(point, centroid):
	'''Returns the euclidean distance between two points'''
	assert type(point) is tuple
	assert type(centroid) is tuple

	#x and y values for the point and the centroid
	point_x, point_y = point
	centroid_x, centroid_y = centroid

	#get euclidean distance
	distance = ( (point_x - centroid_x) ** 2 ) + ( (point_y - centroid_y) ** 2 ) 
	distance = distance ** (0.5)

	return round(distance, 4)

def get_coordinates(points):
	#get coordinates for the points given in tuple form
	print("Please provide coordinates for the {} points. (x, y)".format(points))
	coordinates = []

	for coords in range(points):
		#read as a tuple i.e (x, y)
		coordinates.append( tuple(input()) )

		x, y, z = coordinates[coords]
		coordinates.remove((x, y, z))
		coordinates.append((int(x), int(z)))

	return coordinates


def group_matrix(points):
	'''Return the group matrix given coordinates'''
	coords = get_coordinates(points)
	centroids = []
	euclid_distance = []
	group_distance = []
	grp_matrix = []

	#create an alphabet number mapping
	alphabets = dict(A = 1,B = 2,C = 3,D = 4,E = 5,F = 6,G = 7,H = 8,I = 9,J = 10,K = 11,L = 12,M = 13,
		N = 14,O = 15,P = 16,Q = 17,R = 18,S = 19,T = 20,U = 21,V = 22,W = 23,X = 24,Y = 25,Z = 26)

	#get two random centroids
	for x in range(2):
		k = random.randint(0, (points-1))
		centroids.append(k)

	#get the centroids as per the above rand positions
	centroids = tuple(centroids)
	i, j = centroids
	centroid_one = coords[i]
	centroid_two = coords[j]

	#get euclidean distance for the points and the centroids
	for y in coords:
		#get distance for each point in regard to centroid one
		distance_one = euclidean_distance(y, centroid_one)

		#get distance for each point in regard to centroid two
		distance_two = euclidean_distance(y, centroid_two)

		euclid_distance.append((distance_one, distance_two))

		#group matrix condtions
		if distance_one > distance_two:
			grp_matrix.append((0, 1))
		elif distance_one < distance_two:
			grp_matrix.append((1, 0))

	return grp_matrix

def k_means_cluster(points):
	'''Returns the specific clusters where points lie'''
	#get the group matrix
	grp_matrix = group_matrix(points)
	#get the number of elements in each cluster
	a, b = [], []
	for x_y_values in grp_matrix:
		m, n = x_y_values
		a.append(m)
		b.append(n)

	cluster_one_elems = sum(a)
	cluster_two_elems = sum(b)

	#calculate new centroids and iterate till stable i.e no change on group matrix
	temp_grp_matrix = grp_matrix
	while True:
		if cluster_one_elems == 1:
			#use the same centroid from the previous one
			pass
		elif cluster_one_elems > 1:
			#new centroid is the average of the elements
			pass

		if cluster_two_elems == 1:
			#use the same centroid used in the last iteration
			pass
		elif cluster_two_elems > 1:
			#new centroid is the average of the elements
			pass


		#when no more change happens, stop iteration
		if grp_matrix == temp_grp_matrix:
			return grp_matrix


	#return euclid_distance, grp_matrix


if __name__ == "__main__":
	print(group_matrix(4))