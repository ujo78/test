def createTable_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Table Created\n")
        return func(self, *args, **kwargs)
    return wrapper


def addProject_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Project Added\n")
        return func(self, *args, **kwargs)
    return wrapper


def deleteProject_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Project Deleted\n")
        return func(self, *args, **kwargs)
    return wrapper


def updateProject_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Project Updated\n")
        return func(self, *args, **kwargs)
    return wrapper


def sortProject_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Project Sorted\n")
        return func(self, *args, **kwargs)
    return wrapper


def searchProject_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Project Searched\n")
        return func(self, *args, **kwargs)
    return wrapper


def displayAll_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Displayed All Projects\n")
        return func(self, *args, **kwargs)
    return wrapper


def clearTable_file_update(func):
    def wrapper(self, *args, **kwargs):
        with open("prolog.txt", "a") as file:
            file.write("Table Cleared\n")
        return func(self, *args, **kwargs)
    return wrapper
