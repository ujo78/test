from file_handling import (
    createTable_file_update,
    addProject_file_update,
    deleteProject_file_update,
    updateProject_file_update,
    sortProject_file_update,
    searchProject_file_update,
    displayAll_file_update,
    clearTable_file_update
)
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

    @createTable_file_update
    def create_table(self):
        self.cursor.execute(
            f"create table {self.table_name}("
            f"{self.column[2]} int primary key,"
            f"{self.column[0]} varchar(255),"
            f"{self.column[1]} int,"
            f"{self.column[3]} int,"
            f"{self.column[4]} varchar(255),"
            f"{self.column[5]} int)"
        )

    @addProject_file_update
    def add_project(self):
        self.cursor.execute(
            f"insert into {self.table_name} values("
            f"{self.id},'{self.name}',{self.duration},{self.budget},'{self.status}',{self.emp_id})"
        )

    @deleteProject_file_update
    def delete_project(self):
        self.cursor.execute(
            f"delete from {self.table_name} where {self.column[2]} = {self.id}"
        )

    @updateProject_file_update
    def update_project(self):
        self.cursor.execute(
            f"update {self.table_name} set "
            f"{self.column[0]} = '{self.name}', "
            f"{self.column[1]} = {self.duration}, "
            f"{self.column[3]} = {self.budget}, "
            f"{self.column[4]} = '{self.status}' "
            f"where {self.column[2]} = {self.id}"
        )

    @sortProject_file_update
    def sort_project(self, sortbywhat, ascordsc=True):
        order = "ASC" if ascordsc else "DESC"
        self.cursor.execute(
            f"select * from {self.table_name} order by {sortbywhat} {order}"
        )
        return self.cursor.fetchall()

    @searchProject_file_update
    def search_project(self, searchbywhat, searchinput):
        self.cursor.execute(
            f"select * from {self.table_name} where {searchbywhat} like '{searchinput}%'"
        )
        return self.cursor.fetchall()

    @displayAll_file_update
    def display_all(self):
        self.cursor.execute(
            f"select * from {self.table_name}"
        )
        return self.cursor.fetchall()

    @clearTable_file_update
    def clear_table(self):
        self.cursor.execute(
            f"delete from {self.table_name}"
        )