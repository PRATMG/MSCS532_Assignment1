# MSCS532_Assignment 1
# Prakash_Tamang
# Sat, Aug 31
#Insertion_sort.py

def insertion_sort_decreasing_order(arr):

    #loop through each element
    for i in range(1, len(arr)):
        #save the current element as 'current_value'
        current_value = arr[i]
        #set 'pos' to the index before the current element
        pos = i -1
        #move elements that are less than 'current_value' to one position ahead
        while pos >= 0 and arr[pos] < current_value:
            arr[pos + 1] = arr[pos]
            #go one step left
            pos -= 1
        
        # Place the 'current_value' in its correct position.
        arr[pos + 1] = current_value
