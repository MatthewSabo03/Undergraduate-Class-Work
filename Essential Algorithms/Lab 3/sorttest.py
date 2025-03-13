# Original codebase by Rohrbaugh 2021
# Modifications by: Sabo 2023
# Last modified: 3/14/2023

import csv
import random
import time
from datetime import datetime

# replace yourlastname with your actual last name here
STUDENT_LASTNAME = 'sabo'
VERBOSE_OUTPUT = False

# global constants controlling tests
MIN_SIZE = 32
MAX_SIZE = 512
STEP_SIZE = 32
TRIALS = 20

# global variable used to count steps
step_count = 0
comp_count = 0
swap_count = 0

def bubble_sort(list):
  # step_count must be declared global here
  # otherwise it would create a new variable
  global step_count
  global swap_count
  global comp_count
  for i in range(len(list)-1):
    for j in range(len(list)-i-1):
      step_count += 1
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
        swap_count += 1
      comp_count +=1 


def selection_sort(list):
  global swap_count
  global comp_count
  for i in range(len(list)-1):
    min = i
    for j in range(i+1, len(list)-1):
      if list[min]>list[j]:
        min = j
      comp_count+=1
    if (min != i):
      list[i], list[min] = list[min], list[i]
      swap_count+=1


def insertion_sort(list):
  global swap_count
  global comp_count
  for i in range(1, len(list)-1):
    min = list[i]
    j = i-1
    while (j>=0 and min<list[j]):
      comp_count+=1
      list[j+1] = list[j]
      swap_count+=1
      j-=1
    comp_count+=1
    list[j+1] = min
    swap_count+=1
'''
Both merge and merge_sort pulled from : https://www.geeksforgeeks.org/python-program-for-merge-sort/
'''
def merge(list, left, mid, right):
  global swap_count
  global comp_count

  n1 = mid - left + 1
  n2 = right - mid

  left_array = [0]*(n1)
  right_array = [0]*(n2)

  for i in range(0, n1):
    left_array[i] = list[left+i]
  
  for j in range(0,n2):
    right_array[j] = list[mid+1+j]
  
  i=0
  j=0
  k=left

  while i<n1 and j<n2:
    if left_array[i] <= right_array[j]:
      list[k] = left_array[i]
      i+=1
    else:
      list[k] = right_array[j]
      j+=1
    comp_count+=1
    swap_count+=1
    k+=1
  
  while i<n1:
    list[k] = left_array[i]
    swap_count+=1
    i+=1
    k+=1
  
  while j<n2:
    list[k] = right_array[j]
    swap_count+=1
    j+=1
    k+=1


def merge_sort(list, left, right):
  if left < right:
    mid = left+(right-left)//2

    merge_sort(list, left, mid)
    merge_sort(list, mid+1, right)
    merge(list, left, mid, right)
'''
Both partition and quick_sort pulled from : https://www.geeksforgeeks.org/quick-sort/
'''
def partition(list,low,high):
  global swap_count
  global comp_count

  pivot = list[high]
  i = low-1

  for j in range(low, high):
    if list[j]<=pivot:
      i+=1
      list[i], list[j] = list[j], list[i]
      swap_count+=1
    comp_count+=1
  
  list[i+1], list[high] = list[high], list[i+1]
  swap_count+=1

  return i+1


def quick_sort(list, low, high):
  if low < high:
    pi = partition(list, low, high)

    quick_sort(list, low, pi-1)
    quick_sort(list, pi+1, high)


def near_sort_array(list):
  for i in range(int(len(list)*.05)):
    a = random.randint(0, len(list)-1)
    b = random.randint(0, len(list)-1)
    if a == b:
      a = random.randint(0, len(list)-1)
    list[a], list[b] = list[b], list[a]


def reverse_array(list):
  list.sort(reverse=True)


def header(sort_type, config_type,output_file):
  output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  output_writer.writerow(['algorithm','initial_configuration','MIN_SIZE','MAX_SIZE','TRIALS'])
  output_writer.writerow([sort_type,config_type,MIN_SIZE,MAX_SIZE,TRIALS])
  output_writer.writerow([])
  output_writer.writerow(['size', 'avg_time', 'avg_comps','avg_swaps'])


def generate_filename():
  filename = STUDENT_LASTNAME + '_'
  filename += datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  filename += ".csv"
  return filename


def console_log(message):
  if VERBOSE_OUTPUT:
    print(message)


def main():
  global step_count
  global swap_count
  global comp_count

  with open(generate_filename(), mode='w', newline='') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    #Bubble Sort
    console_log(f"Testing bubble_sort with {TRIALS} trials on arrays sized {MIN_SIZE} to {MAX_SIZE}")
    
    '''
    RANDOM BUBBLE SORT
    '''
    header('bubble_sort','random',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        bubble_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    ALMOST SORTED BUBBLE SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('bubble_sort','almost-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        bubble_sort(list)
        near_sort_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        bubble_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    REVERSE SORTED BUBBLE SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('bubble_sort','reverse-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        bubble_sort(list)
        reverse_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        bubble_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    RANDOM SELECTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    console_log(f"Testing selection_sort with {TRIALS} trials on arrays sized {MIN_SIZE} to {MAX_SIZE}")
    header('selection_sort', 'random', output_file)
    
    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        selection_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    ALMOST SORTED SELECTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('selection_sort','almost-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        selection_sort(list)
        near_sort_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        selection_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    REVERSE SORTED SELECTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('selection_sort','reverse-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        selection_sort(list)
        reverse_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        selection_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    RANDOM INSERTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    console_log(f"Testing insertion_sort with {TRIALS} trials on arrays sized {MIN_SIZE} to {MAX_SIZE}")
    header('insertion_sort', 'random', output_file)
    
    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        insertion_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    ALMOST SORTED INSERTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('insertion_sort','almost-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        insertion_sort(list)
        near_sort_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        insertion_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    REVERSE SORTED INSERTION SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('insertion_sort','reverse-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        insertion_sort(list)
        reverse_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        insertion_sort(list)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    RANDOM MERGE SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('merge_sort','random',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        merge_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    ALMOST SORTED MERGE SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('merge_sort','almost-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        merge_sort(list, 0, len(list)-1)
        near_sort_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        merge_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    REVERSE SORTED MERGE SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('merge_sort','reverse-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        merge_sort(list, 0, len(list)-1)
        reverse_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        merge_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
  
    '''
    RANDOM QUICK SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('quick_sort','random',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        quick_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE
    
    '''
    ALMOST SORTED QUICK SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('quick_sort','almost-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        quick_sort(list, 0, len(list)-1)
        near_sort_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        quick_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE

    '''
    REVERSE SORTED QUICK SORT
    '''
    output_writer.writerow([])
    output_writer.writerow([])
    header('quick_sort','reverse-sorted',output_file)

    size = MIN_SIZE
    while size <= MAX_SIZE:

      sort_time = 0
      sort_steps = 0
      swap_count = 0
      comp_count = 0 

      for t in range(TRIALS):

        # create a list of size elements with values ranging 0..2*size
        list = random.sample(range(0, int(size*2)), size)

        quick_sort(list, 0, len(list)-1)
        reverse_array(list)

        # record time & reset step_count before sorting
        before_time = time.process_time()
        step_count = 0

        quick_sort(list, 0, len(list)-1)

        # calculate & record elapsed time & steps
        sort_time += (time.process_time() - before_time) * 1000000
        sort_steps += step_count
        

      console_log(f"size: {size}")
      output_writer.writerow([size, sort_time/TRIALS, comp_count//TRIALS, swap_count//TRIALS])
      size += STEP_SIZE


if __name__ == '__main__':
  main()

#python sorttest.py