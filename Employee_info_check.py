import csv
import pymysql
open("Selected_Employees.txt", "w").close()
Final_file = open("Selected_Employees.txt", "a+")
connection=pymysql.connect(host='localhost',user='root',passwd='12345',db='sakila')
cursor=connection.cursor()

file=open("employee_data_100",'r')
re=csv.reader(file)

st1="INSERT INTO employee_data_info(ID,Name,Age,Gender,Country,City,Email,Phone,Department,Position,Experience_Years,Salary,Bonus,Joining_Year,Performance_Rating,Work_From_Home,Projects_Handled,Leaves_Taken,Certifications,Overtime_Hours) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i in re:
    cursor.execute(st1, (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[16],i[17],i[18],i[19]))
    connection.commit()




'''Q) Find the employee(s) who have the highest combined total of salary and bonus and list their name, department, and country.'''
st2="SELECT Salary,Bonus,Name,Department,Country from employee_data_info"
cursor.execute(st2)
data=cursor.fetchall()
data2=[]
total_data={}
for i in data:
    if i!=(None, None, None, None, None):
        data2.append(i)
for i in data2:
    total=float(i[0])+float(i[1])
    if total not in total_data.keys():
        total_data[total]=[]
    person_data=[i[2],i[3],i[4]]
    total_data[total].append(person_data)
max=max(total_data.keys())
Final_file.write("Employee(s) who have the highest combined total of salary and bonus:\n")
Final_file.write(f"The employee(s) who have the highest combined total of {max} is: {total_data[max]}\n\n")
# print(f"The employee(s) who have the highest combined total of {max} is: {total_data[max]}")




'''Q) List the employees whose email domain is "example.com", have “Manager” as a position, and joined before 2010.'''
st3="SELECT Email,Position,Joining_year,Name from employee_data_info"
cursor.execute(st3)
data=cursor.fetchall()
data2=[]

Final_file.write("Employees whose email domain is 'example.com', have “Manager” as a position, and joined before 2010:\n")
for i in data:
    if i[0]!=None:
        data2.append(i)
for i in data2:
    if i[0].strip().split('@')[1]=="example.com" and i[1]=="Manager" and int(i[2])<2010:
        # print(f"{i[3]}: {i[0]}, {i[1]}, {i[2]}")
        Final_file.write(f"{i[3]}: {i[0]}, {i[1]}, {i[2]}\n\n")



'''Q) Determine the percentage of employees who joined after 2015 and have handled more than 10 projects.'''
st4="SELECT Joining_year,Projects_Handled from employee_data_info"
cursor.execute(st4)
data=cursor.fetchall()
data2=[]
for i in data:
    if i[0]!=None:
        data2.append(i)
total_employees=len(data2)
count=0
for i in data2:
    if int(i[0])>2015 and int(i[1])>10:
        count+=1
# print(f"The percentage of employees who joined after 2015 and have handled more than 10 projects:{count*100/total_employees}%")
Final_file.write("Percentage of employees who joined after 2015 and have handled more than 10 projects:\n")
Final_file.write(f"The percentage of employees who joined after 2015 and have handled more than 10 projects:{count*100/total_employees}%")