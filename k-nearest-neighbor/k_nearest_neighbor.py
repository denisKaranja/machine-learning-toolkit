#!/usr/bin/python3
"""
A Machine learning algorithm for K Nearest Neighbor.
Date: 17th Feb, 2015 8:51 am


Suppose we have data from some survey (that asks people’s opinions) 
on whether certain toilet papers are good or bad. 
The toilet papers have two attributes (acid durability and strength)

TASK:
 We want to determine whether a toilet paper with attributes X1=3 and X2= 7 is GOOD or BAD

 Given:
 {
 		Acid Durability(seconds),	strength, Classification
 		7, 7, bad
 		7, 4, bad
 		3, 4, good
 }
"""
__author__ = "Denis Karanja"
__version__ = "1.0.0"

import collections, csv 

def get_coordinates(points):
	#get coordinates for the points given in tuple form
	'''
	@param -> tuple
	@return -> list of tuples
	'''
	print("Please provide coordinates for the {} training set. (x, y, label)".format(points))
	coordinates = []

	for coords in range(points):
		#read as a tuple i.e (x, y)
		user_coords = input()
		user_coords = user_coords.split(',')
		x, y, label = int(user_coords[0]), int(user_coords[1]), user_coords[2]

		coordinates.append((x, y, label))

	return coordinates

def get_coords(file_name):
	'''Gets coordinates form a file'''
	file_handle = open(file_name, "r")
	for coords in file_handle:
		pass

def add_set(file_name, coords_list):
	'''Writes coodinates to file. As part of the learning set'''
	file_handle = open(file_name, "a")
	array = ''
	file_handle.write(str((coords_list[0])))
	

def distance_apart(query_instance, training_set, cluster_size, file_name):
	'''
	Determines how far a query set is from the training set
	@params -> tuple, list of tuples, int, string(file_name)
	@return -> tuple
	'''
	assert type(training_set) is list
	assert type(query_instance) is tuple
	assert type(cluster_size) is int

	distance = []
	x_query, y_query = query_instance

	for value in training_set:
		x_train_set, y_train_set, label = value
		dist = ((x_train_set - x_query) ** 2) + ((y_train_set - y_query) ** 2)
		distance.append((dist, label))

	#get the K nearest neigbours
	distance = sorted(distance)[:cluster_size]
	print(distance)
	#get all labels only in the K nearest neigbours
	final_label = []
	for result in distance:
		score, k_label = result
		final_label.append(k_label)


	#get frequecies of labels
	conc_array = []
	label_freq = collections.Counter(final_label)
	query_label = (max(label_freq, key = label_freq.get), )
	conclusion = query_instance + query_label
	conc_array.append(conclusion)

	#add set to learning set
	add_set(file_name, conc_array)

	return conclusion, "Set added to {}".format(file_name)


def read_csv(filename):
	'''
	Read from a csv file
	@params -> String(Filename)
	@return coordinates
	'''
	from_file = []
	with open(filename) as data:
		reader = csv.reader(data)

		for stuff in reader:
			stuff = stuff[0:13]
			from_file.append(stuff)

	data_length = len(from_file)
	# 70% training set, 30% query set
	training_set_len = int(0.7 * data_length)
	query_set_len = int(0.3 * data_length)

	training_set = from_file[0: training_set_len]
	query_set = from_file[training_set_len:]

	
	#write to training set
	with open("training.csv", "w") as train_set:
		writer = csv.writer(train_set, delimiter = ",")
		writer.writerows(training_set)

	# write to query set
	with open("query.csv", "w") as query_instance:
		writer = csv.writer(query_instance, delimiter = ",")
		writer.writerows(query_set)

	return


if __name__ == "__main__":
	query, training, cluster_size, file_name = (5, 6), [(7, 7, 'bad'), (7, 4, 'bad'), (3, 4, 'good'), (1, 4, 'good')], 3, "../data_files/knn.txt" 
	#print(distance_apart(query, training, cluster_size, file_name ))
	#print(get_coords("data_files/knn.txt"))
	print(read_csv("../data_files/csv/heart.data.csv"))
	