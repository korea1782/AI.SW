by. korea1782
```python
class Account(object): #(object)는 안써도 자동으로 object class를 받아온다.
    num_acc=0
#     balance = 0
#     rate = 0.0
#     number = 'OOO-OOO-OOOOO'
    # def __init__(self): Default 생성자
    def __init__(self, num='OOO-OOO-OOOOO', amnt=0, rate=1.0):
        self.number = num
        self.balance = amnt
        self.rate = rate
        Account.num_acc += 1

    # 계좌의 기능(Method)
    def deposit(self, money): #입금
        self.balance += money
    def withdraw(self, money): #인출
        self.balance -= money
    def obtain_interest(self): #이자 획득
        self.balance += self.balance*(self.rate/100)
    def transfer(self, another, amnt):
        self.balance -= amnt
        another.balance += amnt
    def get_balance(self):
        return self.balance
    def set_balance(self, amnt):
        self.balance = amnt
    #operator overloading: 연산자(+,-,*,/)를 클래스에 맞게 재정의하여 사용하는 것
    def __add__(self, another): #두 계좌 통합 기능
        new_acc=Account(amnt=self.balance+another.balance,
        rate=self.rate)
        return new_acc

class MinBalanceAccount(Account): #Account 클래스를 상속받음
    def __init__(self, min_balance=0, num='OOOO-OOO-OOOOO', amnt=0, rate=1.0, b_rate=1.0):
        Account.__init__(self, num=num, amnt=amnt, rate=rate)
#Account.__init__(~)은 다음과 같은 효과
#self.number = num
#self.balance = amnt
#self.rate = rate
#Account.num_acc += 1
#def init을 하지않으면 자동으로 부모 클래스의 init을 상속받는다. 
#하지만 init을 써주어서 Account 클래스의 init을 상속받기 위해 Account.__init__을 해줘야만 한다.

        self.minimum_balance = min_balance 
        self.bonus_rate = b_rate
    def withdraw(self, amnt): # 인출 기능 수정
        if self.balance - amnt < self.minimum_balance:
            print('Sorry, minimum balance must be maintained')
        else:
            Account.withdraw(self, amnt)
    def obtain_interest(self): #보너스 이율 반영
        self.balance += (self.balance)*((self.rate+self.bonus_rate)/100.0)
    def transfer(self, another, amnt):
        if self.balance - amnt < self.minimum_balance:
            print('Sorry, minimum balance must be maintained')
        else:
            Account.transfer(self, another, amnt)

# acc1 = MinBalanceAccount()
# acc2 = MinBalanceAccount()
# acc1.balance = 500
# acc2.balance = 1000

# acc3 = acc1+acc2 #acc3 = MinBalanceAccount.__add__(acc1, acc2) 
# #acc1,acc2가 minbalance이기 때문에 부모에 있는 add 대신 MinbalanceAccount.__add__를 씀
# print(acc3.balance)
acc1= MinBalanceAccount(min_balance=-100)
acc1.set_balance(500)
acc2= MinBalanceAccount(min_balance=0)
acc2.set_balance(1000)
acc1.transfer(acc2, 600)  
print(acc1.get_balance()) #-100
print(acc2.get_balance()) #1600
```
