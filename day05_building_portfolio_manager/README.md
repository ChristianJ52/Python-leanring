# Day 5 — Building Portfolio Manager

This script analyzes a small portfolio of buildings. It filters by city, computes averages, counts buildings per city, estimates monthly energy costs, and flags buildings that may need insulation upgrades.

---

## What it does
- Stores a portfolio as a list of dictionaries (name, area, U-value, city, heating system, monthly kWh).
- Filters buildings in Dublin.
- Calculates the average U-value (two methods for verification).
- Counts buildings per city and finds the largest presence.
- Computes per-building and total monthly energy cost (assumes €0.25/kWh).
- Lists buildings with gas boilers.
- Flags buildings with U-value > 0.4 for potential insulation upgrades.

---

## Sample outputs for the current dataset
- Dublin buildings: Office Tower A, Shopping Center C, St. Vincent’s Hospital (3 total)
- Average U-value: 0.370 W/m²·K
- City with the most buildings: Dublin (3)
- Portfolio monthly energy: 76,600 kWh
- Portfolio monthly cost (@ €0.25/kWh): €19,150.00
- Gas boiler buildings: Warehouse B, School D, St. Vincent’s Hospital (3)
- Insulation upgrade candidates (U > 0.4): Warehouse B (0.45), St. Vincent’s Hospital (0.50)

---

## What I learned
- Working with lists of dictionaries to model real data.
- Looping, filtering, and counting with dictionaries.
- Calculating totals and averages and formatting output.
- Structuring console output into clear task sections.

Screenshot #1 — Average U-value
<img width="726" height="332" alt="image" src="https://github.com/user-attachments/assets/1b087214-1d94-48aa-a1bc-7ee6396026ae" />
I calculated the portfolio’s average U-value in two ways. First, a manual loop with running totals (clear and beginner-friendly). Then, a list comprehension with sum(). Using both methods was a way to double-check results and practice different coding styles.

Screenshot #2 — City counts & largest presence
<img width="851" height="500" alt="image" src="https://github.com/user-attachments/assets/e8a032f0-4c13-426a-b7e2-a03270ef9d5d" />
Here I used a dictionary as a counter to count how many buildings are in each city. Then, I applied Python’s built-in max() with key=... to find the city with the most buildings. This was a big step in learning how to aggregate data and extract insights from a dataset.
