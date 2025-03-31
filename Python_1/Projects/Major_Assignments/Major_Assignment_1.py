def basic_salary(hourly_rate,hours_worked_per_week):
    regular_hours=min(hours_worked_per_week,40)
    salary_month=(regular_hours * hourly_rate)
    return salary_month*4

def overtime_salary(hourly_rate,hours_worked_per_week):
    if hours_worked_per_week>40:
        overtime_rate=hourly_rate*1.5
        overtime=(hours_worked_per_week-40)*overtime_rate
        return overtime*4
    else:
        return 0
    
def total_salary(hourly_rate,hours_worked_per_week):
    return overtime_salary(hourly_rate,hours_worked_per_week) + basic_salary(hourly_rate,hours_worked_per_week)
             
def tax_amount():
    if bassal<60000:
        tax=bassal*0.1
    elif (bassal>60000) and (bassal<85000):
        tax=(60000-bassal)*0.1 + (bassal-60000)*0.15  
    elif bassal>85000:
        tax=(60000-bassal)*0.1 + (85000-bassal)*0.15 + (bassal-85000)*0.2
    return tax

def gross_salary():
    allowances=bassal*0.2
    return bassal+allowances-tax_amount()

def salary_bracket():
    if grosal<50000:
        print('Your salary bracket is Low Income')
    elif (grosal>50000) and (grosal<80000):
        print('Your salary bracket is Middle Income')
    elif grosal>80000:
        print('Your salary bracket is High Income') 


def employee_report():
    print('Basic salary is ',bassal)
    print('Overtime salary is ',overtime_salary(hourly_rate,hours_worked_per_week))
    print('Total salary is ',total_salary(hourly_rate,hours_worked_per_week))
    print('Tax amount is deducted from your account is ',tax_amount())
    print('The gross salary is ',grosal)
    salary_bracket()
    
for i in range (0,3):
    employee=input("Enter your name ")
    hours_worked_per_week=int(input("Enter the hours worked per week "))
    hourly_rate=int(input("Enter the hourly rate "))
    bassal=basic_salary(hourly_rate,hours_worked_per_week)
    grosal=gross_salary()
    employee_report()
    print()
    
