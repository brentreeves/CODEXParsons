# Create the function, filter_strings(str_list), below to take a list of strings, str_list, and return a new list with all the strings from the passed list in the same order that have a length greater than 3.  For example, filter_strings(["Run", "she", "said"]) should return ["said"] and filter _strings(["It", "was", "a", "dark", "night"]) should return ["dark", "night"]
def filter_strings(str_list):
	new_list = []
	for word in str_list:
		if len(word) > 3:
			new_list.append(word)
	return new_list
