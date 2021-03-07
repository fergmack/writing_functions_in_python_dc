

def mean(values):
  """ Get the mean of a list of values

      Args:
      values (iterable of float): a list of numbers

      Returns:
      float: The mean
      """
  mean = sum(values) / len(values)
  return mean 


def median(values):
  """Get the median of a list of values
      
      Args:
      values (iterable of float: a list of numbers
      
      Returns:
      float: The mean"""
  
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    return ((values[midpoint] + values[midpoint - 1 ]) / 2)
  else:
    return values[midpoint]

print(median([1, 2, 3, 4]))


# # Function explained
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# midpoint = int(len(values)/ 2)
# print(midpoint)
# # median = (values[midpoint - 1] + values[midpoint]) / 2
# print(values[midpoint]) # the 5th index is 6
# print(values[midpoint - 1 ]) # 6 minus 1 = 5
# # get the average 
# print( (values[midpoint] + values[midpoint -1 ]) / 2) # median of 10 is 5.5

# e.g. 
# l = [1, 2, 3, 4]
# print(len(l))
# print(len(l)/2)
# midpoint = int(len(l)/2)
# print(midpoint)
# l[midpoint - 1]
