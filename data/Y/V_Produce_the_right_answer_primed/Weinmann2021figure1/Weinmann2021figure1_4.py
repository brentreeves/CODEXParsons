def last_even_adder(li):
    if li[index] % 2 == 0:
        for index in range(len(li)-1, -1, -1):
            return lambda x: x + li[index]
    return 'All odd'
