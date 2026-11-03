"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
def greet(items):
    if not items:
        return "Hello! Your list is currently empty."
    return f"Hello! Your list has {len(items)} items, with a total sum of {sum(items)}."


list1 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1]
list2 = [10, 20, 30]
list3 = []


res1 = greet(list1)
res2 = greet(list2)
res3 = greet(list3)

# Displaying the results
print(res1)
print(res2)
print(res3)