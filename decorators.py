import inspect 


# decorator 
def print_args(func):
  # get original args - e.g. a, b, c
  sig = inspect.signature(func)
  def wrapper(*args, **kwargs):
    # returnds ordered dictionary, list of tuples [(a, 1), (b, 2)] etc
    bound = sig.bind(*args, **kwargs).arguments
    str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
    print('{} was called with {}'.format(func.__name__, str_args))
       # return the function that was passed to the decorator's args
    return func(*args, **kwargs)
  return wrapper 


# /// * inspect the decorator 
# def test_dec(func):
#   # get args
#   sig = inspect.signature(func)
#   print(sig)
#   def wrapper(*args, **kwargs):
#     # returnds ordered dictionary, list of tuples [(a, 1), (b, 2)] etc
#     bound = sig.bind(*args, **kwargs).arguments
#     print(bound)
#     # for each item in bound, iterate and get tuple values k, v
#     str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
#     print('{} was called with {}'.format(func.__name__, str_args))
#     print(func(*args, **kwargs))
#     # return the function that was passed to the decorator's args
#     print(type(func(*args, **kwargs)))
#     return func(*args, **kwargs)
#   print(type(wrapper))
#   return wrapper 

# test =  test_dec(my_function)
# test(1, 2, 3)
# // 

# Decorate my_function() with the print_args() decorator
# function
def my_function(a, b, c):
  print(a + b + c)

my_function = print_args(my_function)

# or 
@print_args
def my_function(a, b, c):
  print(a + b + c)
my_function(10, 10, 10)


# Note that @print_args before the definition of my_function is exactly equivalent to my_function = print_args(my_function). Remember, even though decorators are functions themselves, when you use decorator syntax with the @ symbol you do not include the parentheses after the decorator name.
