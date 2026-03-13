class Student:
    def __init__(self,):
        pass


class Teacher:
    def __init__(self):
        pass
    

class ClassRoom(Student,Teacher):
    def __init__(self,name):
        super().__init__()
        self.name = name
        
        
        
class_five = ClassRoom("mahesh")

print(class_five.name)