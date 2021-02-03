class Atm:
    def __init__(self):
        user_input=int(input(""""hhow would you like too proceed
        1.check balance 
        2. cash deposit 
        3.cash withdrawl
        4.change pin 
        5.exit"""))
        self.__pin=0
        self.__balance=0

         if user_input==1:
             self.check_balance()
         if user_input==2:
             self.deposit()
         if user_input==3:
            self.withdraw()
         if user_input==4:
             self.change_pin()
         if user_input==5:
             print("exit")
    def check_set_pin(self):
        if str(self.__pin)==4:
            pass


    def check_balance(self):
        pin=int(input("enter pin"))
        # if pin==
        pass


