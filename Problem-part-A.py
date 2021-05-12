import os 
import sys 
print("LOl")

def get_months(starting_annual_salary,praportion_salary_saved,cost_of_home,month_return = 0):
    rate_intreset = 0.04 
    down_payment = 0.25 * cost_of_home
    current_savings = 0 
    month_salary = starting_annual_salary/12
    saved_portion = month_salary*praportion_salary_saved
    n = 0 
    while (down_payment - current_savings) >=  0:
        current_savings += current_savings*rate_intreset/12 + saved_portion
        n += 1
    return n

if __name__=="__main__":
    starting_annual_salary = float(input("Please Enter Annual salary(Float):"))
    praportion_salary_saved = float(input("Please Enter % of salary you want to save(Floar):"))
    cost_of_home = float(input("Please Enter the price of home:"))
    print(get_months(starting_annual_salary,praportion_salary_saved,cost_of_home))
