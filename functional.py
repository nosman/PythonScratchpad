import inspect

def curry(func):
    
    num_args = len(inspect.getargspec(func).args)
    args_list = []
    
    def helper(arg):
        args_list.append(arg)
        if len(args_list) == num_args:
            args_list.reverse()
            return func(*tuple(args_list))
        else:
            return helper
        
    return helper
