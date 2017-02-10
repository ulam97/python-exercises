# f_entro.py
# calculate shannon's entropy of a text file

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

def wordlist(fname):
	with open(fname) as f:
		return f.read()

def main():
	print('Put the text file to be calculated together with this script in a folder.')
	fname = input('Input the name of the file (e.g: \'entropy.txt\'): ')
	word = wordlist(fname)
	h = entropy(word)
	print('entropy of file', fname, 'is', h)

main()