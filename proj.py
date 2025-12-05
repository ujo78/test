class project ():
    def __init__(self,cursor):
        self.cursor=cursor
        self.table_name= 'project'
        self.column = ['proj_name','proj_duration', 'proj_id', 'proj_budget','proj_status','emp_id' ]
        self.name = None
        self.duration = None
        self.id = None
        self.budget = None
        self.status = None
        self.emp_id = None
         
    def create_table(self):
        self.cursor.execute(f"create table {self.table_name}({self.column[2]} int primary key,{self.column[0]} varchar(255),{self.column[1]} int,{self.column[3]} int,{self.column[4]} varchar(255),{self.column[5]} int);")
    def add_project(self):
        self.cursor.execute(f"insert into {self.table_name} values({self.id},'{self.name}',{self.duration},{self.budget},'{self.status}',{self.emp_id})")
    
    def delete_project(self):
        self.cursor.execute(f"delete from {self.table_name} where {self.column[2]}={self.id}")
        
    def update_project(self):
        self.cursor.execute(f"update {self.table_name} set {self.column[0]} = '{self.name}', {self.column[1]} = {self.duration}, {self.column[3]} = {self.budget}, {self.column[4]} = '{self.status}' where {self.column[2]} = {self.id}")
        
