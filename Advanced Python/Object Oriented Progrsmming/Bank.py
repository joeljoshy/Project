# create account
# deposit - print balance
# withdraw - balance (check balance before withdrawing)


class Bank:
    bank_name = 'Swiss Bank'
    balance = 0
    def New_Account(self, name, age, gender):

        self.name = name
        self.age = age
        self.gender = gender


    def deposite(self,d_amount):

        self.d_amount = d_amount
        Bank.balance+=d_amount
        print("\nYour ", Bank.bank_name, " account has been credited with ₹", self.d_amount, "\n")


    def withdraw(self, w_amount):

        self.w_amount = w_amount
        if self.w_amount > Bank.balance:
            print("Low Balance!!  \n\t₹", self.balance)
        else:
            print("Amount Debited --> ₹", self.w_amount)
            print("Balance-->  ₹", Bank.balance-w_amount)


    def details(self):

        print("Account Details --> ", self.name, self.age, self.gender, Bank.bank_name)

ac = Bank()
ac.New_Account('Joel', 23, 'M')
ac.details()
ac.deposite(20000)
ac.withdraw(1000)