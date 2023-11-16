# Display welcome message
print("Welcome to the tip calculator.")

# Input: Get the total bill amount from the user
bill = float(input("What was the total bill? $"))

# Input: Get the desired tip percentage from the user
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Input: Get the number of people to split the bill
people = input("How many people to split the bill? ")

# Calculate the tip amount based on the total bill and tip percentage
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent

# Calculate the total bill including the tip
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay
bill_per_person = total_bill / int(people)

# Round the amount to two decimal places
final_amount = round(bill_per_person, 2)

# Display the result
print(f"Each person should pay: ${final_amount}")
