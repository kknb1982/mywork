import json
students = []
FILENAME = "studentdata.json"
def write_dict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj,f)

def read_dict():
    with open(FILENAME) as f:
        return json.load(f)

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(s) Save students")
    print ("\t(l) Load students")
    print ("\t(q) Quit")
    choice = input ("Please select an option (a/v/s/l/q):").strip()
    
    return choice

def do_add(students):
    student = {}
    student["name"] = input ("Enter name: ")
    student["modules"] = read_modules()
    students.append(student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first module name (blank to quit):").strip()
 
    while module_name !="":
        module = {}
        module["name"]= module_name
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
    # now read the next module name
        module_name = input("\tEnter next module name (blank to quit):")
    return modules

def display_modules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print (f"\t{module['name']} \t {module['grade']}")

def do_view(students):
    for student in students:
        print(student["name"])
        print (display_modules(student["modules"]))
 
def do_save(students):
    write_dict(students)
    print("Students saved")

def do_load(students):
    return read_dict()
# Main programme  

choice = display_menu()
while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice == "s":
        do_save(students)
    elif choice == "l":
        do_load(students)
    else:
        print ("\n \n Please choose either a, v, s, l or q")
    choice = display_menu()
