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


if __name__ == "__main__":
    #create a list of example numbers
    arr = [14,17, 12, 8,1, 29, 10]

    #sort the list in decreassing order
    insertion_sort_decreasing_order(arr)
    #print the sorted list
    print("Insetion sort in decreasing order: ", arr)
