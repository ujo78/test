def createTable_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("Created table")
        return func(self, *args , **kwargs)
    return wrapper

def add_employee_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("log.txt" , "w") as file:
            file.write("added customer")
        return func(self, *args , **kwargs)
    return wrapper

def del_employee_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("deleted customer")
        return func(self, *args, **kwargs)
    return wrapper

def  update_employee_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("updated customer")
        return func(self, *args , **kwargs)
    return wrapper

def  search_employee_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("searched customer")
        return func(self, *args , **kwargs)
    return wrapper

def  sort_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("sorted customer")
        return func(self, *args , **kwargs)
    return wrapper

def  clear_table_file_update(func):
    def wrapper(self,*args,**kwargs):
        with open("log.txt" , "w") as file:
            file.write("cleared table")
        return func(self, *args , **kwargs)
    return wrapper