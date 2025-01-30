programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          "Loop": "A program that runs over and over again.",
                          }

print(programming_dictionary)
empty_dictionary = {}
# Loop through dictionaries
for key in programming_dictionary:
    print(key)

for keys, values in programming_dictionary.items():
    print(f"{keys}: {values}")

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key, value in student_scores.items():
    if value > 90:
        student_grades[key] = "Outstanding"
    elif value > 80:
        student_grades[key] = "Exceeds Expectations"
    elif value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"
print(student_grades)
