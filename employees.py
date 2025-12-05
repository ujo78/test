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

    def sort_employee(self):
        
        self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY {self.colums[0]};")
        self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY {self.colums[1]};")
        self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY {self.colums[2]};")
        self.cursor.execute(f"SELECT * FROM {self.table_name} ORDER BY {self.colums[3]};")
        return self.cursor.fetchall()

    def search_employee(self):
        
        if self.id is not None:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE {self.colums[0]} = {self.id};")
        if self.name is not None:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE {self.colums[1]} = '{self.name}';")
        if self.salary is not None:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE {self.colums[2]} = {self.salary};")
        if self.age is not None:
            self.cursor.execute(f"SELECT * FROM {self.table_name} WHERE {self.colums[3]} = {self.age};")
        return self.cursor.fetchall()
    
    def display_all(self):
        self.cursor.execute(f"SELECT * FROM {self.table_name};")
        return self.cursor.fetchall()
    

    def clear_table(self):
        self.cursor.execute(f"DELETE FROM {self.table_name};")
        return self.cursor.fetchall()

