# work hours of employee

work_hours = [('hari', 6),('haran',89),('lonesoul', 9)]

def employee_of_the_month(work_hours):

    current_max = 0
    employee_name=''

    for employee,hour in work_hours:
        if hour > current_max:
            current_max = hour
            employee_name = employee
        else:
            pass
    return(employee_name,current_max)

name,hours = (employee_of_the_month(work_hours))
print(name,hours)