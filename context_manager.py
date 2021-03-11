import contextlib 
import time

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block. 
  
  Yields:
  None"""
  start = time.time()
  # send control back to the context block 
  yield 
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

# You're managing context like a boss! And your colleague can now use your timer() context manager to figure out which of their functions is running too slow. Notice that the three elements of a context manager are all here: a function definition, a yield statement, and the @contextlib.contextmanager decorator. It's also worth noticing that timer() is a context manager that does not return an explicit value, so yield is written by itself without specifying anything to return.


# A read-only open() context manager
# You have a bunch of data files for your next deep learning project that took you months to collect and clean. It would be terrible if you accidentally overwrote one of those files when trying to read it in for training, so you decide to create a read-only version of the open() context manager to use in your project.

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode. 
  Args:
  filename (str): The location of the file to read
  
  Yields:
  file object
  """
  read_only_file = open(filename, mode='r')
  # yield read_only_file so that it can be assigned to my_file
  yield read_only_file
  # close file
  read_only_file.close()

with open_read_only('my_file.txt') as my_file:
  print(my_file.read())


# Now that every time you use with open_read_only() your files are safe from being accidentally overwritten. This function is an example of a context manager that does return a value, so we write yield read_only_file instead of just yield. Then the read_only_file object gets assigned to my_file in the with statement so that whoever is using your context can call its .read() method in the context block.
