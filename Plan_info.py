#16

import pandas as pd

plans=pd.read_csv("plans")
complaints=pd.read_csv("complaints")
usage=pd.read_csv("usage")
sub=pd.read_csv("subscriptions")
customers=pd.read_csv("customers")


#JOINS
'''Join customers and subscriptions to find each customer's active plan details.'''
cus_sub=pd.merge(customers,sub,how='inner',on='customer_id')
print(cus_sub)

print("--------")

'''Perform an inner join between subscriptions and plans to get the monthly fee and data limit for each subscription.'''
sub_plan=pd.merge(plans,sub,how='inner',on='plan_id')
print(sub_plan)


print("--------")

'''Join usage and customers to identify customers from "New York" with more than 50GB monthly usage.'''
usage_cus=pd.merge(usage,customers,how='inner',on='customer_id')
print(usage_cus[(usage_cus["city"]=="New York") & (usage_cus["data_used_gb"]>50)])

print("--------")


'''Combine complaints and customers to find customers who raised more than 3 complaints in 2023.'''
complaints_cus=pd.merge(complaints,customers,how='inner',on='customer_id')
r=complaints_cus.groupby("customer_id")["complaint_id"].count().reset_index(name="no_of_complaints")
print(r[(r["no_of_complaints"]>3)])

print("--------")


'''Join all datasets to create a master table with customer details, plan info, usage, and complaint records.'''
master_table=pd.merge(usage_cus,sub_plan,how='inner',on="customer_id")
master_table=pd.merge(master_table,complaints,how='inner',on="customer_id")
print(master_table)


print("--------")


#GroupBy with Aggregations

'''Find the total data usage per city and sort by descending order.'''
r=usage_cus.groupby("city")["data_used_gb"].sum().reset_index(name="total_data_usage")
print(r.sort_values(by="total_data_usage",ascending=False))

print("--------")


'''Calculate the average voice minutes used by gender.'''
r=usage_cus.groupby("gender")["voice_minutes_used"].mean().reset_index(name="average_voice_minutes")
print(r)


print("--------")




'''Group customers by plan type (Basic, Premium, etc.) and find the maximum, minimum, and average monthly data usage.'''
max=master_table.groupby("plan_name")["data_used_gb"].max().reset_index(name="max_data_usage")
print(max)
print("-----------")
min=master_table.groupby("plan_name")["data_used_gb"].min().reset_index(name="min_data_usage")
print(min)
print("-----------")
mean=master_table.groupby("plan_name")["data_used_gb"].mean().reset_index(name="mean_data_usage")
print(mean)


print("--------")

'''Find the total revenue generated per city (monthly_fee * number of active subscriptions).'''
r=pd.merge(plans,sub,how='inner',on='plan_id')
total_revenue=r.groupby("plan_id")["customer_id"].count().reset_index(name="number_of_active_subscriptions")
total_revenue=pd.merge(total_revenue,r,how="inner",on="plan_id")
total_revenue["total_revenue"]=total_revenue["number_of_active_subscriptions"]*total_revenue["monthly_fee"]
total_revenue=pd.merge(total_revenue,cus_sub,how='inner',on='plan_id')
total_revenue=total_revenue.groupby("city")["total_revenue"].sum().reset_index(name='total_revenue')
print(total_revenue[["city","total_revenue"]])

print("--------")

'''Group by complaint type and count the number of resolved complaints.'''
r=complaints.groupby(["complaint_type","status"])["complaint_id"].count().reset_index(name="no_of_complaints")
print(r[r["status"]=="Resolved"])

print("--------")


#Data Cleaning
'''Identify customers with missing end_date in subscriptions and replace with "Active".'''
sub["end_date"]=sub["end_date"].fillna("Active")
print(sub)


print("--------")

'''Detect and remove duplicate entries in usage dataset.'''
usage=usage.drop_duplicates()
print(usage)


print("--------")

'''Handle missing values in complaints (if any) by filling with "Unknown".'''
complaints=complaints.fillna("Unknown")
print(complaints)


print("--------")


'''Standardize city names in customers (e.g., "new york", "New-York" → "New York").'''
def Standardize(c):
    if c=="new york" or c=="New-York" or "c==New York":
        return "New York"
    elif c=="Houston" or c=="houston":
        return "Houston"
    elif c=="Phoenix" or c=="phoenix":
        return "Phoenix"
    elif c=="Chicago" or c=="chicago":
        return "Chicago"
    elif c=="Los Angeles" or c=="los angeles" or c=="Los-Angeles":
        return "Los Angeles"

customers["city"]=customers["city"].apply(Standardize)
print(customers)


print("--------")



'''Remove outliers in usage where data_used_gb > 100GB and voice_minutes_used > 2000.'''
usage_cleaned=usage[(usage["data_used_gb"]<=100) & (usage["voice_minutes_used"]<=2000)]
print(usage_cleaned)