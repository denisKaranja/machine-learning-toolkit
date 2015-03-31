#!/usr/bin/python3
"""
A Machine learning algorithm for K Nearest Neighbor.
Date: 17th Feb, 2015 8:51 am


Suppose we have data from some survey (that asks people’s opinions) 
on whether certain toilet papers are good or bad. 
The toilet papers have two attributes (acid durability and strength)


 Given:
 {
 	heart.data.txt
 }
"""
__author__ = "Denis Karanja"
__version__ = "1.0.0"

import collections, csv 

def vote(distance, final_label = []):
	'''
	Return output of the 
	@params -> list of tuples [(euclidean_dist, label)], tuple
	@return 
	'''
	for result in distance:
		score, k_label = result
		final_label.append(k_label)


	#get frequecies of labels
	conc_array = []
	label_freq = collections.Counter(final_label)
	query_label = max(label_freq, key = label_freq.get)
	#conclusion = query_instance + query_label
	#conc_array.append(conclusion)


	return query_label

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
			#stuff = stuff[0:13]
			from_file.append(stuff)

	data_length = len(from_file)
	# 70% training set, 30% query set
	training_set_len = int(0.7 * data_length)

	training_set = from_file[0: training_set_len]
	query_set = from_file[training_set_len:]
	query_set_refined = []
	
	for y in query_set:
		query_set_refined.append(y[0:13])

	
	#write to training set
	with open("training.csv", "w") as train_set:
		writer = csv.writer(train_set, delimiter = ",")
		writer.writerows(training_set)

	# write to query set
	with open("query.csv", "w") as query_instance:
		writer = csv.writer(query_instance, delimiter = ",")
		writer.writerows(query_set_refined)


	# read form the file
	query_holder = []
	with open("query.csv", "r") as read_query:
		reader = csv.reader(read_query)
		for query_data in reader:
			query_holder.append(query_data)

	return query_holder

def get_query_element():
	"""
	Return the element specified by the user
	@return list
	"""
	query_holder = read_csv("../data_files/csv/heart.data.csv")
	length = len(query_holder)
	print("Query instance contains {} elements.".format(length))
	print("Choose an element between 1 and {}".format(length))
	query_elem = int(input())
	assert query_elem > 0
	assert query_elem < length + 1

	# get the element
	query_elem = query_holder[query_elem + 1]
	print(query_elem)
	
	return query_elem

def get_distance(clusters):
	'''
	Get the element's outcome
	@params list, int
	'''
	element = get_query_element()

	dist = 0
	distance = []
	with open("training.csv") as training_set:
		reader = csv.reader(training_set)
		for every_train_set in reader:
			y = zip(every_train_set, element)
			for i in y:
				train_set = float(i[0])
				query_set = float(i[1])

				dist += ((train_set - query_set) ** 2)
				label = every_train_set[len(every_train_set) - 1]

				distance.append((dist, label))

	#get the nearest neighbours labels
	distance = sorted(distance)[:clusters]
	return distance
			



if __name__ == "__main__":
	print("The Query Set has an output of [{}]".format(vote(get_distance(20))))
	