#!/usr/bin/python

import sys

def sum_digits(i,power):
    sum_digs = 0
    j = i
    while j and sum_digs <= i:
        sum_digs += (j % 10)**power
        j /= 10
    return sum_digs

def find_narcs(max_digits):

    print "Searching for narcissistic numbers up to " \
            + str(max_digits) + " digits long:"

    for digits in range(max_digits+1): # 0 to max_digits
        for i in range(int(10**(digits-1)),10**(digits)): # 0,1-9,10-99,100-999...
            if sum_digits(i,digits) == i:
                # found narcissistic number
                print i
     

if __name__ == '__main__':
    if len(sys.argv) == 2:
        max_digits = int(sys.argv[1])
        find_narcs(max_digits)

    else:
        max_digits = int(raw_input("Enter the limit (digits) of integers to search for narcissistic numbers (max recommended 7 or 8): "))
        find_narcs(max_digits)
        
