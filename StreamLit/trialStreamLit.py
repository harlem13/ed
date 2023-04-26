import streamlit as st
import pandas as pd

# import plotly.express as px
# from PIL import Image

st.write("""First App""")

header = st.container()
dataset = st.container()
features = st.container()

with header:
    st.title("YNT Support Tickets")
    st.text("You can access the report of YNT support requests from this api.")

with dataset:
    st.header("Dataset from BTYP")
    st.header("Data_csv")

    df = pd.read_csv('/Users/adnanc/SpyderProjects/HelloSpidey/S_data5.csv')
    st.write(df.head())  # first 5 entry
    # nbr_tickets=btyp_data.count(0)
    # print(nbr_tickets)
    st.dataframe(df)

    st.header("Data_excel")
    excel_f = '/Users/adnanc/SpyderProjects/HelloSpidey/S_data6.xlsx'
    sheet_n = 'data1'
    df2 = pd.read_excel(excel_f, sheet_name=sheet_n, usecols='A:C', header=0)
    st.write(df2.head())  # first 5 entry
