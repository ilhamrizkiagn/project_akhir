import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

#fungsi jumlah rental sepeda setiap bulannya
def create_rent_month(df):
    rent_month = df.groupby(by='mnth')[['cnt']].sum()

    return rent_month

#fungsi jumlah rental per musim
def create_rent_season(df):
    day_season = df.groupby(by='season')[['cnt']].sum()

    return day_season

#fungsi jumlah rental per kondisi cuaca
def create_rent_weather(df):
    day_weather = df.groupby(by='weathersit')[['cnt']].sum()

    return day_weather

# Load cleaned data
day_df = pd.read_csv("dashboard/day.csv")
hour_df = pd.read_csv("dashboard/hour.csv")

#membuat copy data day
day_1 = day_df.copy()
day_1.replace({1:'Springer',2:'Summer',3:'Fall',4:'Winter'},inplace=True)
day_2 = day_df.copy()
day_2['weathersit'].replace({1:'Good',2:'Mist with Cloudy',3:'Varied',4:'Bad'},inplace=True)

#buat proporsi antara pengguna casual dan pengguna terdaftar
prop_casual = day_df['casual'].sum()
prop_registered = day_df['registered'].sum()

#tiap nilai dimasukkan ke dalam DataFrame
prop = pd.DataFrame({'user':['casual','registered'],'jumlah':[prop_casual,prop_registered]})

#menyiapkan berbagai dataframe
rent_month = create_rent_month(day_df)
day_season = create_rent_season(day_1)
day_weather = create_rent_weather(day_2)

#membuat barchart rental perbulan dan permusim
st.header('Bike Sharing Dashboard :sparkles:')
st.subheader('Total Rent on Time Period')

#mengatur ukuran chart dan jumlah kolom chart
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

#membuat barchart perbulan di sebelah kiri
sns.barplot(x="mnth", y="cnt", data=rent_month, ax=ax[0],palette=["#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Total Rent per Month", fontsize=15)
ax[0].tick_params(axis ='y', labelsize=12)

#membuat barchart permusim di sebelah kanan
sns.barplot(x="season", y="cnt", data=day_season.sort_values(by='cnt',ascending=False),ax=ax[1],palette=["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Total Rent per Season", loc="center", fontsize=15)
ax[1].tick_params(axis='y', labelsize=12)
 
plt.suptitle("Total Rent on Time Period", fontsize=20)
plt.show()
st.pyplot(fig)

st.subheader('Rent Based On Weather')
#mengatur ukuran chart
fig, ax = plt.subplots(figsize=(16, 8))

#membuat barchart jumlah rental terhadap kondisi cuaca
sns.barplot(x="weathersit", y="cnt", data=day_weather,palette=["#D3D3D3", "#72BCD4", "#D3D3D3"],errorbar=None)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Total Rent Based On Weather", fontsize=15)

plt.show()
st.pyplot(fig)

st.subheader('Casual vs Registered Percentage')
# membuat pie chart terhadap proporsi pengguna casual dan terdaftar
fig, ax = plt.subplots(figsize=(16, 8))
plt.pie(data=prop,x='jumlah',labels='user',autopct='%.0f%%')
ax.set_title('Persentage of Casual and Registered User')

# menampilkan chart
plt.show()

st.pyplot(fig)

st.caption('Copyright © Ilham Rizkia 2024')
