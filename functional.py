import inspect

def curry(func):
    
    num_args = len(inspect.getargspec(func).args)
    args_list = []
    print num_args
    
    def helper(arg):
        args_list.append(arg)
        print args_list
        if len(args_list) == num_args:
            args_list.reverse()
            return func(*tuple(args_list))
        else:
            return helper
        
    return helper
    
x = [1,2,3,4,5]

def add(x, y, z):
    return x + y + z

curry_add = curry(add)
curry1 = curry_add(1)
curry2 = curry1(2)
curry3 = curry2(3)
print(curry3)