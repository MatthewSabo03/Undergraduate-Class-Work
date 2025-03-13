#Name: Matthew Sabo

import time
import csv
import random

def lin_Search(list, target):
    #Sets variable to track position in list and starts timer
    i = 0
    start_time = time.time()
    
    #Loops until i is at the end of the list
    while i < len(list):
        
        #Checks if the current value in list is the target
        if list[i] == target:
            end_time = time.time()
            run_time = end_time - start_time
            return run_time
        
        #Runs if false
        else:
            i += 1
    end_time = time.time()
    run_time = end_time - start_time
    return run_time


def bin_Search(list, target):
    #Sets variables to use in search
    #Low is the lowest index in the list, High is highest index in list
    list.sort()
    low = 0
    high = len(list)-1
    mid = 0
    start_time = time.time()
    while low <= high:
        #Sets mid to the center position in the list
        mid = (high+low)//2
        
        #Target is less than current value of the list. Moves right
        if list[mid] < target:
            low = mid+1
        
        #Target is greater than the current value of the list. Moves left
        elif list[mid] > target:
            high = mid-1
        
        #Target is at the middle of the list
        else:
            end_time = time.time()
            run_time = end_time - start_time
            return run_time
    
    #Runs if the while loop completed
    end_time = time.time()
    run_time = end_time - start_time
    return run_time

#Toggle true or false to test either search Algorithm
binary_search = False
linear_search = True

#Sets up variables for search algorithms
i=0 
num_trials = 50
total_search_time = 0
min_size = 10000
max_size = 1000000
step_size = 10000

#Sets up the output .csv file
with open('Search_Algorithm_Output.csv','w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['array_size', 'run_time'])

    #Main while loop to run through trials
    while i<=num_trials:
        list = (random.sample(range(1,max_size),min_size))
        target = 5
        
        if binary_search is True:
            run_time = bin_Search(list, target)*1000
        if linear_search is True:
            run_time = lin_Search(list, target)*1000
        
        total_search_time += run_time
        writer.writerow((len(list),run_time))
        
        min_size+=step_size
        if min_size>max_size:
            break
        i+=1 

    total_search_time /= num_trials
    writer.writerow(("Average Search Time(ms) :",total_search_time))

#python sabo_searchtests.py