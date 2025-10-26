class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = {i+1: balance[i] for i in range(len(balance))}
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        acc1_balance = self.accounts.get(account1)
        acc2_balance = self.accounts.get(account2)

        if acc1_balance is None or acc2_balance is None: 
            return False
        if acc1_balance < money: 
            return False
        else:
            self.accounts[account1] -= money
            self.accounts[account2] += money
            return True

    def deposit(self, account: int, money: int) -> bool:
        if self.accounts.get(account) is None:
            return False
        else:
            self.accounts[account] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        balance = self.accounts.get(account)
        if balance is None:
            return False
        elif balance < money:
            return False
        else:
            self.accounts[account] -= money
            return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)