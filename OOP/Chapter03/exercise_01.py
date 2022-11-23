# 무슨 일을 하는지 전혀 알수 없음.
class SomeClass:
    variable1 = 0.02
    
    def __init__(self, variable2, variable3):
        self.variable2 = variable2
        self.variable3 = variable3
    
    def func1(self, variable4):
        self.variable3 += variable4
        
    def withdraw(self, variable4):
        if self.variable3 < variable4:
            print("Insufficient balance!")
        else:
            self.variable3 -= variable4
    
    def add_variable1(self):
        self.variable3 *= 1 + SomeClass.variable1
        

# 변수, 클래스 이름을 잘 짓는 것도 추상화의 일종이다. 
class BankAccount:
    interest = 0.02
    
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount
    
    def add_interest(self):
        self.balance *= 1 + BankAccount.interest
        
