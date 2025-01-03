import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe

#fungsi jumlah rental sepeda setiap bulannya
def create_rent_month(df):
    rent_month = df.groupby(by='mnth').cnt.sum().reset_index()

    return rent_month

def create_rent_day(df):
    rent_day = df.groupby(by='hr').cnt.sum().reset_index()

    return rent_day

# Load cleaned data
hour_df = pd.read_csv("dashboard/hour.csv")

# mengganti nilai kolom 'season'
hour_df['season'] = hour_df['season'].replace({1:'Springer',2:'Summer',3:'Fall',4:'Winter'})

all_season = ['Springer', 'Summer', 'Fall','Winter']

#membuat filter season sebagai acuan input dashboard interaktif 
with st.sidebar:
    # Mengambil season input
    season = st.selectbox(
    label="Pilih musim:",
    options=('Springer', 'Summer', 'Fall','Winter','All_Season')
)

#membuat DataFrame baru sebagai acuan load dashboard
for i in season:
    if season == 'All_Season':
        main_df = hour_df[hour_df["season"] == hour_df["season"]]
    else:
        main_df = hour_df[hour_df["season"] == season]

#menyiapkan berbagai dataframe
rent_month = create_rent_month(main_df)
# Membuat list nama-nama bulan
bulan = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']

# Mengubah format bulan dari angka menjadi nama bulan
for i in range(0,len(bulan)):
    rent_month['mnth'] = rent_month['mnth'].replace(i+1,bulan[i])

rent_day = create_rent_day(main_df)

#membuat barchart rental perbulan dan permusim
st.header('Bike Sharing Dashboard :sparkles:')
st.subheader('Total Rent Terhadap Bulan')

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(24, 12)) #mengatur ukuran chart dan jumlah kolom chart

sns.barplot(y="mnth", x="cnt", hue="mnth", data=rent_month, ax=ax, 
            palette=["#72BCD4"])
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis ='y', labelsize=30)
ax.tick_params(axis ='x', labelsize=30)

plt.show()
st.pyplot(fig)

# membuat lineplot rental pada jam-jam tertentu
st.subheader('Jumlah Rental pada Jam-Jam Tertentu')

fig = plt.figure(figsize=(10, 5))

plt.plot(rent_day['hr'], rent_day['cnt'], marker='o', linewidth=2, color="#72BCD4") 
plt.xticks(fontsize=15) 
plt.yticks(fontsize=15) 
plt.show()

st.pyplot(fig)

#caption
st.caption('Copyright © Ilham Rizkia 2024')
