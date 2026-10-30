"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one number choose from the user
# 2. Process: the program will check if the number is odd or even and print the result for each number from 1 to N
# 3. Out: one line per number from 1 to N, saying whether it is odd or even
# 4. What happens on 0, on a negative number, on a very large number: the program will print a message saying that N must be at least 1 for 0 and negative numbers, and for very large numbers (greater than 1000), it will print a message saying that N is too large and ask the user to enter 1000 or less.


# Your code below

n = int(input("Enter a number N: "))

if n < 1:
    print("N must be at least 1.")
elif n > 1000:
    print("N is too large, please enter 1000 or less.")
else:
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")
