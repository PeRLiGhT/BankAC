class BankAccount:
    def __init__(self, account_number: int, balance: float, name: str, account_type: str):
        self.__account_number = account_number
        self.__balance = balance 
        self.__name = name 
        self.__account_type = account_type 

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"{self.__name} ฝากเงิน {amount} บาทสำเร็จ")
        else:
            print("จำนวนเงินฝากต้องมากกว่า 0")

    def withdraw(self, amount: float):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"{self.__name} ถอนเงิน {amount} บาทสำเร็จ")
            else:
                print("ยอดเงินในบัญชีไม่เพียงพอ")
        else:
            print("จำนวนเงินที่ถอนต้องมากกว่า 0")

    def get_balance(self):
        return self.__balance

    def transfer(self, target_account, amount: float):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            target_account.__balance += amount
            print(f"{self.__name} โอนเงิน {amount} บาทไปยัง {target_account.__name} สำเร็จ")
        else:
            print("ยอดเงินไม่พอสำหรับโอน")

    def calculate_interest(self):
        interest_rates = {
            'saving': 0.02,
            'checking': 0.01
        }
        rate = interest_rates.get(self.__account_type, 0)
        interest = self.__balance * rate
        self.__balance += interest
        print(f"ดอกเบี้ยที่ได้รับ: {interest:.2f} บาท (ประเภทบัญชี: {self.__account_type})")


# ตัวอย่างการใช้งาน
account1 = BankAccount(123456, 5000.0, "สมชาย", "saving")
account2 = BankAccount(654321, 3000.0, "วิชัย", "checking")

account1.deposit(2000)  
account1.withdraw(1000)
account1.calculate_interest()
account1.transfer(account2, 1500)

print(f"ยอดเงินคงเหลือของ {account1._BankAccount__name}: {account1.get_balance()} บาท")
print(f"ยอดเงินคงเหลือของ {account2._BankAccount__name}: {account2.get_balance()} บาท")