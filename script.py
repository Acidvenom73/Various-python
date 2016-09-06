def count(sequence, item):
	result = 0
	for i in sequence: # For each item in *sequence*
		if item in sequence: # if *item* is in *sequence
			result = result + 1
	print result

count([1,2,1,1,6], 1)




# Return amount of times *item* appears in *sequence*
# Return it as an integer, int()
# *item* can be an integer, string, float or list
# Different code depending on input type?


