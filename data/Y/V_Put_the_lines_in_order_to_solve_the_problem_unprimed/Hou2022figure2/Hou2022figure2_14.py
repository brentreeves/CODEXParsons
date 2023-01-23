def filter_strings(str_list):
    new_list = []
    for word in str_list:
        if len(word) > 3:
            new_list.append(word)
    return new_list
 
