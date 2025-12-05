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

employee = emp.customer()
project = proj.project()


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
    
