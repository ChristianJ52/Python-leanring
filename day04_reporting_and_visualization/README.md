# Day 4 — Multi-Tool with Reporting and Visualization

On Day 4, I upgraded my Building Engineering Tool by adding data logging and visualization features.  
This version not only calculates energy, heating load, and CO₂ emissions, but also stores the results in files and generates charts.

---

## What it does

### 1. Energy Cost Calculator
- Inputs: energy used (kWh) and cost per kWh (€).  
- Outputs total cost and equivalent energy in megajoules (MJ).  
- Logs results to a timestamped text report and appends kWh to `energy_log.csv`.  

### 2. Heating Load Estimator
- Inputs: floor area (m²), U-value (W/m²·K), and temperature difference (°C).  
- Outputs heating load in kW and converts ΔT to °F.  
- Saves results in the report file.  

### 3. CO₂ Emissions Calculator
- Inputs: energy used (kWh).  
- Uses a fixed emission factor (0.233 kg CO₂ per kWh).  
- Outputs estimated emissions and logs results.  

### 4. Report Viewer
- Reads and displays `report.txt`, which stores a timestamped history of all calculations.  

### 5. Energy Usage Chart
- Reads data from `energy_log.csv`.  
- Uses Matplotlib to plot energy usage (kWh) over time.  

---

## What I learned
- How to use **CSV logging** to store historical data.  
- Generating **charts with Matplotlib** to visualize results.  
- Managing multiple output files (`report.txt` and `energy_log.csv`).  
- Improving input handling with reusable helper functions.  
- Combining calculations with data storage and visualization in one tool.  
   ```bash
   python multi_tool_reporting.py
