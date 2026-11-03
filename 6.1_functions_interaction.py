"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process, function by function:
# 3. Out:
# 4. The question my fourth function answers:


# Your code below

def filter_positive_numbers(numbers: list[int | float]) -> list[int | float]:
    """Returns a list containing only numbers strictly greater than zero."""
    return [num for num in numbers if num > 0]


# Function 2: One job -> summing
def sum_numbers(numbers: list[int | float]) -> int | float:
    """Returns the sum of all elements in the given list."""
    return sum(numbers)


# Function 3: One job -> counting
def count_numbers(numbers: list[int | float]) -> int:
    """Returns the number of elements in the given list."""
    return len(numbers)


# Function 4: Orchestrator -> uses the other three
def calculate_average_of_positives(numbers: list[int | float]) -> float:
    """Calculates the mean of all positive numbers in the list."""
    positives = filter_positive_numbers(numbers)
    if not positives:
        return 0.0
    total = sum_numbers(positives)
    count = count_numbers(positives)
    return total / count



# Individual tests for each small function
test_data = [10, -5, 20, -1, 30]

print("--- Individual Tests ---")
print("1. filter_positive_numbers:", filter_positive_numbers(test_data))
print("2. sum_numbers:", sum_numbers([10, 20, 30]))
print("3. count_numbers:", count_numbers([10, 20, 30]))

print("\n--- Fourth Function Combined Test ---")
result = calculate_average_of_positives(test_data)
print(f"Average of positives: {result}")
