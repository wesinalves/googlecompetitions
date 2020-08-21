'''
Code for google kickstart
Round A - Even Digits
Wesin Ribeiro
2020

##############
Problem
##############
This calculator only has a display, a plus button, and a minus button.
The integer N is displayed on the calculator display.
Pressing the plus button increases the current number displayed on the calculator
display by 1. Similarly, pressing the minus button decreases the current number
displayed on the calculator display by 1.
The calculator does not display any leading zeros.
Determine the minimum number of button presses to make the calculator
display an integer with no odd digits.

##############
Comments
##############
a number is even if the module operation by 2 is 0.
How to check if all numbers are even?

'''
def check_evens(digits, start_search):
    '''check if all digits are even'''
    even = True
    for d in range(start_search, len(str(digits))):
        if (int(str(digits)[d]) % 2) != 0:
            even = False
            start_search = d
            return even, start_search
    return even, start_search

def main():
    '''Main function'''
    tests = int(input())
    for t in range(tests):
        ans = 0
        button_increase = 0
        button_decrease = 0
        n = int(input())
        all_even, start = check_evens(n, 0)
        start_increase = start
        start_decrease = start
        while not all_even:
            button_increase += 1
            all_even, start_increase = check_evens(n + button_increase, start_increase)
            if all_even:
                ans = button_increase
                break
            button_decrease += 1
            all_even, start_decrease = check_evens(n - button_decrease, start_decrease)

        if all_even and ans == 0:
            ans = button_decrease


        print('Case #{}: {}'.format(t+1, ans))

main()