# Day 4 — Energy Usage Predictor

On Day 4, I extended my Building Engineering Tool with features that log energy usage and generate charts.  
This turns the tool into an early version of an **energy usage predictor**, since past usage can now be tracked and visualized.

---

## What it does

### 1. Energy Cost Calculator
- Inputs: energy used (kWh) and cost per kWh (€).  
- Outputs total cost and equivalent energy in megajoules (MJ).  
- Saves results to a text report and logs kWh to `energy_log.csv`.  

### 2. Heating Load Estimator
- Inputs: floor area (m²), U-value (W/m²·K), and temperature difference (°C).  
- Outputs heating load in kW and converts ΔT to °F.  
- Logs results to the report file.  

### 3. CO₂ Emissions Calculator
- Inputs: energy used (kWh).  
- Uses a fixed emission factor (0.233 kg CO₂ per kWh).  
- Outputs estimated emissions and logs results.  

### 4. Report Viewer
- Displays the contents of `report.txt`, which contains a timestamped history of calculations.  

### 5. Energy Usage Chart
- Reads `energy_log.csv` and plots energy usage (kWh) over time with Matplotlib.  
- Helps identify usage patterns and trends.  

---

## What I learned
- How to persist data with **CSV files** and reuse it later.  
- How to generate **line charts** to visualize building energy usage.  
- How to append and timestamp results in a report file.  
- Writing **reusable input functions** for better error handling.  
- Building a menu-driven program with multiple data sources.  
