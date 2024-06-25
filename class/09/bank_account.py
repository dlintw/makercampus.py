class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"存款 {amount} 成功。當前餘額：{self.balance}")
        else:
            print("存款金額必須大於零。")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"取款 {amount} 成功。當前餘額：{self.balance}")
        else:
            print("取款金額無效或餘額不足。")

    def display_account_info(self):
        print(f"帳戶號碼：{self.account_number}")
        print(f"帳戶持有人：{self.account_holder}")
        print(f"餘額：{self.balance}")

# 創建帳戶
account = BankAccount("123456789", "Alice", 1000)

# 存款
account.deposit(500)

# 取款
account.withdraw(200)

# 顯示帳戶資訊
account.display_account_info()
