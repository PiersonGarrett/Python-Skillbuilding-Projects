# Sieve of Eratosthenes, an effcient way of finding all the prime numbers below 10 million or so
# We first generate a list of numbers from 2 to n. We then, starting with the first number,
# mark all the multiples in a seperate list. After we go through all of the numbers in the first
# list we can refer to the second list to find all the prime numbers between 2 and n.


def eratosthenes_generator(n):
   # Generate list of numbers from 2 to n and boolean list to keep track of prime numbers
    number_list = [i+2 for i in range(n-1)]
    boolean_list = [0]*len(number_list)
    prime_list = []
    
    # starting at 2 go through each number in the first list
    for num in number_list:
        # if the number has been marked as a multiple skip it
        if boolean_list[num-2]  == 0:
            multiple_counter = 2
            # Until we reach a number outside of our list mark the multiples of the currernt number num
            while((num * multiple_counter) - 2 <= len(number_list)-1):
                boolean_list[num * multiple_counter - 2] += 1
                multiple_counter += 1
    
    # Create a list of the prime numbers using the boolean list and number list
    for index,boolean in enumerate(boolean_list):
        if boolean == 0:
            prime_list.append(number_list[index])
    
    return prime_list

if __name__ == '__main__':
    print(eratosthenes_generator(21))