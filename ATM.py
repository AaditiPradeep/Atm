class ATM(object):
    def __init__(self , cardNo, pinNo ):
        self.cardNo = cardNo
        self.pinNo = pinNo
    def BalanceEnquiry(self):
        print("enquiring")
    def CashWithdrawal(self):
        print("withdrawing cash")

customer1 = ATM(input("Enter your card No : "), input("Ener your pinNo : "))
print("Your cardNo is" , customer1.cardNo)
print("Your pinNo is" , customer1.pinNo)
customer1.BalanceEnquiry()
customer1.CashWithdrawal()
