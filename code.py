
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#import the data
df=pd.read_csv(r'E:\test\new-york-city-airbnb-open-data\AB_NYC_2019.csv')
#be care of keeping the integrity of data, it’s better to create an original file to avoid irreversible effort 
original=pd.read_csv(r'E:\test\new-york-city-airbnb-open-data\AB_NYC_2019.csv')

#observe the data
df.head()

#check the null
df.isnull().sum()

#delete irrelevant columns
df.drop(['id','host_name','last_review'],axis=1,inplace=True)

#replace  NaN values
df.fillna({'reviews_per_month':0},inplace=True)
df.fillna({'name':0},inplace=True)
df.isnull().sum()

#check the different types 
df['room_type'].unique()
df['neighbourhood_group'].unique()

#how many listings for each host 
#option 1:
top_host=df.host_id.value_counts().head(10)
#option 2:
top_host1=df.groupby(['host_id']).name.count()
top_host1=top_host1.sort_values(ascending=False).head(10)
top_host1

#visulization
sns.set(rc={'figure.figsize':(10,8)})
chart1=top_host1.plot(kind='bar',width=0.5,color=['r','g','m','c','c','c','c','c','c','c'])
sns.set_style('darkgrid')
chart1.set_title('Hosts with most listings in NYC',fontsize=15,color='r',fontweight='bold')
chart1.set_xlabel("Hosts's ID")
chart1.set_ylabel('Num of Listings')
chart1.set_xticklabels(chart1.get_xticklabels(),rotation=45)
plt.savefig('E:/test/new-york-city-airbnb-open-data/Hosts with most listings in NYC.png')

#the relationship across neighbourhood_group and price
#Brooklyn
sub1=df.loc[df['neighbourhood_group']=='Brooklyn']
price_sub1=sub1['price']

#Manhattan
sub2=df.loc[df['neighbourhood_group']=='Manhattan']
price_sub2=sub2['price']

#Queens
sub3=df.loc[df['neighbourhood_group']=='Queens']
price_sub3=sub3['price']

#Staten Island
sub4=df.loc[df['neighbourhood_group']=='Staten Island']
price_sub4=sub4['price']

#Bronx
sub5=df.loc[df['neighbourhood_group']=='Bronx']
price_sub5=sub5['price']

#After filtering the series ,combined to dataframe :
price_sum=[price_sub1.describe(), price_sub2.describe(), price_sub3.describe(), price_sub4.describe(), price_sub5.describe()]
price_list=pd.DataFrame(price_sum)
price_list.index=['Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Bronx']
price_list=price_list.T
price_list

#violinplot
df=df[df.price<500]
chart2=sns.violinplot(data=df,x='neighbourhood_group',y='price')
chart2.set_title('Price Distribution Across Neighbourhood group',fontsize=15,color='r',fontweight='bold')
chart2
plt.savefig('E:/test/new-york-city-airbnb-open-data/Price Distribution Across Neighbourhood group.png')

#boxplot
chart3=sns.boxplot(x='neighbourhood_group',y='price',data=df,showfliers=False)
chart3.set_title('Price distribution in different neighbourhood_group\n price<500 ',fontsize=15,color='r',fontweight='bold')
plt.savefig('E:/test/new-york-city-airbnb-open-data/Price distribution in different neighbourhood group price below 500 .png')

#longitude and latitude across listings
chart4=df.plot(figsize=(10,8),kind='scatter',x='longitude',y='latitude',marker='.',label='availability_365',c='price',cmap=plt.get_cmap('jet'),colorbar=True)
chart4.set_title('Listing distribution according to postion across the price ',fontsize=15,color='r',fontweight='bold')
chart4
plt.savefig('E:/test/new-york-city-airbnb-open-data/Listing distribution according to postion across the price.png')

#the relationship btw room_type and price
pivot_table2=df.pivot_table(values='price',index='neighbourhood_group',columns='room_type',aggfunc='mean').plot.bar()
pivot_table2.set_ylabel('Price',color='r',fontsize=13)
pivot_table2.set_xlabel('Neighbourhood_group',color='r',fontsize=13)
pivot_table2.set_xticklabels(pivot_table2.get_xticklabels(),rotation=45)
pivot_table2.set_title('Average Price by Room Type',fontsize=15,color='r',fontweight='bold')
plt.savefig('E:/test/new-york-city-airbnb-open-data/Average Price by Room Type.png')

# check the number of listings by Room Type across zone
pivot_table3=df.pivot_table(values='price',index='neighbourhood_group',columns='room_type',aggfunc='count').plot.bar()
pivot_table3.set_xlabel('Neighbourhood_group',color='r',fontsize=13)
pivot_table3.set_ylabel('Num of listings',color='r',fontsize=13)
pivot_table3.set_xticklabels(pivot_table2.get_xticklabels(),rotation=45)
pivot_table3.set_title('Num of listing by Room Type across zone',fontsize=15,color='r',fontweight='bold')
plt.savefig('E:/test/new-york-city-airbnb-open-data/Num of listing by Room Type across zone.png')

#sort the largest num of reviews
top_review=df.sort_values(by=['number_of_reviews'],ascending=False).head(10)

#calculate the average price
avg_price=top_review.price.mean()

