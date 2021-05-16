import os 
import sys 

def get_months(starting_annual_salary,praportion_salary_saved,cost_of_home,semi_annual_salary,month_return = 0):
    rate_intreset = 0.04 
    down_payment = 0.25 * cost_of_home
    current_savings = 0 
    month_salary = starting_annual_salary/12
    saved_portion = month_salary*praportion_salary_saved
    n = 0 
    while (down_payment - current_savings) >=  0:
        if n%6 == 0 and n!= 0 :
            month_salary += month_salary* semi_annual_salary
            saved_portion = month_salary*praportion_salary_saved
        current_savings += current_savings*rate_intreset/12 + saved_portion
        n += 1
    return n

if __name__=="__main__":
    starting_annual_salary = float(input("Please Enter Annual salary(Float):"))
    praportion_salary_saved = float(input("Please Enter % of salary you want to save(Float):"))
    cost_of_home = float(input("Please Enter the price of home:"))
    semi_annual_salary = float(input("Please enter mid year raise(float):"))
    print(get_months(starting_annual_salary,praportion_salary_saved,cost_of_home,semi_annual_salary))
