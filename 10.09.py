def show(func):
    def new_func(*args, **kwargs):
        print(' Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        prunt('Keyword argumebts are: ', kwargs)
        result = func(*args,**kwargs)
        print('Result: ',result)
        return result
    return new_fanc
def names_generator(num=1):
    i=0
    while i < num:
        s =''
        for k in range(0,3):
            s += chr(randrange(97,122))*5
            if k < 2:
                s += ' '
        yield s
        i += 1
def initials(name):
    I = name.split()
    return I[0] +' ' + I[1][0:1] + '.' + I[2][0:1]

@show
def initials_more(names):
    return [initials(name) for name in names_generator
            
print( initials_more(names))