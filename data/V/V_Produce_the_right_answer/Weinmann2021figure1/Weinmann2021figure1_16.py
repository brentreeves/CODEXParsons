def last_even_adder(li):
    def adder(x):
        for index in range(len(li)-1, -1, -1):
            if li[index] % 2 == 0:
                return x + li[index]
        return 'All odd'
    return adder
