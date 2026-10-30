"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: nothing type by the user, only the code will give us the answer
# 2. Process: the program will manipulate the dictionary in various ways
# 3. Out: the name, age, city, and country of the person, and the remaining fields after removing the age field
# 4. My object, my five fields, and why those: I described a person, and I chose the fields name, age, city, and country because they are basic information that is often needed to describe a person. I also chose to remove the age field to demonstrate how to remove a field from a dictionary.


# Your code below

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
country = input("Enter your country: ")

print("My name is",name)
print("My age is",age)
print("My city is",city)
print("My country is",country)


person = {
    "name": name,
    "age": age,
    "city": city,
    "country": country,
}   

print("The person's name is:", person["name"])
print("The person's age is:", person["age"])
print("The person's city is:", person["city"])
print("The person's country is:", person["country"])

person_age = person.pop("age")
print("The person's age has been removed. The removed age is:", person_age)
print("The person's remaining fields are:", person)
