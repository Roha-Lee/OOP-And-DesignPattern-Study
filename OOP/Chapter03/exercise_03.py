# type hinting 적용하기 
class BankAccount:
    """은행 계좌 클래스"""
    interest: float = 0.02
    
    def __init__(self, owner_name: str, balance: float) -> None:
        """Constructor"""
        self.owner_name: str = owner_name
        self.balance: float = balance
    
    def deposit(self, amount: float) -> None:
        """deposit amount of money to current balance"""
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        """withdraw amount of money to current balance"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount
    
    def add_interest(self):
        """apply interest to current balance"""
        self.balance *= 1 + BankAccount.interest
        
help(BankAccount) # docstring이 요약되어 나온다. 

# type hinting을 지키지 않아도 실행에 에러가 뜨지는 않지만 IDE에서 에러를 띄워준다. 