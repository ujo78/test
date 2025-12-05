import mysql.connector as mysql
from employees import *
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

emp = employee(cursor)
project = proj.project(cursor)


while(True):
    print("1 : Create Table")
    print("2 : Add Employee")
    print("3 : Delete Employee")
    print("4 : Update Employee")
    print("5 : Add Project")
    print("6 : Delete Project")
    print("7 : Update Project")
    print("8 : Sort Employees")
    print("9 : Search Employee")
    print("10 : Sort Projects")
    print("11 : Search Project")
    print("12 : Search Project")
    print("13 : Search Project")
    print("14 : Display Employee Table")
    print("15 : Display Project Table")
    
    print("16 : Exit")

    choice = int(input("Enter your choice"))

    if choice == 1:
        emp.createTable()
        project.create_table()
        print("Tables created")

    if choice == 2:
            emp.id = int(input("Enter employee id: "))
            emp.name = input("Enter employee name: ")
            emp.salary = int(input("Enter salary: "))
            emp.age = int(input("Enter age: "))

            emp.add_employee()
            print("Employee inserted.")
    
    if choice == 3:
         emp.id = int(input("Enter employee id: "))
         emp.delete_employee()
         print("Employee deleted")

    if choice == 4:
        emp.id = int(input("Enter new id: "))
        emp.name = input("Enter new name")
        emp.salary = int(input("Enter new salary"))
        emp.age = int(input("Enter new age"))

        emp.update()
        print("Employee updated")

    if choice == 5:
        project.name = input("Enter project name")
        project.duration = int(input("Enter the duration"))
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
        project.duration = int(input("Enter updated duration"))
        project.id = int(input("Enter updated id"))
        project.budget = int(input("Enter updated project budget"))
        project.status = input("Enter updated status of the project")
        project.emp_id = input("Enter the updated employee id")

        project.add_project()
        print("Project added")

    if choice == 8:
        print("Sort Employee ")
        emp.sort_employee()
        print("Table Sorted")

    if choice == 9:
        print("Search Employee")
        emp.search_employee()
        print("Searched employee")
        
    if choice == 10:
        print(emp.display_all())

    if choice == 11:
        print(project.display_all())
