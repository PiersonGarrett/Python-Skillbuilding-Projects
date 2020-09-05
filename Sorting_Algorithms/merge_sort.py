# Implementation of Merge Sort in Python

# Merge Sort uses recursion to sort a list. Recursion allows us to reduce problems to their simplest form (base case) to which we can solve and then rebuilt the solution to the original problem. Sorting lists this way exploits the optimal substructure property of these types of problems. 

# A merge sort works by taking larger array and splitting it in half (as close as possible)
# the ncall merge sort on those halfs. We repeat this until we have an array with an element
# at this point sorting is trival so we sort the two element array and return the result. We then
# add the now sorted halfs back together using the first element of one of the arrays to determine 
# how we append them. We re[eat this until we end up with a sorted list.
import math

def merge(leftarr,rightarr):
    # Recombine left and right array so they are sorted
    # There are a few cases we need to check when recombining:
    #   1) Is the first element of the left array greater than the last element of the right array
    #   2) Is the last element of the left array less than the first element of the right array
    #   3) Otherwise we need to iterate through the arrays to recombine them :(
    #print(leftarr)
    #TODO: keep getting nunetype error

    if leftarr[0] > rightarr[-1]:
        rightarr.extend(leftarr)
        return rightarr
    elif leftarr[-1] < rightarr[0]:
        leftarr.extend(rightarr)
        return leftarr
    else:
        # We can merge the two lists using the following method:
            # Keep track of a index for the left array and right array, start both at 0th index
            # Compare the first elements of both lists, add the smaller element to a temp array
            # and then advance the array index of where the element came from. Repeat this until
            # you reach then end of one of the list then add the rest of the elements to the end
            # of the temp array
        leftindex, rightindex = 0,0
        temp = []
        
        # print("left")
        # print(leftarr)
        # print("right")
        # print(rightarr)
        
        while(leftindex <= len(leftarr) - 1 and rightindex <= len(rightarr) - 1):
            if leftarr[leftindex] < rightarr[rightindex]:
                temp.append(leftarr[leftindex])
                leftindex += 1
            elif leftarr[leftindex] > rightarr[rightindex]:
                temp.append(rightarr[rightindex])
                rightindex += 1
            elif leftarr[leftindex] == rightarr[rightindex]:
                temp.append(leftarr[leftindex])
                temp.append(rightarr[rightindex])
                leftindex += 1
                rightindex += 1
            
            # print("left index: {}".format(leftindex))
            # print("right index: {}".format(rightindex))
            # print(temp)


        
        if leftindex >= len(leftarr):
            print(rightarr[rightindex:])
            temp.extend(rightarr[rightindex:])
        elif rightindex >= len(rightarr):
            temp.extend(leftarr[leftindex:])
        return temp

def merge_sort(num_list):
    
    # Check to see if we can split array further (less than two elements) if so return sorted array
    if len(num_list) <= 1:
        return num_list
    # split the array into two pieces
    split_index = int(math.floor(len(num_list)/2))
    leftarr = num_list[:split_index]
    rightarr = num_list[split_index:]
   

    # call merge sort on both halfs refered to as left and right from now on
    leftarr = merge_sort(leftarr)
    rightarr = merge_sort(rightarr)

    # merge back together
    num_list = merge(leftarr,rightarr)

    return num_list

if __name__ == '__main__':
    l = [5,32,15,4,7,11,56,56]
    print(merge_sort(l))
