#7

import csv
import pymysql
connection= pymysql.connect(host='localhost',user='root',passwd='12345',db='sakila')
cursor=connection.cursor()

file=open("telecom_data",'r')
r=csv.reader(file)
data=[]
for i in r:
    data.append(i)
st='INSERT INTO telecom_data(customer_id,plan_type,call_minutes,data_usage_gb,messages_sent,monthly_bill,region) VALUES(%s,%s,%s,%s,%s,%s,%s)'
for i in data:
    cursor.execute(st,(i[0].strip(),i[1].strip(),i[2].strip(),i[3].strip(),i[4].strip(),i[5].strip(),i[6].strip()))
    connection.commit()
file.close()

'''Count the total number of customers.'''
print(f"The total no of cutomers={len(data)}")

print("--------")

'''Find the number of customers in each region.'''
st1='SELECT region,count(customer_id) FROM telecom_data GROUP BY region;'
cursor.execute(st1)
d=cursor.fetchall()
print(d)

print("--------")

'''Calculate the average monthly bill for all customers.'''
st2='SELECT avg(monthly_bill) FROM telecom_data;'
cursor.execute(st2)
d=cursor.fetchall()
print(f"The average monthly bill for all customers={d[0][0]}")

print("--------")

'''Identify the highest data usage (in GB) among all customers.'''
print("The highest data usage (in GB) among all customers:")
st3='SELECT * FROM telecom_data ORDER BY data_usage_gb DESC;'
cursor.execute(st3)
d=cursor.fetchall()
print(d[0])

print("--------")

'''Find the customer who sent the most messages.'''
print("The customer who sent the most messages:")
st4='SELECT * FROM telecom_data ORDER BY messages_sent DESC;'
cursor.execute(st4)
d=cursor.fetchall()
print(d[0])

print("--------")

'''Count how many customers are on the 'Postpaid' plan.'''
st5="SELECT count(customer_id) FROM telecom_data GROUP BY plan_type HAVING plan_type LIKE 'Postpaid';"
cursor.execute(st5)
d=cursor.fetchall()
print(f"No. of customers are on the 'Postpaid' plan:{d[0][0]}")

print("--------")

'''Calculate the average call minutes used by 'Prepaid' customers.'''
st6='SELECT avg(call_minutes) FROM telecom_data GROUP BY plan_type HAVING plan_type LIKE "Prepaid";'
cursor.execute(st6)
d=cursor.fetchall()
print(f"The average call minutes used by 'Prepaid' customers:{d[0][0]}")

print("--------")

'''List customers whose monthly bill exceeds ₹1000.'''
st7='SELECT * FROM telecom_data WHERE monthly_bill>1000;'
cursor.execute(st7)
d=cursor.fetchall()
print(d)

print("--------")

'''Find the region with the highest number of 'Corporate' plan customers.'''
st8="SELECT region,count(customer_id) as count FROM telecom_data WHERE plan_type LIKE 'Corporate' GROUP BY region ORDER BY count DESC;"
cursor.execute(st8)
d=cursor.fetchall()
print(d[0])

print("--------")

'''Calculate the total data consumed in the 'North' region.'''
st9="SELECT region,sum(data_usage_gb) FROM telecom_data GROUP BY region HAVING region like 'North';"
cursor.execute(st9)
d=cursor.fetchall()
print(d[0])

print("--------")

'''List top 5 customers with highest call minutes.'''
st10="SELECT * FROM telecom_data ORDER BY call_minutes DESC;"
cursor.execute(st10)
d=cursor.fetchall()
print(d[:5])

print("--------")

'''Find the average number of messages sent by customers in the 'East' region.'''
st11="SELECT region, avg(messages_sent) as avg_msgs_sent FROM telecom_data WHERE region like 'East' GROUP BY region;"
cursor.execute(st11)
d=cursor.fetchall()
print(d)


print("--------")

'''Which plan type has the highest average monthly bill?'''
st12="SELECT plan_type, avg(monthly_bill) as avg_monthly_bill FROM telecom_data GROUP BY plan_type ORDER BY avg_monthly_bill DESC;"
cursor.execute(st12)
d=cursor.fetchall()
print(d[0])

print("--------")

'''Find customers who used less than 100 call minutes and sent more than 200 messages.'''
st13="SELECT * FROM telecom_data where call_minutes<100 and messages_sent>200;"
cursor.execute(st13)
d=cursor.fetchall()
print(d)

print("--------")

'''Find the percentage of customers using more than 20GB of data.'''
st14="SELECT customer_id FROM telecom_data WHERE data_usage_gb>20;"
cursor.execute(st14)
d=cursor.fetchall()
perc=(len(d)/len(data))*100
print(f"Percentage of customers using more than 20GB of data={perc}%")
st15="SELECT * FROM telecom_data WHERE"
