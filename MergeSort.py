

def initialize_array(array):
	# Produces a list of lists as a starting point for the merge sort algorithm

	result = []
	for element in array:
		result.append([element])

	return result


def merge_sort(a1, a2):
	# The basic mserg sort algorithm that takes two lists of elements, where each list is already sorted,
	# and merges these two lists into a single sorted list.

	result = []
	a1_finished, a2_finished = not bool(a1), not bool(a2)
	i, j = 0, 0
	while not a1_finished and not a2_finished:
		if a1[i] <= a2[j]: # The = sign assures a 'stable' sort that preserves the order of same-rank elements
			result.append(a1[i])
			i += 1
			if i == len(a1):
				a1_finished = True
		else:
			result.append(a2[j])
			j += 1
			if j == len(a2):
				a2_finished = True
	if not a1_finished:
		for index in range(i, len(a1)):
			result.append(a1[index])
	if not a2_finished:
		for index in range(j, len(a2)):
			result.append(a2[index])
	
	return result


def merge_pairs(working_array):
	# Working_array is a list of sorted lists. If working_array is an odd number of elements,
	# the last two elements are merged sorted to create an even number. Then this merge sorts
	# in pairs.

	new_working_array = []
	if len(working_array)%2 != 0:
		working_array.append(merge_sort(working_array.pop(), working_array.pop() ) )
	for i in range(0, len(working_array), 2):
		new_working_array.append(merge_sort(working_array[i], working_array[i+1]))

	return new_working_array


def merge_sort_boss(array):
	# This function is the main scheduler which uses the above functions to take an array and return
	# a sorted version. The original array is unchanged.
	
	working_array = initialize_array(array)
	while len(working_array) > 1:
		working_array = merge_pairs(working_array)
	result = working_array.pop()
	
	return result