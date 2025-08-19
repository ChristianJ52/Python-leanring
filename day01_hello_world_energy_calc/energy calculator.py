#Energy Cost Calculator

#Ask the user for an input
energy_used = float(input("enter energy used in kwh: "))
cost_per_kwh = float(input("eneter cost per kwh in euros: "))

#Calculate total cost 
total_cost = energy_used * cost_per_kwh

#Display the result
print(f"Total energy cost: €{total_cost:.2f}")