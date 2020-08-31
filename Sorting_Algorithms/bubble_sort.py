# Implementation of Bubble Sort in Python
# One of the first sorts you learn in introductory classes in Computer Science
# start with the first element of a list of numbers, if it is larger than the 
# next element in the list keep it, otherwise swap the elements and continue 
# checking the rest of the elements in the list.
# Repeat this until the entire list is sorted.


def bubble_sort(number_list):
    
    # Iterate through each element in the list and perform bubble sort
    for element_index in range(len(number_list)):
        for loop_element_index in range(len(number_list)):
            if number_list[element_index] <= number_list[loop_element_index]:
                # swap elements
                number_list[element_index], number_list[loop_element_index] = number_list[loop_element_index], number_list[element_index] 

    print(number_list)

if __name__ == '__main__':
    number_list = [3,2,3]
    print(number_list)
    bubble_sort(number_list)