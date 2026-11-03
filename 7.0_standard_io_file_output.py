"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:name, last name, date of birth, student ID
# 2. Process:enter the data, check if the file exists, if not create it and write the header, then append the new entry to the file
# 3. Out, file name and columns:student data.csv with columns: First Name, Last Name, Date of Birth, Student ID
# 4. Why these columns, and what this file is for:to collect basic student information for record-keeping and administrative purposes. Once the file has two hundred rows, it can be used for generating reports, tracking student demographics, and managing student records efficiently.


# Your code below
print("Please enter the following information for the new entry:")
first_name = input("First Name: ")
last_name = input("Last Name: ")
birth_year = input("Date of birth (DD/MM/YYYY): ")
student_id = input("Student ID: ")

with open("7.0_student_data.csv", "a", newline="") as file:
    file.write("First Name,Last Name,Date of Birth,Student ID\n")
    file.write(first_name + "," + last_name + "," + birth_year + "," + student_id + "\n")

print("Data saved successfully!")
