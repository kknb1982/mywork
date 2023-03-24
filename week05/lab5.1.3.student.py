# Creating a dictionary to store: student name, coureses and grades
# Uses code by Andrew Beatty
# Author: Kirstin Barnett

student = {
    "name": "Mary",
    "modules": [
        {"course_name": "Programming",
        "grade": 45},
        {"course_name": "History",
        "grade": 99}
    ]
}

print (f'Student: {student["name"]}')

for module in student["modules"]:
    print(f'    {module["course_name"]}     {module["grade"]}' )

