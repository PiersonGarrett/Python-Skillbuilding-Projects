# 08/30/2020 Credit Card Validator
# This program takes in a credit card number and uses the Luhn algorithm and the last digit of the card number to check the card.
# Credit cards have 16 numbers, the first 6 are from the institution that distributes the card, the remaining 9 identify the individual account associated with the card. The Luhn algorithm takes in the first 15 digits and and returns one digit which is then checked for equality with the 16th digit, if this is true the card could be valid (this is more for data entry error than actual security because anyone familiar with Luhn's algorithm can generate fake numbers)
import math
def check_card(credit_card_number):
    # seperate digits and store in array
    digit_arr = []
    for digit in str(credit_card_number):
        digit_arr.append(int(digit))
    
    # Create new array of the first n-1 digits and reverse if to ease future steps
    check_sum_arr = digit_arr[0:len(digit_arr)-1]
    check_sum_arr.reverse()

    # Double every other digit
    for index in range(len(check_sum_arr)):
        print(index)
        if index % 2 == 0:
            check_sum_arr[index] *= 2
        if check_sum_arr[index] > 9:
           digits =  [int(digit) for digit in str(check_sum_arr[index])] 
           check_sum_arr[index] = sum(digits)

    # Calculate check sum
    check_sum = (sum(check_sum_arr) * 9) % 10

    return check_sum == digit_arr[-1]



if __name__ == '__main__':
    print(check_card(79927398713))