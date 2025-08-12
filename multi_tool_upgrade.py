# ---------------------------
# Building Engineering Tool
# ---------------------------

# Imports for chart and file handling
import os, csv, datetime
import matplotlib.pyplot as plt

# ---------------------------
# Report generator
# ---------------------------
def save_report(text):
    """Append a timestamped line to report.txt"""
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("report.txt", "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {text}\n")

def view_report():
    """Print the report (or say if it doesn't exist yet)"""
    if not os.path.exists("report.txt"):
        print("No report yet. Run a calculation first.")
        return
    print("\n--- Report History ---")
    with open("report.txt", "r", encoding="utf-8") as f:
        print(f.read())
    print("--- End ---\n")

# ---------------------------
# number check
# ---------------------------
def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("X Please enter a valid number like 12.5")

def ask_menu(prompt, options=("1","2","3","4")):
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"Invalid choice. Pick one of: {', '.join(options)}")

# ---------------------------
# Unit conversions
# ---------------------------
def kwh_to_mj(kwh): return kwh * 3.6
def kw_to_btuhr(kw): return kw * 3412.142
def c_to_f(c): return (c * 9/5) + 32

# ---------------------------
# CSV Logging for charting
# ---------------------------
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

def plot_energy_history():
    """Read energy_log.csv and plot kWh over time."""
    if not os.path.exists(ENERGY_LOG):
        print("No energy log yet. Run the Energy Cost Calculator first.")
        return

    timestamps, kwh_values = [], []
    with open(ENERGY_LOG, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            timestamps.append(row["timestamp"])
            try:
                kwh_values.append(float(row["kwh"]))
            except ValueError:
                pass

    if not kwh_values:
        print("Log exists but has no valid data yet.")
        return

    plt.figure()
    plt.plot(timestamps, kwh_values, marker="o")
    plt.title("Energy Usage History")
    plt.xlabel("Timestamp")
    plt.ylabel("kWh")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

# ---------------------------
# Function #1: Energy cost calculator
# ---------------------------
def energy_cost():
    energy_used = ask_float("Enter energy used in kWh: ")
    cost_per_kwh = ask_float("Enter cost per kWh in euros: ")

    total_cost = energy_used * cost_per_kwh
    energy_mj = kwh_to_mj(energy_used)

    print(f"Energy used: {energy_used:.2f} kWh ({energy_mj:.2f} MJ)")
    print(f"Total energy cost: €{total_cost:.2f}")

    save_report(f"Energy Cost — {energy_used:.2f} kWh ({energy_mj:.2f} MJ), €{total_cost:.2f}")
    log_energy_usage(energy_used)

    print("Logged energy usage for charting.")

# ---------------------------
# Function #2: Heating load estimation
# ---------------------------
def heating_load():
    area = ask_float("Enter floor area in m²: ")
    u_value = ask_float("Enter average U-value (W/m²·K): ")
    temp_diff = ask_float("Enter temperature difference (inside - outside, °C): ")

    load_watts = area * u_value * temp_diff

    print(f"ΔT: {temp_diff:.2f} °C ({c_to_f(temp_diff):.2f} °F)")
    print(f"Estimated heating load: {load_watts / 1000:.2f} kW")
    save_report(f"Heating Load — Area {area:.2f} m², ΔT {temp_diff:.2f} °C, {load_watts:.2f} kW")

# ---------------------------
# Function #3: CO₂ emissions calculator
# ---------------------------
def co2_emissions():
    Emission_factor_electricity = 0.233
    energy_used = ask_float("Enter energy used in kWh: ")

    emissions = energy_used * Emission_factor_electricity

    print(f"Energy: {energy_used:.2f} kWh ({kwh_to_mj(energy_used):.2f} MJ)")
    print(f"Estimated CO₂ emissions: {emissions:.2f} kg")
    save_report(f"CO₂ — {energy_used:.2f} kWh ({kwh_to_mj(energy_used):.2f} MJ), {emissions:.2f} kg")

# ---------------------------
# Main program loop
# ---------------------------
while True:
    print("\nBuilding Engineering Tool")
    print("1. Energy Cost Calculator")
    print("2. Heating Load Estimator")
    print("3. CO₂ Emissions Calculator")
    print("4. View report")
    print("5. Plot energy history")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        energy_cost()
    elif choice == "2":
        heating_load()
    elif choice == "3":
        co2_emissions()
    elif choice == "4":
        view_report()
    elif choice == "5":
        plot_energy_history()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
