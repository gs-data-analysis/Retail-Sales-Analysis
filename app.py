import streamlit as st #web app 
import pandas as pd # data manipulation
import numpy as np # random gen
import plost

#import matplotlib.pyplot as plt
#matplotlib inline

import seaborn as sns


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.title("Retail Sales Analytics for store XYZ")

#df = pd.read_csv('https://github.com/gs-data-analysis/Retail-Sales-Analysis/blob/main/pos4.csv',error_bad_lines=False)


df = pd.read_csv("/Users/ramya/pos4.csv",error_bad_lines=False)
df[["create_date","write_date"]]=df[["create_date","write_date"]].apply(pd.to_datetime)
df[["name","full_product_name"]]=df[["name","full_product_name"]].astype('string')

df['month_year'] = df['create_date'].apply(lambda x: x.strftime('%Y-%m'))
df_temp = df.groupby('month_year').sum()['price_subtotal_incl'].reset_index()
#plt.figure(figsize=(16, 5))
#plt.plot(df_temp['month_year'], df_temp['price_subtotal_incl'], color='#b80045')
#plt.xticks(rotation='vertical', size=8)
#plt.show()

print(df_temp)


st.markdown("")
st.subheader("Overall Sales Trend")

plost.line_chart(
    data = df_temp,
    x = 'month_year',
    y = 'price_subtotal_incl'
)


# Grouping products by sales
prod_sales = pd.DataFrame(df.groupby('full_product_name').sum()['price_subtotal_incl'])

# Sorting the dataframe in descending order
prod_sales.sort_values(by=['price_subtotal_incl'], inplace=True, ascending=False)


a1,a2 = st.columns((6,4))
with a1:
    st.subheader("Top 10 products by sales")
    st.markdown("")
    # Top 10 products by sales
    prod_sales[:10]

    ##plost.bar_chart(
        #data = prod_sales,
        # bar = 'full_product_name',
        #value = 'price_subtotal_incl'
    #)

with a2:
   
    st.subheader("Most selling by quantity")
    st.markdown("")
    # Grouping products by Quantity
    best_selling_prods = pd.DataFrame(df.groupby('full_product_name').agg(Qty=('qty', 'sum'), NoOfOrders=('qty', 'count')))

    # Sorting the dataframe in descending order
    best_selling_prods.sort_values(by=['Qty','NoOfOrders'], inplace=True, ascending=False)

    # Most selling products
    best_selling_prods[:10]