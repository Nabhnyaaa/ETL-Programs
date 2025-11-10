#5



import csv
import numpy as nm
import pandas as pd

d=pd.read_csv("departments")
e=pd.read_csv("employees")




'''Find the average salary of all employees.'''
r=e["Salary"].mean()
print(r)

print("--------")

'''Count the number of employees in each department using the lookup file.'''
n=pd.merge(d,e,how='inner',on='Department_ID')
count=n.groupby("Department_Name")["Employee_ID"].count().reset_index(name='no_of_emp')
print(count)

print("--------")


'''Find the highest salary in each department.'''
n=pd.merge(d,e,how='inner',on='Department_ID')
m=n.groupby("Department_Name")["Salary"].max().reset_index(name='max_sal_in_dept')
print(m)


print("--------")

'''List all employees older than 50 years.'''
old=e[(e["Age"]>50)]
print(old)

print("--------")


'''Find the total salary expenditure department-wise.'''
n=pd.merge(d,e,how='inner',on='Department_ID')
total=n.groupby("Department_Name")["Salary"].sum().reset_index(name='Total_Salary_Expenditure')
print(total)

print("--------")


'''Find the department with the maximum number of employees.'''
n=pd.merge(d,e,how='inner',on='Department_ID')
total=n.groupby("Department_Name")["Employee_ID"].count().reset_index(name='no_of_emp').sort_values(by='no_of_emp',ascending=False)
print(total.head(1))

print("--------")


'''List all employees whose name starts with the letter 'A'.'''
employees_start_with_a = e[e['Name'].str.startswith('A')]
print(employees_start_with_a)

print("--------")


'''Create a new CSV file merging department name from the lookup file into the employee data.'''
n=pd.merge(d,e,how='inner',on='Department_ID')
n.to_csv("res1.csv")

print("--------")


'''Find the youngest employee in the company'''
r=e.sort_values(by='Age',ascending=True).head(1)
print(r)

print("--------")


'''Find the total number of employees'''
r=e["Employee_ID"].count()
print(r)

print("--------")


''' Find the top 5 highest paid employees'''
r=e.sort_values(by='Salary',ascending=False).head(5)
print(r)

print("--------")


'''List employees between ages 30 and 40'''
r=e[(e["Age"]>30) & (e["Age"]<40)]
print(r)

print("--------")


'''Find the average age of employees department-wise'''
n=pd.merge(d,e,how='inner',on='Department_ID')
av=n.groupby("Department_Name")["Age"].mean().reset_index(name='Avg_Age')
print(av)

print("--------")


'''List departments with fewer than 5 employees'''
n=pd.merge(d,e,how='inner',on='Department_ID')
ag=n.groupby("Department_Name")["Employee_ID"].count().reset_index(name='Emp_count')
print(ag[(ag["Emp_count"]<5)])

print("--------")


'''Count how many employees have salary above ₹100,000'''
high_salary_employees = e[e['Salary'] > 100000]
high_salary_count = len(high_salary_employees)
print(high_salary_count)


print("--------")


'''Create a list of unique department names'''
unique_departments = d['Department_Name'].unique().tolist()
print(unique_departments)


print("--------")


'''Save filtered employees aged over 45 to a new CSV file'''
emp=e[(e["Age"]>45)]
emp.to_csv("Employees Aged Over 45.csv")