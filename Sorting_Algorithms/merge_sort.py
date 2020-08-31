# Implementation of Merge Sort in Python

# Merge Sort uses recursion to sort a list. Recursion allows us to reduce problems to their simplest form (base case) to which we can solve and then rebuilt the solution to the original problem. Sorting lists this way exploits the optimal substructure property of these types of problems. 

# A merge sort works by taking larger array and splitting it in half (as close as possible)
# the ncall merge sort on those halfs. We repeat this until we have an array with an element
# at this point sorting is trival so we sort the two element array and return the result. We then
# add the now sorted halfs back together using the first element of one of the arrays to determine 
# how we append them. We re[eat this until we end up with a sorted list.
def merge(leftarr,rightarr):
    # Recombine left and right array so they are sorted
    # There are a few cases we need to check when recombining:
    #   1) Is the first element of the left array greater than the last element of the right array
    #   2) Is the last element of the left array less than the first element of the right array
    #   3) Otherwise we need to iterate through the arrays to recombine them :(
        
    pass
def merge_sort(num_lists):
    # Check to see if we can split array further (less than two elements) if so return sorted array
    
    # split the array into two pieces

    # call merge sort on both halfs refered to as left and right from now on

   

    return num_lists

if __name__ == '__main__':
    print("hello")