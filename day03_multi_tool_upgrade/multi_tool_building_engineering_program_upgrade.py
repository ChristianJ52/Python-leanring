# ---------------------------
# Building Engineering Tool
# ---------------------------

#imports for chart 
import os, csv, datetime
import matplotlib.pyplot as plt



#Report generator
import datetime
import os

def save_report(text):
    """Append a timestamped line to report.txt"""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("report.txt","a", encoding="utf-8")as f:
        f.write(f"[{ts}]) {text}\n")

def view_report():
    """Print the report (or say if it doesn't exist yet)"""
    if not os.path.exists("report.txt"):
        print("No report yet. Run a calculation first.")
        return
    print("\n--- Report History ---")
    with open("report.txt", "r", encoding="utf-8") as f:
        print(f.read())
    print("--- End ---\n")        

#Error Proofing

def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
         print("X Please enter a valid number like 12.5")

def ask_menu(prompt, options=("1","2","3","4")):
    while True:
        choice = input(prompt).strip()   # trims spaces/newlines
        if choice in options:
            return choice
        print(f"Invalid choice. Pick one of: {', '.join(options)}")
      
#conversion of units
def kwh_to_mj(kwh):      return kwh * 3.6
def kw_to_btuhr(kw):     return kw * 3412.142
def c_to_f(c):           return (c * 9/5) + 32      

# Function #1: Energy cost calculator
def energy_cost():
   
   
   # Ask user for inputs and convert them to float (decimal) numbers
    energy_used = ask_float("Enter energy used in kWh: ")
    cost_per_kwh = ask_float("Enter cost per kWh in euros: ")
    
    # Calculate total cost
    total_cost = energy_used * cost_per_kwh
    
 #Do conversions here (kWh → MJ)
    energy_mj = kwh_to_mj(energy_used)





    # Print result with 2 decimal places
    print(f"Energy used: {energy_used:.2f} kWh ({energy_mj:.2f} MJ)")
    print(f"Total energy cost: €{total_cost:.2f}")
    save_report(f"Energy Cost — {energy_used:.2f} kWh ({kwh_to_mj(energy_used):.2f} MJ), €{total_cost:.2f}")
    
    ENERGY_LOG = "energy_log.csv"
    def log_energy_usage(kwh):
        """Append a timestamp + kWh to energy_log.csv (creates file with header if missing)."""
    new_file = not os.path.exists(ENERGY_LOG)
    with open(ENERGY_LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["timestamp", "kwh"])
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        w.writerow([ts, kwh])
   
    # log kWh so we can chart history
    log_energy_usage(energy_used)
    print("Logged energy usage for charting.")



# Function #2: Heating load estimation
def heating_load():
    # Ask for building area in m²
    area = ask_float("Enter floor area in m²: ")
    
    # Ask for average U-value in W/m²·K
    u_value = ask_float("Enter average U-value (W/m²·K): ")
    
    # Ask for temperature difference between inside and outside
    temp_diff = ask_float("Enter temperature difference (inside - outside, °C): ")
    
    # Formula: Heat load = Area × U-value × Temperature difference
    load_watts = area * u_value * temp_diff
    
    #convert Watts to Kw and print result
    print(f"ΔT: {temp_diff:.2f} °C ({c_to_f(temp_diff):.2f} °F)")
    print(f"Estimated heating load: {load_watts / 1000:.2f} kW")
    save_report(f"Heating Load — Area {area:.2f} m², ΔT {temp_diff:.2f} °C, {load_watts:.2f} kW")


def co2_emissions():
    # Constant for CO2 emissions per kWh
    Emission_factor_electricity = 0.233 #kg co2 per kWh
    # Ask for energy usage
    energy_used = ask_float("Enter energy used in kWh: ")
    
    # Calculate emissions
    emissions = energy_used * Emission_factor_electricity
    
    # Print result
    print(f"Energy: {energy_used:.2f} kWh ({kwh_to_mj(energy_used):.2f} MJ)")
    print(f"Estimated co2 emissions: {emissions:.2f}kg co2")
    save_report(f"CO₂ — {energy_used:.2f} kWh ({kwh_to_mj(energy_used):.2f} MJ), {emissions:.2f} kg")


# ---------------------------
# Main program loop
# ---------------------------

while True:
    #Display the menu
    print("\nBuilding Engineering tool")
    print("1. Energy Cost Calculator")
    print("2. Heating Load Estimator")
    print("3. CO₂ Emissions Calculator")
    print("4. View report")
    print("5. Exit")

    
    # Ask the user for a choice
    choice = input("Choose an option (1-5): ")

      # Run the matching function based on user choice
    if choice == "1":
        energy_cost()
    elif choice == "2":
        heating_load()
    elif choice == "3":
        co2_emissions()
    elif choice == "4":
        view_report()
    
    elif choice == "5":
        print("Goodbye!")
        break  # Exit the loop and end the program
    else:
        # If the user enters something that's not 1-4
        print("Invalid choice, please try again.")