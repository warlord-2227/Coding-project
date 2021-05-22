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

def get_total_saving(proportion,rate_of_interest,semi_annual_salary,monthly_salary):
    saved_salary = monthly_salary*proportion
    current_saving = 0
    for i in range(1,37):
        if i%6 == 0 :
            monthly_salary += monthly_salary*semi_annual_salary
            saved_salary = monthly_salary*proportion/100 
        current_saving += current_saving * rate_of_interest/12 + saved_salary
        # print(current_saving)
    return current_saving


def get_right_amount(starting_annual_salary,rate_of_interest):
    semi_annual_salary = 0.07
    # rate_of_interest = 0.04 
    cost_of_home = 1000000
    current_saving = 0 
    down_payment = 0.25 * cost_of_home  
    a = 0
    b = 10000 
    n = 0 
    monthly_salary = starting_annual_salary/12
    if (down_payment - get_total_saving(100,rate_of_interest,semi_annual_salary,monthly_salary)) > 0 :
        return 0,0
    
    flag = False
    while flag == False:
        praportion = (a+b)/2
        current_saving = get_total_saving(praportion/100,rate_of_interest,semi_annual_salary,monthly_salary)
        print(current_saving,down_payment,monthly_salary)
        if (down_payment - current_saving < 100):
            flag = True
        else:
            a = praportion
        n += 1
    return praportion/100,n
if __name__=="__main__":
    starting_annual_salary = float(input("Please Enter Annual salary(Float):"))
    # praportion_salary_saved = float(input("Please Enter % of salary you want to save(Float):"))
    # cost_of_home = float(input("Please Enter the price of home:"))
    # semi_annual_salary = float(input("Please enter mid year raise(float):"))
    rate_of_interest = float(input("Please Enter best rate of interest:"))
    # print(get_months(starting_annual_salary,praportion_salary_saved,cost_of_home,semi_annual_salary))
    print(get_right_amount(starting_annual_salary,rate_of_interest))