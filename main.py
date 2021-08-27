#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")
ToPay=float(input("What was the total bill?\n€")) #500
peopleCount=(int(input("Between how many people should the bill be split?\n"))) #5
tipPercentage=(float(input("How many percent would you like to tip?\n"))/100)  #12%
payPerPerson=ToPay/peopleCount
totalBill=ToPay+ToPay*tipPercentage
totalBillPerPerson=payPerPerson + payPerPerson * tipPercentage
TotalPerPerson="{:.2f}".format(totalBillPerPerson)
TotalToPay="{:.2f}".format(totalBill)
print(f"Total to pay with a tip is {totalBill}")
print(f"The Total amount with the tip to pay by each person is {TotalPerPerson}€")