def check_guess(guess,target):
    if guess < target:
        return 'too lowx'
    elif guess == target:
        return 'correctx'
    else:
        return 'too highx'

