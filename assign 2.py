class Bank:
    def __init__(self, bankname, bankcode):
        self.bankname = bankname
        self.bankcode = bankcode


class Branch:
    def __init__(self, branchname, branchcode, bank):
        self.branchname = branchname
        self.branchcode = branchcode
        self.bank = bank


class Employee:
    def __init__(self, employeename, employeenumber, branch):
        self.employeename = employeename
        self.employeenumber = employeenumber
        self.branch = branch


class BankAccount:
    def __init__(self, accountno, accountname, totalbalance, branch):
        self.accountno = accountno
        self.accountname = accountname
        self.totalbalance = totalbalance
        self.branch = branch

        def deposit(self, depositAmount):
            self.totalBalance += depositAmount
            print("Deposited amount:", depositAmount)

        def withdraw(self, withdrawAmount):
            if self.totalBalance > withdrawAmount:
                self.totalBalance -= withdrawAmount
                print("Withdraw amount:", withdrawAmount)
            else:
                print("Insufficient balance")

        def checkBalance(self):
            print("Your account balance is:", self.totalBalance)

        def calcInterest(self, interestRate):
            self.totalBalance += self.totalBalance * interestRate / 100
            print("Updated balance after interest calculation:", self.totalBalance)


class CurrentAccount:
    def __init__(self, AccountNo, TotalBalance, BankAccount):
        self.AccountNo = AccountNo
        self.TotalBalance = TotalBalance
        self.overdraftlimit = 0
        self.BankAccount = BankAccount

    def MakeDeposit(self, DepositAmount):
        self.TotalBalance += DepositAmount

    def MakeWithdrawal(self, WithdrawAmount):
        if self.TotalBalance - WithdrawAmount >= -self.overdraftlimit:
            self.TotalBalance -= WithdrawAmount
        else:
            print("Insufficient funds available")

    def CheckBalance(self):
        return self.TotalBalance

    def GetOverdraftLimit(self):
        return self.overdraftlimit

    def SetOverdraftLimit(self, overdraftlimit):
        self.overdraftlimit = overdraftlimit


class SavingsAccount:
    def __init__(self, AccountNo, TotalBalance, BankAccount):
        self.AccountNo = AccountNo
        self.TotalBalance = TotalBalance
        self.interestRate = 0.04
        self.BankAccount = BankAccount

    def Deposit(self, amount):
        self.TotalBalance += amount

    def Withdraw(self, amount):
        self.TotalBalance -= amount

    def CheckBalance(self):
        print("Your Current Balance is %d" % (self.TotalBalance))

    def CalculateInterest(self):
        print("Your Interest is %d" % (self.TotalBalance * self.interestRate))

