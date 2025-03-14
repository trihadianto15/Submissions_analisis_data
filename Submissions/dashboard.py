import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_byhr_df(df):
    byhr_df = df.groupby(by="hr").agg({
        "cnt": "max"
    }).reset_index()
    
    return byhr_df

def create_byweathersit_temp_df(df):
    byweathersit_temp_df = df.groupby(by=["weathersit", "temp"]).agg({
      "cnt": "sum" 
    }).reset_index()

    return byweathersit_temp_df

df_hour = pd.read_csv("https://raw.githubusercontent.com/trihadianto15/Submissions_analisis_data/refs/heads/main/Submissions/all_hour.csv")

datetime_columns = ["dteday"]
df_hour.sort_values(by="dteday", inplace=True)
 
for column in datetime_columns:
    df_hour[column] = pd.to_datetime(df_hour[column])


min_date = df_hour["dteday"].min()
max_date = df_hour["dteday"].max()
 
with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = df_hour[(df_hour["dteday"] >= str(start_date)) & 
                (df_hour["dteday"] <= str(end_date))]


byhr_df = create_byhr_df(main_df)
byweathersit_temp_df = create_byweathersit_temp_df(main_df)

st.header('URBAN CYCLE')

st.subheader('Penyewaan Sepeda')
 
col1, col2, col3 = st.columns(3)
 
with col1:
    total_cnt = main_df["cnt"].sum()
    st.metric("Total penyewa", value=total_cnt)

with col2:
    total_casual = main_df["casual"].sum()
    st.metric("Total Casual", value=total_casual)

with col3:
    total_registered = main_df["registered"].sum()
    st.metric("Total registered", value=total_registered)


st.subheader("Penyewaan sepeda menurut jam")

  
col1, col2 = st.columns(2)

with col1:

    fig, ax = plt.subplots(figsize=(23, 10))
 
    sns.barplot(
    y="cnt", 
    x="hr",
    data=byhr_df.sort_values(by="cnt", ascending=False),
    ax=ax
    )
    ax.set_title("Penyewaan sepeda terbanyak menurut jam", loc="center", fontsize=50)
    ax.set_ylabel("cnt")
    ax.set_xlabel("hr")
    ax.tick_params(axis='x', labelsize=35)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)


with col2:
    st.write(byhr_df[["hr", "cnt"]])

st.subheader("Penyewaan sepeda menurut weathersit dan temp")

col1, col2 = st.columns(2)

set_1 = byweathersit_temp_df[byweathersit_temp_df["weathersit"]==1]
set_2 = byweathersit_temp_df[byweathersit_temp_df["weathersit"]==2]

with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.lineplot(
        y="cnt",
        x="temp",
        data=set_1,
        marker="o",
        linewidth=4,
        color="#72BCD4",
        ax=ax 
    )
    ax.set_title("Pengaruh weathersit 1 dan temp dalam penyewaan sepeda", loc="center", fontsize=50)
    ax.set_ylabel("cnt")
    ax.set_xlabel("temp")
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.lineplot(
        y="cnt",
        x="temp",
        data=set_2,
        marker="o",
        linewidth=4,
        color="#db1514",
        ax=ax 
    )
    ax.set_title("Pengaruh weathersit 2 dan temp dalam penyewaan sepeda", loc="center", fontsize=50)
    ax.set_ylabel("cnt")
    ax.set_xlabel("temp")
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

col3, col4 = st.columns(2)

set_3 = byweathersit_temp_df[byweathersit_temp_df["weathersit"]==3]
set_4 = byweathersit_temp_df[byweathersit_temp_df["weathersit"]==4]

with col3:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.lineplot(
        y="cnt",
        x="temp",
        data=set_3,
        markers="o",
        linewidth=4,
        color="#FFFF00",
        ax=ax
    )
    ax.set_title("Pengaruh weathersit 3 dan temp dalam penyewaan sepeda", loc="center", fontsize=50)
    ax.set_ylabel("cnt")
    ax.set_xlabel("temp")
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

with col4:
    fig, ax = plt.subplots(figsize=(20, 10))

    sns.lineplot(
        y="cnt",
        x="temp",
        data=set_4,
        markers="o",
        linewidth=4,
        color="#008000",
        ax=ax
    )
    ax.set_title("Pengaruh weathersit 4 dan temp dalam penyewaan sepeda", loc="center", fontsize=50)
    ax.set_ylabel("cnt")
    ax.set_xlabel("temp")
    ax.tick_params(axis="x", labelsize=35)
    ax.tick_params(axis="y", labelsize=35)
    st.pyplot(fig)

with st.sidebar:
    st.caption("Sukabumi, 2025")
