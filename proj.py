class project ():
    def __init__(self,cursor):
        self.cursor=cursor 
        self.table_name= 'project'
        self.column = ['proj_name','proj_duration', 'proj_id', 'proj_budget','proj_status','emp_id' ]
         
    def create_table(self):
        self.cursor.execute(f"create table{self.table_name}({self.column[1]} varcar(255),{self.column[2]}varcar(255),{self.column[0]}int ,{self.column[3]}int),{self.column[4]} varcar(255);")
    def add_project(self):
        self.cursor.execute(f"insert({self.name},{self.duration},{self.id},{self.budget},{self.status})")
    
    def delete_project(self):
        self.cursor.execute(f"delete from project where project_id={self.id}")
        
    def update_project(self):
        self.cursor.execute(f"update{self.table_name} set"
                            f"{self.column[1]} = '{self.name}'",
                            f"{self.column[2]} = '{self.duration}'",
                            f"{self.column[3]} = '{self.budget}'"
                            f"{self.column[4]} = '{self.status}'"
                            f"where{self.column[0]} = '{self.id}'"
                            )
        
   