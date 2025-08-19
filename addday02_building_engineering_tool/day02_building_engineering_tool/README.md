# Day 2 — Building Engineering Tool

On Day 2, I built a simple **multi-tool program** for basic building engineering calculations.  
The script runs in a loop and lets the user choose between different tools.

---

## What it does

### 1. Energy Cost Calculator
- Asks the user for energy usage (kWh) and cost per kWh (€).  
- Calculates and displays the total energy cost.  

### 2. Heating Load Estimator
- Inputs: floor area (m²), average U-value (W/m²·K), and temperature difference (°C).  
- Formula used:  
  Q = Area × U-value × Temperature Difference  
- Converts the result from Watts to kW and displays the heating load.  

### 3. CO₂ Emissions Calculator
- Uses a constant emissions factor for electricity (0.233 kg CO₂ per kWh).  
- Multiplies by energy usage to estimate emissions in kg CO₂.  

---

## What I learned
- How to create and organize multiple functions in a program.  
- Building a **menu-driven tool** with a `while True` loop.  
- Taking and converting user inputs with `input()` and `float()`.  
- Formatting results for readability with f-strings.  
- Using constants in calculations.  
