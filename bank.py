balance=0
def deposit():
    global balance
    amount=int(input("emter the amt to deposit"))
    balance=balance+amount
    balcheck()
def withdraw():
    global balance
    amount=int(input("emter amout"))
    balance=balance-amount
    balcheck()

def balcheck():
    print('available balance',balance)

def menu():
    ch=0
    while(ch!=4):
      print("1.deposit","2.withdraw","3.balance")
      ch=int(input("enter ur choice"))
      if ch==1:
        deposit()
      elif ch==2:
        withdraw()
      elif ch==3:
        balcheck()
def welcome():
    print('welcome ATM')
    pin=int(input('enter ur pin no'))
    if pin==123:
        menu()
    else:
        print('invalid pin')
        welcome()

    welcome()










































welcome()