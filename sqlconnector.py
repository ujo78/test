import mysql.connector as mysql
from employees import *
import proj


def printData(obj):
    
    obj.cursor.execute(f"Select * from {obj.table_name};")
    return obj.cursor.fetchall()

        
conn = mysql.connect(
    host = "localhost" ,
    user = "root" ,
    password = "@may2004" ,
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
    print("8 : Search Employee")
    print("9 : Sort Employee")
    print("10 : Clear Employee Table")
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
        print("Enter the details: ")
        emp.id = int(input("Enter new id: "))
        emp.name = input("Enter new name")
        emp.salary = int(input("Enter new salary"))
        emp.age = int(input("Enter new age"))

        emp.update_employee()
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
        print("Enter input for condition to search by id, name, salary")
        searchbywhat = input("Enter by what you want to search")
        searchinput = input("Enter to search")
        filterbywhat = input("By what you want to filter")
        start = input("Give the starting value")
        end = input("Give the ending value")
        if(filterbywhat == 'age'):
            if(start >= 40 and end <= 50):
                print("Budha Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))
            
            if(start >= 30 and end <= 39):    
                print("Medium Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))

            if(start >= 20 and end <= 29):    
                print("Young Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))

        if(filterbywhat == 'salary'):
            if(start >= 40,000 and end <= 50,000):
                print("Budha Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))
            
            if(start >= 30,000 and end <= 39,000):    
                print("Medium Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))

            if(start >= 20,000 and end <= 29,000):    
                print("Young Employees are: ")
                print(emp.search_employee(searchbywhat , searchinput , filterbywhat,start,end))
        

    if choice == 9:
        sortbywhat =input("Enter the condition to sort for: ")
        print("Sorted employees are")
        print(emp.sort(sortbywhat))
        
    if choice == 10:
        print(emp.clear_table())

    if choice == 11:
        print("Table is : ")
        print(printData(emp))

   
