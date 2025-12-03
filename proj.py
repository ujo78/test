class project ():
    def __init__(self,cursor):
        self.cursor=cursor
    def __init__(self,table_name): 
         self.table_name= 'project'
         self.column = ['proj_name','proj_duration', 'proj_id', 'proj_budget','proj_status','emp_id' ]
         
    def create_table(self):
        self.cursor.execute(f"create table{self.table_name}({self.column[1]} varcar(255),{self.column[2]}varcar(255),{self.column[0]}int ,{self.column[3]}int),{self.column[4]} varcar(255);")
    def add_project(self):
        self.cursor.execute(f"insert({self.name},{self.duration},{self.id},{self.budget},{self.status})")
    
    def delete_project(self):
        pass