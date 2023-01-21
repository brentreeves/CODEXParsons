def errortype(key):
    msgs = {'output': 'output incorrect',
            'runtime': 'runtime error',
            'import': 'import error'}
    if not key in msgs:
        # self logerr(1, f'ERROR - invalid error code: {key}')
        print( f'ERROR - invalid error code: {key}')
        return 'unknown error'
    else:
        return msgs[key]

print( errortype('output') )
print( errortype('runtime') )
print( errortype('import') )
print( errortype('blee') )
