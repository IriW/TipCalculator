#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
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