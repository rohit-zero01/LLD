class Bank:
    def __init__(self, name, balance):
        self.name = name
        #Private attribute - "__"
        self.__balance = balance

    #GETTER
    def get_balance(self):                              #this is a getter, it is used to only display the
        print(f"Available balance: {self.__balance}")    # priate attribute in public, no one can modify it

    # SETTER
    def set_balance(self, new_amount):
        print(f"Available balance: {new_amount}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"Amount deposited, Account balance: {self.__balance}\n")

    def withdrawal(self, amount):
        if amount>self.__balance:
            print("Not enough balance")
        else:
            self.__balance -=amount
            print(f"Amount withdrawn, Account balance: {self.__balance}\n")

acc = Bank("Rohit", 5000)
acc.deposit(2000)
acc.balance = 2000000.  #anyone can access the balance attribute from public and modify it, that's why we make it private.
acc.get_balance()
acc.set_balance(100000)
acc.withdrawal(3000)
