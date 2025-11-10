import pymysql
import csv

connection=pymysql.connect(host="localhost",user="root",db="sakila",passwd="12345")
cursor=connection.cursor()
file=open("aviation_data","r")
re=csv.reader(file)


st1="INSERT INTO aviation_data(Flight_ID,Airline,Source,Destination,Aircraft_Type,Departure_Time,Arrival_Time,Duration_Minutes,Ticket_Price,Status,Passenger_Count) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for i in re:
    cursor.execute(st1,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10]))
    connection.commit()




'''Q1) Write a SQL query to find the top 3 destinations with the highest number of flights.'''
stq1="select Destination,count(Flight_ID) as flight_count from aviation_data  where Status!='Cancelled' group by Destination order by flight_count desc;"
cursor.execute(stq1)
data=cursor.fetchall()
print(data[:3])


print("--------")

'''Q2) Write a SQL query to get the average passenger count for each aircraft type.'''
stq2="select Aircraft_Type,avg(Passenger_Count) as avg_Passenger_Count from aviation_data group by Aircraft_Type;"
cursor.execute(stq2)
data=cursor.fetchall()
print(data)

print("--------")


'''Q3) Write a SQL query to find all flights that are more than 3 hours long and were delayed.'''
stq3="select * from aviation_data where Duration_Minutes>180 and Status like 'Delayed';"
cursor.execute(stq3)
data=cursor.fetchall()
print(data)


print("--------")


'''Q4) Write a SQL query to calculate total ticket revenue per destination.'''
stq4="select Destination,sum(Ticket_Price*Passenger_count) as Total_Ticket_Revenue from aviation_data group by Destination;"
cursor.execute(stq4)
data=cursor.fetchall()
print(data)

print("--------")


'''Q5) Write a SQL query to get the number of on-time vs delayed vs cancelled flights for each airline.'''
stq5="select Status,count(Flight_ID) as flight_count from aviation_data group by Status;"
cursor.execute(stq5)
data=cursor.fetchall()
print(data)