"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -Problem 1: Blank / empty lines scattered inside the file (e.g., between Hopper and Turing, and Rossum and Liskov).
# - Problem 2: Leading spaces / indentation at the beginning of some lines (e.g., '  alan TURING', '  linus torvalds').
# - Problem 3: Inconsistent casing across the file:
#              * Some first names are lowercase ('ada', 'grace'), while others are uppercase ('GUIDO').
#              * Some last names are in ALL CAPS ('LOVELACE', 'TURING', 'JOHNSON', 'LISKOV'),
#                while others are in lowercase ('hopper', 'hamilton', 'torvalds', 'van rossum').
# - Problem 4: Irregular word count per line: most lines contain two words (first and last name),
#              but one line contains three words with a particle ('GUIDO van rossum').
# 

# 1. In: a text file with names, one per line, with inconsistent formatting (whitespace, casing, and word count).
# 2. Process, problem by problem: lank lines: checked with line.strip(); if empty, the line is skipped immediately.
#    - Leading whitespace: stripped using .strip() or .split(), which eliminates unwanted spaces.
#    - Inconsistent casing: normalized using .title() (or .capitalize()) on first names and last names,
#      ensuring standard Title Case (e.g., 'Ada Lovelace').
#    - Multi-word names: if a line contains more than 2 words (like 'GUIDO van rossum'),
#      the first token is taken as the first name, and the remaining tokens form the compound last name.
#    - Sorting: sorted alphabetically from A to Z based on the last name in lowercase.
# 3. Out: A new file named 'cleaned_names.txt' containing exactly 8 properly formatted lines,
#    sorted by last name from A to Z, without modifying 'names.txt'.
# 4. How I decide which word is the last name: When splitting a standard line into words, Western naming order puts the first name first
#    (index 0) and the family name at the end (index -1, or all words after index 0 for compound
#    names such as 'van Rossum'). We sort by comparing the last name component in lowercase
#    so that capitalization differences do not distort the alphabetical order.


# Your code below

"""
Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

# What is wrong with names.txt (found by reading it, not by guessing):
# - Problem 1: Blank / empty lines scattered inside the file (e.g., between Hopper and Turing, and Rossum and Liskov).
# - Problem 2: Leading spaces / indentation at the beginning of some lines (e.g., '  alan TURING', '  linus torvalds').
# - Problem 3: Inconsistent casing across the file:
#              * Some first names are lowercase ('ada', 'grace'), while others are uppercase ('GUIDO').
#              * Some last names are in ALL CAPS ('LOVELACE', 'TURING', 'JOHNSON', 'LISKOV'),
#                while others are in lowercase ('hopper', 'hamilton', 'torvalds', 'van rossum').
# - Problem 4: Irregular word count per line: most lines contain two words (first and last name),
#              but one line contains three words with a particle ('GUIDO van rossum').

# 1. In:
#    A text file named 'names.txt' containing 10 raw lines (including empty lines),
#    with whitespace, case inconsistencies, and 8 computing pioneers' names.

# 2. Process, problem by problem:
#    - Blank lines: checked with line.strip(); if empty, the line is skipped immediately.
#    - Leading whitespace: stripped using .strip() or .split(), which eliminates unwanted spaces.
#    - Inconsistent casing: normalized using .title() (or .capitalize()) on first names and last names,
#      ensuring standard Title Case (e.g., 'Ada Lovelace').
#    - Multi-word names: if a line contains more than 2 words (like 'GUIDO van rossum'),
#      the first token is taken as the first name, and the remaining tokens form the compound last name.
#    - Sorting: sorted alphabetically from A to Z based on the last name in lowercase.

# 3. Out:
#    A new file named 'cleaned_names.txt' containing exactly 8 properly formatted lines,
#    sorted by last name from A to Z, without modifying 'names.txt'.

# 4. How I decide which word is the last name:
#    When splitting a standard line into words, Western naming order puts the first name first
#    (index 0) and the family name at the end (index -1, or all words after index 0 for compound
#    names such as 'van Rossum'). We sort by comparing the last name component in lowercase
#    so that capitalization differences do not distort the alphabetical order.

# --- CHECK IT YOURSELF ---
# - Lines in 'names.txt': 10 lines (8 names + 2 empty lines).
# - Lines in 'cleaned_names.txt': 8 lines.
# - Difference: Exactly 2 lines fewer because the 2 blank lines are eliminated.
# - First person in sorted list: Margaret Hamilton (H)
# - Last person in sorted list: Guido van Rossum (V) [or Alan Turing if sorted strictly on Rossum]
"""

import os

INPUT_FILE = "names.txt"
OUTPUT_FILE = "cleaned_names.txt"


def clean_and_parse_line(raw_line: str) -> tuple[str, str] | None:
    """
    Cleans leading/trailing whitespace and normalizes casing.
    Returns a tuple (first_name, last_name), or None if the line is empty.
    """
    cleaned_line = raw_line.strip()
    if not cleaned_line:
        return None

    words = cleaned_line.split()

    if len(words) == 1:
        first_name = ""
        last_name = words[0].title()
    elif len(words) == 2:
        first_name = words[0].title()
        last_name = words[1].title()
    else:
        # Handles 3 words or more, e.g. "GUIDO van rossum"
        first_name = words[0].title()
        # Keep particles like 'van', 'de', 'von' lowercase or format as Title Case
        particles = {"van", "von", "de", "del", "du"}
        last_name_parts = [
            w.lower() if w.lower() in particles else w.title()
            for w in words[1:]
        ]
        last_name = " ".join(last_name_parts)

    return first_name, last_name


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' was not found in the current folder.")
        print("Please create 'names.txt' and paste your raw names inside.")
        return

    cleaned_entries = []
    raw_line_count = 0

    with open(INPUT_FILE, mode="r", encoding="utf-8") as infile:
        for line in infile:
            raw_line_count += 1
            parsed = clean_and_parse_line(line)
            if parsed is not None:
                cleaned_entries.append(parsed)

    # Sort alphabetically by last name (case-insensitive)
    sorted_entries = sorted(
        cleaned_entries,
        key=lambda person: (person[1].lower(), person[0].lower())
    )

    # Write results to the new file without modifying the original
    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as outfile:
        for first, last in sorted_entries:
            full_name = f"{first} {last}".strip()
            outfile.write(full_name + "\n")

    print("=== Processing Summary ===")
    print(f"Lines read from '{INPUT_FILE}': {raw_line_count}")
    print(f"Lines written to '{OUTPUT_FILE}': {len(sorted_entries)}")
    print(f"Difference: {raw_line_count - len(sorted_entries)} blank lines removed.\n")

    print("Output preview:")
    for first, last in sorted_entries:
        print(f"  - {first} {last}")


if __name__ == "__main__":
    main()
    