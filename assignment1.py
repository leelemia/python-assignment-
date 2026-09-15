# ============================================================
# Assignment 1: Python Basics and Data Structures
# Name: Lee
# ============================================================


# ============================================================
# PART 1: Python Introduction and Data Types
# ============================================================

# ------------------------------------------------------------
# Question 1: Personal Information
# ------------------------------------------------------------
print("=== Question 1: Personal Information ===")

name = "Lee"
age = 19
height = 1.70
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

print()

# ------------------------------------------------------------
# Question 2: Identify the Data Types
# ------------------------------------------------------------
print("=== Question 2: Identify the Data Types ===")

name = "Abdurrahman"
age = 25
height = 1.75
is_student = True

print("Value:", name, "-> Data Type:", type(name))
print("Value:", age, "-> Data Type:", type(age))
print("Value:", height, "-> Data Type:", type(height))
print("Value:", is_student, "-> Data Type:", type(is_student))

print()


# ============================================================
# PART 2: Lists
# ============================================================

# ------------------------------------------------------------
# Question 3: Favourite Foods
# ------------------------------------------------------------
print("=== Question 3: Favourite Foods ===")

favourite_foods = ["Pizza", "Injera", "Pasta", "Sushi", "Burger"]

print("Original list:", favourite_foods)
print("First food:", favourite_foods[0])
print("Last food:", favourite_foods[-1])

favourite_foods.append("Salad")
print("List after adding a food:", favourite_foods)

favourite_foods.remove("Pasta")
print("List after removing a food:", favourite_foods)

favourite_foods[0] = "Tacos"
print("List after changing a food:", favourite_foods)

print("Final list:", favourite_foods)

print()

# ------------------------------------------------------------
# Question 4: Student Scores
# ------------------------------------------------------------
print("=== Question 4: Student Scores ===")

scores = [75, 80, 65, 90, 85]

print("All scores:", scores)
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

scores.append(95)
print("Updated scores list:", scores)

print()


# ============================================================
# PART 3: Tuples
# ============================================================

# ------------------------------------------------------------
# Question 5: Days of the Week
# ------------------------------------------------------------
print("=== Question 5: Days of the Week ===")

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("All days:", days)
print("First day:", days[0])
print("Last day:", days[-1])

try:
    days[0] = "Funday"
except TypeError as error:
    print("Error when trying to change a tuple value:", error)
    print("Explanation: Tuples are immutable, meaning their values cannot")
    print("be changed, added, or removed after creation. That is why")
    print("Python raises a TypeError when we try to modify one.")

# Answer: Why is a tuple different from a list?
# A list is mutable (its items can be changed, added, or removed),
# while a tuple is immutable (once created, its items cannot be changed).
# Tuples are usually used for fixed data that should not change,
# while lists are used for data that may need to be updated.

print()


# ============================================================
# PART 4: Sets
# ============================================================

# ------------------------------------------------------------
# Question 6: Remove Duplicate Values
# ------------------------------------------------------------
print("=== Question 6: Remove Duplicate Values ===")

numbers = [1, 2, 3, 4, 2, 5, 3, 6, 1]

numbers_set = set(numbers)

print("Original list:", numbers)
print("Set (duplicates removed):", numbers_set)

print("Explanation: A set can only contain unique values, so when a list")
print("is converted into a set, any duplicate values are automatically removed.")

print()

# ------------------------------------------------------------
# Question 7: Unique Programming Languages
# ------------------------------------------------------------
print("=== Question 7: Unique Programming Languages ===")

languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

languages_set = set(languages)
print("Unique programming languages:", languages_set)

languages_set.add("Django")
print("Set after adding Django:", languages_set)

print()


# ============================================================
# PART 5: Dictionaries
# ============================================================

# ------------------------------------------------------------
# Question 8: Student Profile
# ------------------------------------------------------------
print("=== Question 8: Student Profile ===")

student = {
    "name": "Lee",
    "age": 19,
    "course": "Computer Science",
    "level": "3rd year",
    "skills": ["Python", "HTML", "SQL"]
}

print("Student profile:", student)
print("Student name:", student["name"])

student["email"] = "lee@example.com"
student["level"] = "4th year"
del student["age"]

print("Final student profile:", student)

print()


# ============================================================
# Final Challenge
# ============================================================

# ------------------------------------------------------------
# Question 9: Student Management Data
# ------------------------------------------------------------
print("=== Question 9: Student Management Data ===")

student1 = {
    "name": "John",
    "age": 22,
    "course": "Backend Development",
    "skills": ["Python", "HTML", "Git"]
}

student2 = {
    "name": "Mary",
    "age": 24,
    "course": "Data Analysis",
    "skills": ["Excel", "SQL", "Python"]
}

student3 = {
    "name": "Lee",
    "age": 19,
    "course": "Computer Science",
    "skills": ["Python", "Java", "SQL"]
}

for student_info in (student1, student2, student3):
    print("Name:", student_info["name"])
    print("Age:", student_info["age"])
    print("Course:", student_info["course"])
    print("Skills:", student_info["skills"])
    print("-" * 20)

print()


# ============================================================
# ASSIGNMENT 2: Student Information Manager
# ============================================================

# ------------------------------------------------------------
# Basic variables
# ------------------------------------------------------------
print("=== Assignment 2: Basic Student Variables ===")

student_name = "Lee"
student_age = 19
student_height = 1.70
is_enrolled = True

print("Name:", student_name)
print("Age:", student_age)
print("Height:", student_height)
print("Is enrolled:", is_enrolled)

print()

# ------------------------------------------------------------
# 1. List
# ------------------------------------------------------------
print("=== Assignment 2: List ===")

skills = ["Python", "HTML", "CSS", "JavaScript", "SQL"]

print("First skill:", skills[0])

skills.append("Git")
print("Skills after adding a new item:", skills)

skills.remove("CSS")
print("Skills after removing an item:", skills)

print("Updated skills list:", skills)

print()

# ------------------------------------------------------------
# 2. Tuple
# ------------------------------------------------------------
print("=== Assignment 2: Tuple ===")

favorite_numbers = (7, 10, 25)

print("Second favorite number:", favorite_numbers[1])

print()

# ------------------------------------------------------------
# 3. Set
# ------------------------------------------------------------
print("=== Assignment 2: Set ===")

hobbies = {"Reading", "Gaming", "Football", "Reading"}

print("Hobbies set:", hobbies)

print("Explanation: 'Reading' was entered twice, but since a set only")
print("stores unique values, the duplicate was automatically removed.")

hobbies.add("Chess")
print("Hobbies after adding a new one:", hobbies)

print()

# ------------------------------------------------------------
# 4. Dictionary
# ------------------------------------------------------------
print("=== Assignment 2: Dictionary ===")

student_dict = {
    "name": student_name,
    "age": student_age,
    "height": student_height,
    "is_enrolled": is_enrolled,
    "skills": skills,
    "favorite_numbers": favorite_numbers,
    "hobbies": hobbies
}

print("Student name:", student_dict["name"])
print("Student skills:", student_dict["skills"])

student_dict["country"] = "Ethiopia"
student_dict["age"] = 20

print("Complete student dictionary:", student_dict)

print()

# ------------------------------------------------------------
# Bonus Challenge
# ------------------------------------------------------------
print("=== Assignment 2: Bonus Challenge ===")

bonus_name = "Lee"
bonus_age = 19
favorite_language = "Python"

bonus_info = {
    "name": bonus_name,
    "age": bonus_age,
    "favorite_language": favorite_language
}

print(f"Hello {bonus_info['name']}!")
print(f"You are {bonus_info['age']} years old.")
print(f"Your favorite programming language is {bonus_info['favorite_language']}.")

print()

# ------------------------------------------------------------
# Short Explanation: List vs Tuple vs Set vs Dictionary
# ------------------------------------------------------------
print("=== Short Explanation: List vs Tuple vs Set vs Dictionary ===")
print("List: An ordered, changeable collection that allows duplicate values.")
print("      Example: [1, 2, 3, 2]")
print("Tuple: An ordered, unchangeable (immutable) collection that allows")
print("       duplicate values. Example: (1, 2, 3, 2)")
print("Set: An unordered collection that does not allow duplicate values.")
print("     Example: {1, 2, 3}")
print("Dictionary: A collection of key-value pairs, where each key is unique.")
print("            Example: {'name': 'Lee', 'age': 19}")
