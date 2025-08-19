# Day 3 — Multi-Tool Upgrade

On Day 3, I upgraded my original Building Engineering Tool by adding new features to make it more practical and professional.  
This version can log results, generate charts, handle errors, and convert units.

---

## What it does

### 1. Energy Cost Calculator
- Inputs: energy used (kWh) and cost per kWh (€).  
- Outputs total cost and equivalent energy in megajoules (MJ).  
- Logs results to a report file and to `energy_log.csv` for charting.  

### 2. Heating Load Estimator
- Inputs: floor area (m²), U-value (W/m²·K), and temperature difference (°C).  
- Outputs heating load in kW and converts ΔT to °F.  
- Logs results to the report file.  

### 3. CO₂ Emissions Calculator
- Inputs: energy used (kWh).  
- Uses a fixed emission factor (0.233 kg CO₂ per kWh).  
- Outputs estimated emissions and logs to the report file.  

### 4. Report Viewer
- Reads and displays the `report.txt` history of all calculations.  

### 5. Energy Usage Chart
- Reads `energy_log.csv`.  
- Uses Matplotlib to plot kWh usage over time.  

---

## What I learned
- How to use **CSV files** for data logging.  
- How to generate simple **line charts** with Matplotlib.  
- Writing reusable input functions for **error handling**.  
- Creating and appending to a **timestamped report file**.  
- Adding **unit conversions** (kWh → MJ, kW → BTU/hr, °C → °F).  
