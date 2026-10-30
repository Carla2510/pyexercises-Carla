"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: one sentence from the user
# 2. Process: the program will transform the sentence in four different ways
# 3. Out: the sentence transformed in four different ways
# 4. My four transformations, and when each is useful: it is useful to remove spaces at the beginning and end of a sentence, to make all letters lowercase, to make all letters uppercase, and to replace spaces with underscores.


# Your code below

sentence = input("Enter a sentence: ")
print("[" + sentence.strip() + "]")
print("[" + sentence.lower() + "]")
print("[" + sentence.upper() + "]")
print("[" + sentence.replace(" ", "_") + "]")