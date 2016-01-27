"""
	Here's the assignment: https://www.hackerrank.com/challenges/pairs

	In short:
		Given N integers, return the number of pairs whose difference is K.

		There are multiple spins on the problem -- sometimes n and k are provided
		as arguments, other times you have to read from standard input -- and
		I'll be doing both that I know of.

	Constraints:
		There are no duplicates.
		Each integer is greater than zero.
		You don't have to worry about overflow.

	Sample Input:
		5 2
		1 5 3 4 2

	Sample Output:
		3

	Explanation:
		(1, 3), (3, 5), (2, 4)
		Note: (3, 1) is not considered a pair because of (1, 3)
"""

def pairs(a, k):
	"""
		Given a list of integers a and a value k, returns
		the number of integer pairs within a whose difference is k.
	"""
	# a is the list of numbers and k is the difference value
	answer = 0

	# Load values from list a to dictionary n_dict
	n_dict = {index : 0 for throwaway, index in enumerate(a)}

	# Determine whether value + k is also in the dictionary
  # If so, increment answer
	for value in n_dict:
		if value + k in n_dict:
			answer += 1

	return answer


def stdin_pairs():
	"""
		Accomplishes the same task as our pairs function, but
		includes standard input.
	"""
	import sys
	input = sys.stdin.readlines()

	### Clean input
	clean_line_one = input[0].rstrip("\n")
	first_line = [int(number) for number in clean_line_one if number.isdigit()]
	second_line = {int(number) : 0 for throwaway, index in input[1] if number.isdigit()}
	
	### Define relevant variables
	n = first_line[0]
	k = first_line[1]
	pairs = 0

	### Task
	for value in second_line:
		if value + k in second_line:
			pairs += 1
	
	return pairs


