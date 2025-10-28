#a split rent programme

rent = float(input("Current rent: "))
food = int(input("Number of foods ordered: "))
electricity = float(input("Electricity unit: "))
unit_charge = int(input("Charge per unit: "))
roommate = int(input("How many in flat/room: "))

electricity_bill = float(electricity * unit_charge)
total_bill = float(food + rent + electricity_bill)
split_bill = float(food + rent + electricity_bill) // roommate

print(f"Electricity bill: {electricity_bill}")
print(f"Total bill: {total_bill}")
print(f"Split bill per person: {split_bill}")
