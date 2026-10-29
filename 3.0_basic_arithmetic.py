"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:resultat of calcul
# 2. Process:the code give us the answer of all four operations
# 3. Out:give us the answer
# 4. What happens when the second number is zero, and why:we have to create an another variable to adjust it 


# Your code below
number_1 =int(input("Enter number 1: "))
number_2 =int(input("Enter number 2: "))

print("The number 1 is : ", number_1)
print("The number 2 is : ", number_2)

# addition of two numbers
sum = number_1 + number_2
print("The sum of two number is: ", sum)

#diffenrence of two numbers
diff = number_2 - number_1
print("the difference of two numbers is: ", diff)

#product of two numbers
product = number_1 * number_2
print("the product of two number is: ", product)

#division of two numbers
if number_2!=0:
    div = number_1 / number_2
    print ("the division between two numbers is : ", div)
else:
    print ("the second number is", 0)

