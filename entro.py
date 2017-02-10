# entro.py
# calculate shannon's entropy of a string of character

import math

def entropy(word):
	string_set = ''.join(set(word))
	string_set_length = len(string_set)
	i = 0
	h = 0 # entropy
	while i < string_set_length:
		p = char_prob(string_set[i], word)
		h += p * math.log(p, 2)
		i += 1
	return -h

def char_prob(char, word):
	string_length = len(word)
	char_count = word.count(char)
	prob = char_count / string_length
	return prob

h = entropy(input('Input the string to be calculated: '))

print('entropy of the string is', h)
