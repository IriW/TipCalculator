#This is the tip calculator. To be used and overused
print("Welcome to Irina's tip calculator")
ToPay=float(input("What is the total bill?\n€"))
peopleCount=(int(input("How many people are splitting the bill?\n")))
tipPercentage=(float(input("How large of a tip would you like to leave? 10? 12? 15? or 20? ...Or just give your number: \n"))/100)
payPerPerson=ToPay/peopleCount
totalBill=ToPay+ToPay*tipPercentage
totalBillPerPerson=payPerPerson + payPerPerson * tipPercentage
TotalPerPerson="{:.2f}".format(totalBillPerPerson)
TotalToPay="{:.2f}".format(totalBill)
print(f"Total to pay with a tip is {totalBill}")
print(f"Each person should pay: {TotalPerPerson}€")