#12

import json
with open ("banking_customers") as file:
    data=json.load(file)



'''Find the total number of customers in each bank'''   #q1
bank_customers={}
for i in data:
    if i["bank_name"] not in bank_customers.keys():
        bank_customers[i["bank_name"]]=0
    bank_customers[i["bank_name"]]+=1
print(bank_customers)


print("--------")

'''List all unique account types present across all customers'''   #q2
acc_types=[]
for i in data:
    for j in i["account_types"]:
        if j not in acc_types:
            acc_types.append(j)
print(acc_types)

print("--------")


'''Find the average account balance of customers from 'Mumbai'''   #q3
c=0
bal=0
for i in data:
    if i["address"]["city"]=='Mumbai':
        c+=1
        bal+=i["balance"]
print(f"The average account balance of customers from 'Mumbai'={bal/c}")

print("--------")

'''Get the highest balance and the corresponding customer name'''   #q4
m_bal=0
for i in data:
    if i['balance']>m_bal:
        m_bal=i['balance']
        name=i["customer_name"]
print(f"The highest balace of {m_bal} was in {name}'s bank")

print("--------")


'''Count the number of customers who have both 'Savings' and 'Current' accounts'''   #q5
name={}
c=0
for i in data:
    if i["customer_name"] not in name.keys():
        name[i["customer_name"]]=[]
    for j in i["account_types"]:
        if j=='Savings' or j=='Current':
            if j not in name[i["customer_name"]]:
                name[i["customer_name"]].append(j)
for n in name.keys():
    if len(name[n])==2:
        c+=1
print(f"The number of customers who have both 'Savings' and 'Current' accounts={c}")

print("--------")

'''Find the total balance of customers from each state'''   #q6
statewise={}
for i in data:
    if i["address"]["state"] not in statewise.keys():
        statewise[i["address"]["state"]]=0
    statewise[i["address"]["state"]]+=i["balance"]
print(statewise)

print("--------")


'''List all customers having more than ₹50,000 balance in "HDFC Bank"'''   #q7
names=[]
for i in data:
    if i["bank_name"]=='HDFC Bank' and i['balance']>50000 and i["customer_name"] not in names:
        names.append(i["customer_name"])
print(names)

print("--------")

'''Find the total number of customers in each city'''   #q8
citywise={}
for i in data:
    if i['address']['city'] not in citywise.keys():
        citywise[i['address']['city']]=[]
    if i["customer_name"] not in citywise[i['address']['city']]:
        citywise[i['address']['city']].append(i["customer_name"])
for city in citywise.keys():
    print(f"{city}:{len(citywise[city])}")

print("--------")


'''Calculate the percentage of customers having 'Fixed Deposit' accounts'''   #q9
names=[]
Fixed_names=[]
for i in data:
    if i["customer_name"] not in names:
        names.append(i["customer_name"])
    if 'Fixed Deposit' in i["account_types"] and i["customer_name"] not in Fixed_names:
        Fixed_names.append(i["customer_name"])
print(f"Percentage of customers having 'Fixed Deposit' accounts={len(Fixed_names)*100/len(names)}%")