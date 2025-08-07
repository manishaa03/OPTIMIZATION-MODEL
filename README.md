# OPTIMIZATION-MODEL

COMPANY: CODTECH IT SOLUTIONS

NAME: MANISHA KUMARI

INTERN ID: CT12DN310

DOMAIN: DATA SCIENCE

DURATION: 12 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

# OPTIMIZATION MODEL - PRODUCT MIX  
CodTech Internship Task 4 – Linear Programming with PuLP  

## Project Overview  
This project solves a real-world business optimization problem using Linear Programming and PuLP in Python.  
The goal is to **maximize profit** by determining the optimal number of products to produce under given constraints.

## Problem Description  
A company produces two products:
- **Product A**: Profit ₹20/unit, requires 3 machine hours and 2 labor hours  
- **Product B**: Profit ₹30/unit, requires 4 machine hours and 3 labor hours  

Available Resources:
- Machine Hours: 60  
- Labor Hours: 40  

**Objective**: Maximize total profit while staying within resource limits.

## Technologies Used  
- Python  
- PuLP (Linear Programming library)

## How to Run  
1. Install PuLP (if not already installed):  
```bash
pip install pulp
```

2. Run the optimization script:  
```bash
python optimization_model.py
```

3. Output will show:  
- Optimal quantity of Product A and B  
- Maximum achievable profit  
- Solution status (Optimal / Infeasible)

## Sample Output  
```
Status: Optimal  
Optimal Units of Product A: 0.0  
Optimal Units of Product B: 13.33  
Maximum Profit: ₹400  
```

