import sys

def calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years):
    total_savings = current_wealth
    for year in range(1, years + 1):
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        print(f"Year {year}: Total wealth = {total_savings:.2f}")
    return 0

def calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth):
    total_savings = current_wealth
    years_to_freedom = 0
    while True:
        years_to_freedom += 1
        interest = total_savings * (rate_of_return / 100)
        total_savings += interest + (monthly_savings * 12)
        if total_savings > target_wealth:
            print(f"You will reach financial freedom in {years_to_freedom} years! Keep grinding!! ")
            return 0

def main():
    prog = input("Which program would you like to run? Type 'returns' or 'freedom' ")
    try:
        current_wealth = float(input("Enter your current wealth: "))
        rate_of_return = float(input("Enter estimated rate of return (%): "))
        monthly_savings = float(input("Enter how much you can save per month: "))
    except ValueError:
        print("Invalid input. You must only enter numbers, dumbass!! ")
        sys.exit()
    if prog == 'returns':
        years = int(input("Enter investment period in years: "))
        calculate_wealth_by_year(current_wealth, rate_of_return, monthly_savings, years)
    elif prog == 'freedom':
        try:
            target_wealth = float(input("How much money do you need to be financially free? "))
        except ValueError:
            print("Invalid input. You must only enter numbers, dumbass!! ")
            sys.exit()
        calculate_years_till_freedom(current_wealth, rate_of_return, monthly_savings, target_wealth)
    else:
        print("Invalid input. Type 'returns' or 'freedom'")

main()
