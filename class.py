# class BankAccount():
#     def __init__(self, balance = 1000):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def widthdraw(self, amount):
#         if self.balance > amount:
#             self.balance -= amount

#         else: return 'Insufficient balance'



# class Student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def add_marks(self, marks):
#         self.marks += marks

#     def get_average(self, subjects):
#         return self.marks/subjects


class Car():
    def __init__(self, fuel):
        self.fuel = fuel

    def add_fuel(self,amount):
        self.fuel += amount 

    def drive(self, distance):
        if self.fuel>=distance:
            self.fuel -=distance

        else: return 'low on fuel'

    def get_fuel(self):
        return self.fuel      
    

class Mobile():
    def __init__(self, battery):
        self.battery = battery

