import mysql.connector as mysql
import employees as emp
import proj


def printData(obj):
    
    obj.cursor.execute(f"Select * from {obj.table_name};")
    data = obj.cursor.fetchall

    for i in obj.colums:
        print(i)

        
conn = mysql.connect(
    host = "localhost" ,
    user = "root" ,
    password = "Pp7004554599" ,
    database = "EMS"
    )

cursor = conn.cursor()


