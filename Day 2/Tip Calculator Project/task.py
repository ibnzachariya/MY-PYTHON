# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))


# print("welcome to the tip calculator!")
# bill =float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
# people = int(input("How many people to split the bill? "))
# bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)
# bill_per_person = round(bill_with_tip / people)
# print(f"Each person should pay: ${bill_per_person}")

barrels = int(input("Total barrels produced?"))
price_per_barrel = int(input("Total price per barrel?"))
Total_revenue: int = barrels * price_per_barrel
price_revenue_in_Naira: int = Total_revenue * 1300
print(f"Total Revenue: USD: ${Total_revenue}")
print(f"Total Revenue: Naira: N{price_revenue_in_Naira}")
