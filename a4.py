def calculate_gross_salary(basic_salary):
    da = 0.70 * basic_salary  # Dearness Allowance (70% of BS)
    ta = 0.30 * basic_salary  # Travel Allowance (30% of BS)
    hra = 0.10 * basic_salary  # House Rent Allowance (10% of BS)
    gross_salary = basic_salary + da + ta + hra
    
    print(f"Basic Salary (BS): {basic_salary:.2f}")
    print(f"Dearness Allowance (DA) [70% of BS]: {da:.2f}")
    print(f"Travel Allowance (TA) [30% of BS]: {ta:.2f}")
    print(f"House Rent Allowance (HRA) [10% of BS]: {hra:.2f}")
    print(f"Gross Salary (BS + DA + TA + HRA): {gross_salary:.2f}")
    
    return gross_salary

# Prompt user for basic salary
basic_salary = float(input("Enter the Basic Salary (BS): "))
calculate_gross_salary(basic_salary)
