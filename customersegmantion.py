import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

data = pd.read_excel("Online_Retail.xlsx")
data

data=data[pd.notnull(data['CustomerID'])]

filtered_data=data[['Country','CustomerID']].drop_duplicates()

filtered_data.Country.value_counts()[:10].plot(kind='bar')

filtered_data.Country.value_counts()

uk_data=data[data.Country=='United Kingdom']


uk_data=data[data.Country=='United Kingdom']
uk_data.info()

uk_data.describe()

uk_data = uk_data[(uk_data['Quantity']>0)]
uk_data.describe()

uk_data=uk_data[['CustomerID','InvoiceDate','InvoiceNo','Quantity','UnitPrice']]

uk_data['TotalPrice']=uk_data['Quantity']*uk_data['UnitPrice']
uk_data

uk_data['InvoiceDate'].min(),uk_data['InvoiceDate'].max()


PRESENT = dt.datetime(2011,12,10)
uk_data['InvoiceDate'] = pd.to_datetime(uk_data['InvoiceDate'])

uk_data.head()

rfm=uk_data.groupby('CustomerID').agg({'InvoiceDate':lambda date: (PRESENT-date.max()).days,
                                       'InvoiceNo':lambda num:len(num),
                                       'TotalPrice':lambda price:price.sum()})
rfm

rfm.columns=['monetary','recency','frequency']


rfm['recency'] = rfm['recency'].astype(int)
rfm.head()

rfm['r_quartile'] = pd.qcut(rfm['recency'], 4, ['1','2','3','4'])
rfm['f_quartile'] = pd.qcut(rfm['frequency'], 4, ['4','3','2','1'])
rfm['m_quartile'] = pd.qcut(rfm['monetary'], 4, ['4','3','2','1'])

rfm.head()

rfm['RFM_Score'] = rfm.r_quartile.astype(str)+ rfm.f_quartile.astype(str) + rfm.m_quartile.astype(str)
rfm.head()

rfm[rfm['RFM_Score']=='111'].sort_values('monetary', ascending=False).head()







