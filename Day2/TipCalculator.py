#number = 5

#print("Alexander"[number])
#print(f"Alexander{number}")

#print ("this is a number" + str(number))

#print (str(70) + str(100))

#print (2 ** 5)

#print(8 // 3)
#print(round(8 / 3))


#score = 0
#height = 1.8
#isWinning = True

#f-string

#print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

payout = int(total_bill) / int(split) * (1 + (0.01 * int(percentage)))

final_amount = "{:.2f}".format(payout)

print(f"Each person should pay: ${final_amount}")