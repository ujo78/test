class employee():
    def __init__(self, cursor):
        self.cursor = cursor
        self.table_name = 'employees'
        self.colums = ['empid', 'empname', 'empsalary', 'empage']

        self.id = None
        self.name = None
        self.salary = None
        self.age = None
    
    def createTable(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name}({self.colums[0]} INT , {self.colums[1]} VARCHAR(255) , {self.colums[2]} INT , {self.colums[3]} INT );")

    def add_employee(self):
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES ({self.id}  , '{self.name}' , {self.salary} , {self.age});")

    def del_employee(self):
        self.cursor.execute(f"DELETE FROM {self.table_name} WHERE {self.colums[0]} = {self.id};")

    def update_employee(self):
        self.cursor.execute(
            f"UPDATE {self.table_name} SET "
            f"{self.colums[1]} = '{self.name}', "
            f"{self.colums[2]} = {self.salary}, "
            f"{self.colums[3]} = {self.age} "
            f"WHERE {self.colums[0]} = {self.id};"
        )


       
    
    def search_employee(self , searchbywhat , filterbywhat , searchinput , start , end):
     
        self.cursor.execute(f"select * from table_name where {searchbywhat} like {searchinput}% and  {filterbywhat} between {start} and {end}")

        return self.cursor.fetchall()


    def sort(self , sortbywhat , ascordsc = True):
        if ascordsc == True:
            self.cursor.execute(f"Select * from {self.table_name} order by {sortbywhat} ")
        else: 
            ascordsc = "DESC"
            self.cursor.execute(f"Select * from {self.table_name} order by {sortbywhat} {ascordsc} ")
        return self.cursor.fetchall()
    

    def clear_table(self):
        self.cursor.execute(f"DELETE FROM {self.table_name};")
        return self.cursor.fetchall()
    

    

    
    

    










    

    
    



