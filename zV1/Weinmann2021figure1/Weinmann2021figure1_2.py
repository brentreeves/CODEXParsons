def last_even_adder(li):
    for index in range (len(li)-1,-1,-1):
        if(li[index]) % 2 == 0:
            return 'All odd'
        return lambda x : x + li[index]

