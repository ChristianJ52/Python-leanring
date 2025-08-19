# ---------------------------
# Building Portfolio Manager - Day 4 Practice
# Learning to work with multiple buildings at once
# ---------------------------

# My building portfolio with some example buildings plus the hospital I added
buildings_portfolio = [
    {
        "name": "Office Tower A",
        "area": 1200,
        "u_value": 0.25,
        "city": "Dublin",
        "heating_system": "heat_pump",
        "monthly_energy_kwh": 3200
    },
    {
        "name": "Warehouse B", 
        "area": 2500,
        "u_value": 0.45,
        "city": "Cork",
        "heating_system": "gas_boiler",
        "monthly_energy_kwh": 8100
    },
    {
        "name": "Shopping Center C",
        "area": 3200,
        "u_value": 0.30,
        "city": "Dublin", 
        "heating_system": "heat_pump",
        "monthly_energy_kwh": 12500
    },
    {
        "name": "School D",
        "area": 800,
        "u_value": 0.35,
        "city": "Galway",
        "heating_system": "gas_boiler", 
        "monthly_energy_kwh": 2800
    },
    {
        "name": "St. Vincent's Hospital",
        "area": 50000,
        "u_value": 0.5,
        "city": "Dublin",
        "heating_system": "gas_boiler",
        "monthly_energy_kwh": 50000
    }
]

print("=== My Building Portfolio Analysis ===\n")

# ---------------------------
# Task 1: Added St. Vincent's Hospital to my portfolio
# ---------------------------
print("Task 1: Added St. Vincent's Hospital")
print(f"Now managing {len(buildings_portfolio)} buildings total\n")

# ---------------------------
# Task 2: Find all my Dublin buildings
# ---------------------------
print("Task 2: Finding all buildings in Dublin")
print("-" * 40)

dublin_buildings = []  # Empty list to collect my Dublin buildings

# Check each building to see if it's in Dublin
for building in buildings_portfolio:
    if building["city"] == "Dublin":  # If building is in Dublin
        dublin_buildings.append(building)  # Add it to my Dublin list

print(f"I have {len(dublin_buildings)} buildings in Dublin:")
for building in dublin_buildings:
    print(f"  - {building['name']}")

print()

# ---------------------------
# Task 3: Calculate average U-value across my portfolio
# ---------------------------
print("Task 3: Calculate average U-value for my buildings")
print("-" * 40)

# Going to add up all U-values and divide by number of buildings
total_u_value = 0
building_count = 0

for building in buildings_portfolio:
    total_u_value += building["u_value"]
    building_count += 1

average_u_value = total_u_value / building_count
print(f"Average U-value across my portfolio: {average_u_value:.3f} W/m²·K")

# Let me try a different way using Python shortcuts
u_values = [building["u_value"] for building in buildings_portfolio]
average_u_value_v2 = sum(u_values) / len(u_values)
print(f"Double-checking with method 2: {average_u_value_v2:.3f} W/m²·K")

print()

# ---------------------------
# Task 4: See which city I have the most buildings in
# ---------------------------
print("Task 4: Which city has most of my buildings?")
print("-" * 40)

# I need to count how many buildings I have in each city
city_counts = {}  # This will store city names and counts

for building in buildings_portfolio:
    city = building["city"]
    if city in city_counts:
        city_counts[city] += 1  # Add one more to this city's count
    else:
        city_counts[city] = 1   # First building I have in this city

print("My buildings by city:")
for city, count in city_counts.items():
    print(f"  {city}: {count} buildings")

# Find which city has the most
most_buildings_city = max(city_counts, key=city_counts.get)
most_buildings_count = city_counts[most_buildings_city]

print(f"\nMy largest presence is in: {most_buildings_city} ({most_buildings_count} buildings)")

print()

# ---------------------------
# Task 5: Calculate my total monthly energy costs
# ---------------------------
print("Task 5: What are my total monthly energy costs?")
print("-" * 40)

cost_per_kwh = 0.25  # Assuming €0.25 per kWh
total_energy = 0
total_cost = 0

print("Cost breakdown for each building:")
for building in buildings_portfolio:
    energy = building["monthly_energy_kwh"]
    cost = energy * cost_per_kwh
    total_energy += energy
    total_cost += cost
    
    print(f"  {building['name']}: {energy:,} kWh = €{cost:,.2f}")

print(f"\nMy portfolio monthly totals:")
print(f"  Total energy consumption: {total_energy:,} kWh")
print(f"  Total monthly cost: €{total_cost:,.2f}")

print()

# ---------------------------
# Extra practice: Find my buildings with gas boilers
# ---------------------------
print("Extra: Which of my buildings use gas boilers?")
print("-" * 40)

gas_boiler_buildings = []
for building in buildings_portfolio:
    if building["heating_system"] == "gas_boiler":
        gas_boiler_buildings.append(building)

print(f"I have {len(gas_boiler_buildings)} buildings with gas boilers:")
for building in gas_boiler_buildings:
    print(f"  - {building['name']} in {building['city']}")

print()

# ---------------------------
# More practice: Buildings that need insulation upgrades
# ---------------------------
print("Extra: Buildings that might need insulation upgrades (U-value > 0.4)")
print("-" * 40)

poor_insulation_count = 0
for building in buildings_portfolio:
    if building["u_value"] > 0.4:
        poor_insulation_count += 1
        print(f"  - {building['name']}: {building['u_value']} W/m²·K")

print(f"\nBuildings I should consider upgrading: {poor_insulation_count}")

print("\n" + "="*60)
print("Day 4 of learning completed I will now spend time going back through the code I wrote and breaking it down to fully understand what is happening with each line of code ")
print("Today I learned:")
print("   How to work with lists and dictionaries")  
print("   Looping through building data")
print("   Filtering and counting buildings")
print("   Calculating totals and averages")
print("   Finding buildings that meet certain criteria")
