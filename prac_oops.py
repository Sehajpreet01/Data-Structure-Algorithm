class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def display(self):
        return f'Student name is {self.name} and marks are {self.marks}'
    
    def is_pass(self):
        if self.marks>=40:
            return True 
        else: return False

    def grade(self):
        if self.marks>=80:
            return ('A')

        elif self.marks>=60:
            return ('B')

        elif self.marks>=40:
            return ('C')

        else: return ('Failed')


s1 = Student('Sehaj', 89)
# print(s1.display())
# print(s1.name)
# print(s1.marks)
print(s1.is_pass())
print(s1.grade())
            