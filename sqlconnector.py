import mysql.connector as mysql
import employees as emp
import proj


def printData(obj):
    
    obj.cursor.execute(f"Select * from {obj.table_name};")
    data = obj.cursor.fetchall

    for i in obj.colums:
        print(data)

        
conn = mysql.connect(
    host = "localhost" ,
    user = "root" ,
    password = "Pp7004554599" ,
    database = "EMS"
    )

cursor = conn.cursor()

employee = emp.customer(cursor)
project = proj.project(cursor)


while(True):
    print("1 : Create Table")
    print("2 : Add Employee")
    print("3 : Delete Employee")
    print("4 : Update Employee")
    print("5 : Add Project")
    print("6 : Delete Project")
    print("7 : Update Project")
    print("8 : Show employees")
    print("9 : Show projects")
    print("10 : Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        employee.createTable()
        project.createTable()
        print("Tables created")

    if choice == 2:
            employee.id = int(input("Enter employee id: "))
            employee.name = input("Enter employee name: ")
            employee.salary = int(input("Enter salary: "))
            employee.age = int(input("Enter age: "))

            employee.add_employee()
            print("Employee inserted.")
    
    if choice == 3:
         employee.id = int(input("Enter employee id: "))
         employee.delete_employee()
         print("Employee deleted")

    if choice == 4:
        employee.id = int(input("Enter new id: "))
        employee.name = input("Enter new name")
        employee.salary = int(input("Enter new salary"))
        employee.age = int(input("Enter new age"))

        employee.update()
        print("Employee updated")

    if choice == 5:
        project.name = input("Enter project name")
        project.duration = input("Enter the duration")
        project.id = int(input("Enter project id"))
        project.budget = int(input("Enter project budget"))
        project.status = input("Enter status of the project")
        project.emp_id = input("Enter the employee id")

        project.add_project()
        print("Project added")

    if choice == 6:
        project.id = int(input("Enter project id to delete"))
        project.delete_project()
        print("Project deleted")

    if choice == 7:
        project.name = input("Enter updated project name")
        project.duration = input("Enter updated duration")
        project.id = int(input("Enter updated id"))
        project.budget = int(input("Enter updated project budget"))
        project.status = input("Enter updated status of the project")
        project.emp_id = input("Enter the updated employee id")

        project.add_project()
        print("Project added")

    if choice == 8:
        print("Employee table: ")
        printData(employee)

    if choice == 9:
        print("Project table: ")
        printData(project)
