"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the list from exercise 4.0
# 2. Process: the program will reorder the list in four different ways, using different methods that either modify the original list or create a new one
# 3. Out: four different orders of the list, and the original list at the end to prove it has not been modified
# 4. My four orders, and which ones modify the original: the order : smallest to largest, largest to smallest, backwards, and as text. The first two orders modify the original list, while the last two create new lists without modifying the original.


# Your code below

my_list = [4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1]

order_1 = my_list.copy()
order_1.sort()

order_2 = sorted(my_list, reverse=True)

order_3 = my_list[::-1]

order_4 = sorted(my_list, key=str)

print("1. Smallest to largest:", order_1)
print("2. Largest to smallest:", order_2)
print("3. Backwards:", order_3)
print("4. As text:", order_4)

print("Original:", my_list)
