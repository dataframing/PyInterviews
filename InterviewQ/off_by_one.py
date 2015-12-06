"""
	Here's the assignment:
		You're given two strings that are identical with the exception
		that one string has just one extra character. You are asked to
		return the differing character.

	Constraints:
		Ideally, you would not use auxiliary space or data structures

	Examples:
		Given strings "abc" and "abcd", return: "d"
		Given strings "one" and "neoj", return "j"

	Implementation considerations:
		Originally I thought of converting each string into a set and 
		utilizing set difference, but that proves tricky on string pairs 
		like "nn" and "nnn", which would result in an empty difference set.
"""

def string_difference(string_1, string_2):
	difference = []
	if len(string_1) > len(string_2):
		difference = [char for char in string_1 if char not in string_2]
	else:
		difference = [char for char in string_2 if char not in string_1]
	return "".join(difference)


def main():
	from string import ascii_letters
	from random import choice as random_choice
	ascii_length = len(ascii_letters)
	for i in range(ascii_length):
		test_string_1 = test_string_2 = ascii_letters[i]
		random_letter = random_choice(ascii_letters)
		if i % 2 == 0:
			test_string_2 += random_letter
		else:
			test_string_1 += random_letter
		difference = string_difference(test_string_1, test_string_2)
		assert difference == "{}".format(random_letter), "Expected string difference of {}, was actually {} when s1 = {} and s2 = {} on i = {}".format(random_letter, difference, test_string_1, test_string_2, i)
		 

if __name__ == "__main__":
	main()
