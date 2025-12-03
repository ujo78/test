class customer():
    def __init__(self,cursor):
        self.cursor = cursor
        self.table_name = 'employees'
        self.colums = ['empid' , 'empname' , 'empsalary' , 'empage']
    
    def createTable(self ):
        self.cursor.execute(f"create table{self.table_name}({self.colums[0]} int , {self.colums[1]} varchar(255) , {self.colums[2]} int , {self.colums[3]} int );")


    def add_employee(self):
        self.cursor.execute (f"Insert ({self.id}  , '{self.name}' , {self.salary} , {self.age});")

    def del_employee(self):
        self.cursor.execute (f"Delete from customers where cutomer_id = {self.id}")

def update_employee(self):

    if self.name is not null:

    


    


