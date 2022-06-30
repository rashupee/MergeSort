def initialize_array(array):
	result = []
	for element in array:
		result.append([element])
	return result





def merge_sort(a1, a2):
	result = []

	a1_finished, a2_finished = not bool(a1), not bool(a2)
	i, j = 0, 0
	while not a1_finished and not a2_finished:
		if a1[i] <= a2[j]:
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




def merge_sorted(array):
	answer = []

	return answer