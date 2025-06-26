# import pandas as pd
# import datetime as dt
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')

# data = pd.read_csv("student.csv", encoding="utf-8")
# print("Total number of Male & Female: "+ str(data.shape[0]))
# features = ['id', 'name', 'class', 'mark', 'gender']
# data_clv = data[features]
# # data_clv['Totalstudent'] = data_clv['mark'].multiply(data_clv['name'])
# print(data_clv.shape)
# print(data_clv.head())
 

import pandas as pd
import warnings

warnings.filterwarnings('ignore')   #This code disables warning messages from appearing in your Python output.

#load data
data = pd.read_csv("OnlineRetail.csv", encoding="unicode_escape")
print("Total number of transactions: " + str(data.shape[0]))

#Relavent Features
features = ['CustomerID', 'InvoiceNo', 'InvoiceDate', 'Quantity', 'UnitPrice']
data_clv = data[features]

# Calculate Total Sales per transaction
data_clv['TotalSales'] = data_clv['Quantity'].multiply(data_clv['UnitPrice'])

print(data_clv.shape)      # It returns a tuple representing the number of rows and columns.
print(data_clv.head())     # returns the first 5 rows if a number is not specified.

#Invoice to datetime
data_clv['InvoiceDate'] = pd.to_datetime(data_clv['InvoiceDate'])

# Print the details of data set
maxdate = data_clv['InvoiceDate'].dt.date.max()
mindate = data_clv['InvoiceDate'].dt.date.min()
unique_customer = data_clv['CustomerID'].nunique()
total_quantity = data_clv['Quantity'].sum()
total_sales = data_clv['TotalSales'].sum()

# Output
print(f"Range of Transaction is : {mindate} to {maxdate}")
print(f"Total no. of unique customers : {unique_customer}")
print(f"Total quantity sold : {total_quantity}")
print(f"Total sales revenue : {total_sales}")

#Historical approach (aggregation:the average revenue per customer based on past transactions)
customer= data_clv.groupby('CustomerID').agg({'InvoiceDate': lambda x: (x.max() - x.min()).days,'InvoiceNo' : lambda x: len(x),'TotalSales': lambda x: sum(x)})
customer.columns = ['Age' , 'Frequency' , 'TotalSales']  #groupby :analyzing and summarizing data based on specific criteria.
customer.head()



