class BankAccount:
    ROI = 0.05  

    def __init__(self, name):
        self.name = name
        self.amount = 0.0

    def deposit(self, amount):
        self.amount += amount
        print(f"Deposited ${amount} into {self.name}'s account.")
        
    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            print(f"Withdrew ${amount} from {self.name}'s account.")
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        interest = self.amount * BankAccount.ROI
        return interest

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Balance: ${self.amount:.2f}")
        print(f"Interest Rate: {BankAccount.ROI * 100:.2f}%")
        print(f"Calculated Interest: ${self.calculate_interest():.2f}")
        print("-" * 30)

account1 = BankAccount("Alice")
account1.deposit(1000)
account1.withdraw(200)
account1.display()

account2 = BankAccount("Bob")
account2.deposit(1500)
account2.withdraw(300)
account2.display()
