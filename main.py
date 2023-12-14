#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

#Questions 
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 15, 18, or 20? "))
people = int(input("How many people are splitting the bill? "))

#Bill Calculations
bill_with_tip = bill * (1 + tip / 100)
cost_per_person = bill_with_tip / people
final_amount = round(cost_per_person, 2)
final_amount = "{:.2f}".format(cost_per_person)
print(f"Each person should pay: ${final_amount}")