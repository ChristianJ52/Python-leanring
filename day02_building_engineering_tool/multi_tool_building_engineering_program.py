# ---------------------------
# Building Engineering Tool
# ---------------------------

# Function #1: Energy cost calculator
def energy_cost():
   # Ask user for inputs and convert them to float (decimal) numbers
    energy_used = float(input("Enter energy used in kWh: "))
    cost_per_kwh = float(input("Enter cost per kWh in euros: "))
    
    # Calculate total cost
    total_cost = energy_used * cost_per_kwh
    
    # Print result with 2 decimal places
    print(f"Total energy cost: €{total_cost:.2f}")

# Function #2: Heating load estimation
def heating_load():
    # Ask for building area in m²
    area = float(input("Enter floor area in m²: "))
    
    # Ask for average U-value in W/m²·K
    u_value = float(input("Enter average U-value (W/m²·K): "))
    
    # Ask for temperature difference between inside and outside
    temp_diff = float(input("Enter temperature difference (inside - outside, °C): "))
    
    # Formula: Heat load = Area × U-value × Temperature difference
    load_watts = area * u_value * temp_diff
    
    #convert Watts to Kw and print result
    print(f"Estimated heating load: {load_watts / 1000:.2f} kW")

def co2_emissions():
    # Constant for CO2 emissions per kWh
    Emission_factor_electricity = 0.233 #kg co2 per kWh
    # Ask for energy usage
    energy_used = float(input("Enter energy used in kWh: "))
    
    # Calculate emissions
    emissions = energy_used * Emission_factor_electricity
    
    # Print result
    print(f"Estimated co2 emissions: {emissions:.2f}kg co2")

# ---------------------------
# Main program loop
# ---------------------------

while True:
    #Display the menu
    print("\nBuilding Engineering tool")
    print("1. Energy Cost Calculator")
    print("2. Heating Load Estimator")
    print("3. CO₂ Emissions Calculator")
    print("4. Exit")
    
    # Ask the user for a choice
    choice = input("Choose an option (1-4): ")

      # Run the matching function based on user choice
    if choice == "1":
        energy_cost()
    elif choice == "2":
        heating_load()
    elif choice == "3":
        co2_emissions()
    elif choice == "4":
        print("Goodbye!")
        break  # Exit the loop and end the program
    else:
        # If the user enters something that's not 1-4
        print("Invalid choice, please try again.")