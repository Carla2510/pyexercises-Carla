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
# -
# -
# -
# -

# 1. In:
# 2. Process, problem by problem:
# 3. Out:
# 4. How I decide which word is the last name:


# Your code below

import os

INPUT_FILE = "names.txt"
OUTPUT_FILE = "cleaned_names.txt"


def clean_and_parse_line(raw_line: str) -> tuple[str, str] | None:
    """Cleans whitespace and casing, returning (first_name, last_name), or None if line is blank."""
    words = raw_line.strip().split()
    if not words:
        return None

    # Handle standard case (at least First and Last) or single token
    if len(words) == 1:
        first_name = ""
        last_name = words[0].capitalize()
    else:
        first_name = " ".join(word.capitalize() for word in words[:-1])
        last_name = words[-1].capitalize()

    return first_name, last_name


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' was not found in the current folder.")
        return

    unique_names = set()
    raw_line_count = 0

    with open(INPUT_FILE, mode="r", encoding="utf-8") as infile:
        for line in infile:
            raw_line_count += 1
            parsed = clean_and_parse_line(line)
            if parsed is not None:
                unique_names.add(parsed)

    # Sort primarily by last name (case-insensitive), secondarily by first name
    sorted_names = sorted(
        unique_names,
        key=lambda person: (person[1].lower(), person[0].lower()),
    )

    with open(OUTPUT_FILE, mode="w", encoding="utf-8") as outfile:
        for first, last in sorted_names:
            full_name = f"{first} {last}".strip()
            outfile.write(full_name + "\n")

    print(f"Processing complete:")
    print(f"  - Raw lines read from '{INPUT_FILE}': {raw_line_count}")
    print(f"  - Cleaned, sorted lines written to '{OUTPUT_FILE}': {len(sorted_names)}")
    if sorted_names:
        first_entry = f"{sorted_names[0][0]} {sorted_names[0][1]}".strip()
        last_entry = f"{sorted_names[-1][0]} {sorted_names[-1][1]}".strip()
        print(f"  - First entry: {first_entry}")
        print(f"  - Last entry:  {last_entry}")


if __name__ == "__main__":
    main()