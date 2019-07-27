'''
Problem 4
1 point possible (ungraded)

Implement a function called closest_power that meets the specifications below.
'''

def closest_power(base, num):

    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exponent=1
    while base**exponent < num:
        exponent +=1
    larger=base*exponent
    smaller= base**(exponent-1)
    if abs(larger-num) >= abs(smaller-num):
        print (exponent-1)
        return exponent-1
    else:
        print(exponent)
        return exponent

closest_power(3,12) #returns 2
closest_power(4,12) #returns 2
closest_power(4,1)  #returns 0
