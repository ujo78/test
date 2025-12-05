class project():
    def __init__(self, cursor):
        self.cursor = cursor
        self.table_name = 'project'
        self.column = ['proj_name', 'proj_duration', 'proj_id', 'proj_budget', 'proj_status', 'emp_id']
        self.name = None
        self.duration = None
        self.id = None
        self.budget = None
        self.status = None
        self.emp_id = None
         
    def create_table(self):
        self.cursor.execute(
            f"create table {self.table_name}("
            f"{self.column[2]} int primary key,"
            f"{self.column[0]} varchar(255),"
            f"{self.column[1]} int,"
            f"{self.column[3]} int,"
            f"{self.column[4]} varchar(255),"
            f"{self.column[5]} int);"
        )

    def add_project(self):
        self.cursor.execute(
            f"insert into {self.table_name} values("
            f"{self.id},'{self.name}',{self.duration},{self.budget},'{self.status}',{self.emp_id})"
        )
    
    def delete_project(self):
        self.cursor.execute(
            f"delete from {self.table_name} where {self.column[2]} = {self.id}"
        )
        
    def update_project(self):
        self.cursor.execute(
            f"update {self.table_name} set "
            f"{self.column[0]} = '{self.name}', "
            f"{self.column[1]} = {self.duration}, "
            f"{self.column[3]} = {self.budget}, "
            f"{self.column[4]} = '{self.status}' "
            f"where {self.column[2]} = {self.id}"
        )
    
    def sort_project(self):
        self.cursor.execute(f"select * from {self.table_name} order by {self.column[0]}")
        self.cursor.execute(f"select * from {self.table_name} order by {self.column[1]}")
        self.cursor.execute(f"select * from {self.table_name} order by {self.column[2]}")
        self.cursor.execute(f"select * from {self.table_name} order by {self.column[3]}")
        self.cursor.execute(f"select * from {self.table_name} order by {self.column[4]}")
        return self.cursor.fetchall() 
    
    def search_project(self):
        if self.id is not None:
            self.cursor.execute(
                f"select * from {self.table_name} where {self.column[2]} = {self.id}"
            )
        elif self.name is not None:
            self.cursor.execute(
                f"select * from {self.table_name} where {self.column[0]} = '{self.name}'"
            )
        elif self.duration is not None:
            self.cursor.execute(
                f"select * from {self.table_name} where {self.column[1]} = {self.duration}"
            )
        elif self.budget is not None:
            self.cursor.execute(
                f"select * from {self.table_name} where {self.column[3]} = {self.budget}"
            )
        elif self.status is not None:
            self.cursor.execute(
                f"select * from {self.table_name} where {self.column[4]} = '{self.status}'"
            )
        else:
            self.cursor.execute(
                f"select * from {self.table_name}"
            )
        return self.cursor.fetchall() 

    def display_all(self):
        self.cursor.execute(f"select * from {self.table_name};")
        return self.cursor.fetchall()
    
    def clear_table(self):
        self.cursor.execute(f"delete from {self.table_name};")
