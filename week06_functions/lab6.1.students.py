students = []

def display_menu():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input ("Please select an option (a/v/q): ").strip ()
    
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

def diplay_modules(modules):
    print ("\tName \tGrade")
    for module in modules:
        print (f"\t{module['name']} \t {module['grade']}")

def do_view(students):
    for student in students:
        print(student["name"])
        print (display_modules(student["modules"]))
 

# Main programme  

choice = display_menu()
while choice != "q":
    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    else:
        print ("\n \n Please choose either a, v or q")
        choice = display_menu()
