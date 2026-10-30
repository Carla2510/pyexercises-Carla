"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the user will be asked if he wants to continue or not
# 2. Process: the program will keep asking the user if he wants to continue until the user answers "no" or until the maximum number of attempts is reached
# 3. Out: a summary of the number of attempts, the number of "yes" answers, the number of invalid answers, and the reason why the loop stopped
# 4. My stop condition, my attempt limit, my summary: stop condition is when the user answers "no", maximum number of attempts is 5, and the summary contains the number of attempts, the number of "yes" answers, the number of invalid answers, and the reason why the loop stopped.


# Your code below

MAX_ATTEMPTS = 5

attempts = 0
yes_count = 0
invalid_count = 0
reason = ""

while attempts < MAX_ATTEMPTS:
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
    attempts += 1

    if answer == "no":
        reason = "the user answered no"
        break
    elif answer == "yes":
        yes_count += 1
        print("You chose to continue.")
    else:
        invalid_count += 1
        print("Invalid input. Please answer 'yes' or 'no'.")
else:
    reason = "the limit of " + str(MAX_ATTEMPTS) + " attempts was reached"
    print("Maximum number of attempts reached, the program stops.")

print("--- Summary ---")
print("Attempts:", attempts)
print("Yes answers:", yes_count)
print("Invalid answers:", invalid_count)
print("Loop stopped because", reason)
  