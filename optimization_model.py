# Install PuLP if not installed
# pip install pulp

import pulp as pl

# Create LP problem (Maximize Profit)
model = pl.LpProblem("Product_Mix_Optimization", pl.LpMaximize)

# Decision Variables (Number of products A and B)
A = pl.LpVariable('A', lowBound=0, cat='Continuous')
B = pl.LpVariable('B', lowBound=0, cat='Continuous')

# Objective Function: Maximize Profit
# Profit: A = $20, B = $30
model += 20 * A + 30 * B, "Total Profit"

# Constraints
# Machine Hours: A takes 3 hrs, B takes 4 hrs, total available = 60 hrs
model += 3 * A + 4 * B <= 60, "Machine_Hours"

# Labor Hours: A takes 2 hrs, B takes 3 hrs, total available = 40 hrs
model += 2 * A + 3 * B <= 40, "Labor_Hours"

# Solve the problem
model.solve()

# Output Results
print("Status:", pl.LpStatus[model.status])
print(f"Optimal Units of Product A: {A.varValue}")
print(f"Optimal Units of Product B: {B.varValue}")
print(f"Maximum Profit: ${pl.value(model.objective)}")
