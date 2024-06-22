# Import the libraries
import streamlit as st
# import mysql.connector
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine
import altair as alt



# HEAD
# Title
st.set_page_config(
    page_title="Adventureworks Dashboard",
    page_icon="🚲",
    layout="wide",
    initial_sidebar_state="expanded")

# connect to database
# conn = st.connection("mydb", type="sql", autocommit=True)
host="kubela.id"
port=3306
user="davis2024irwan"
password="wh451n9m%40ch1n3" #encode '@' as '%40'
database="aw"

connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
conn = create_engine(connection)
st.title("Visualisasi Data dari Database Adventure Works")


# SIDEBAR
with st.sidebar:
    st.title('🚲 *Adventureworks Dashboard*')

#     query_year = """select distinct d.CalendarYear 
# from dimtime d"""
#     data_year = pd.read_sql(query_year, connection)
#     year_list = list(data_year.CalendarYear.unique())[::-1]
#     selected_year = st.selectbox('Select a year', year_list)
    st.markdown('#### IMDB Dashboard')
    st.write("[Click here to the link](https://sifodavis-21082010120-imdb.streamlit.app/)")
    st.markdown("#### GitHub Link")
    st.write("[Click here to the link](https://github.com/kharistya281/FPDAVIS-21082010120.git)")

    st.write("Nama : Kharisma Agustya Zahra Salsabilla")
    st.write("NPM  : 21082010120")
    st.write("Matkul : Data Visualisasi Par A")

# =========================================================
# =========================================================

# TRY INSPECT KUBELA.ID'S TABLES
# def get_tables():
#     # connection = create_connection()
#     try:
#         cursor = connection.cursor()
#         # connection = koneksi ke database 
#         # cursor = digunakan untuk mengksekusi perintah SQL dan mengambil hasil dari perintah tersebut 
#         cursor.execute("SHOW TABLES")
#         # execute = memerintah eksekusi perintah SQL 
#         tables = cursor.fetchall()
#         # fetchall = untuk mendapatkan daftar semua tabel yang ada dalam database 

#         # Mengembalikan daftar tabel
#         return [table[0] for table in tables] 
    
#     except mysql.connector.Error as err:
#         st.error(f"Error: {err}")
#         return []
    
#     # finally:
#     #     if connection.is_connected():
#     #         cursor.close()
#     #         connection.close()

# tables = get_tables()
# if tables: 
#     st.write('Tabel-tabel dalam database: ')
#     for table in tables:
#         st.write(table)
# else:
#     st.write('Tidak ada tabel ditemukan atau ada terjadi kesalahan.')

# def get_data_table(tableName):
#     # connection = create_connection()
#     query = f"SELECT * FROM {tableName}"
#     table = pd.read_sql(query, connection)
#     st.write(f"Tabel {tableName.capitalize()}")
#     st.dataframe(table)

# get_data_table('dimtime')
# get_data_table('dimsalesterritory')
# get_data_table('dimreseller')
# get_data_table('dimproductsubcategory')
# get_data_table('dimproductcategory')
# get_data_table('dimproduct')
# get_data_table('factinternetsales')


# =========================================================
# =========================================================


# Relationship (scatter plot) 

query1 = """select d.AnnualSales, d.AnnualRevenue, d2.CountryRegionCode 
from dimreseller d 
join dimgeography d2 on d.GeographyKey = d2.GeographyKey
group by d2.CountryRegionCode, d.AnnualSales, d.AnnualRevenue """

data1 = pd.read_sql(query1, conn)

st.markdown("#### Scatter plot of Annual Sales and Annual Revenue")
st.write("*RELATIONSHIP CHART - SCATTER PLOT*")
# st.scatter_chart(
#     data1, 
#     x='AnnualRevenue', 
#     y='AnnualSales',
#     size='CountryRegionCode',
#     color='CountryRegionCode'
#     )

chart = alt.Chart(data1).mark_circle().encode(
    x='AnnualRevenue',
    y='AnnualSales',
    size='CountryRegionCode',
    color='CountryRegionCode'
).interactive()

st.altair_chart(chart, use_container_width=True)

# fig, ax = plt.subplots(figsize=(10, 6))
# ax.scatter(data1['AnnualSales'], data1['AnnualRevenue'])
# ax.set_xlabel('Annual Sales')
# ax.set_ylabel('Annual Revenue')
# ax.set_title('Scatter plot of Annual Sales and Annual Revenue')

# st.pyplot(fig)

st.write("Grafik tersebut menunjukkan korelasi positif antara penjualan tahunan (Annual Sales) dan pendapatan tahunan (Annual Revenue) berdasarkan Country Region Code. Artinya, ketika penjualan meningkat, maka pendapatan ikut meningkat. Semakin tinggi penjualan tahunan, semakin tinggi pula pendapatan tahunan. Hal ini ditunjukkan oleh titik-titik yang bergerak semakin naik ke kanan atas. Ini menunjukkan bahwa ada hubungan linier yang cukup kuat antara penjualan tahunan dengan pendapatan tahunan. Hubungan dalam grafik tersebut menunjukkan bahwa peningkatan penjualan cenderung berkontribusi secara signifikan terhadap peningkatan pendapatan. ")
st.write("Secara umum, grafik menunjukkan tren yang meningkat untuk semua region, namun dengan beberapa perbedaan dalam kinerja rata-rata per region. Region GB dan US menunjukkan pola peningkatan yang konsisten menandakan bahwa entitas dari wilayah ini lebih cenderung memiliki pendapatan dan penjualan yang lebih tinggi. Region AU dan CA cenderung memiliki pendapatan dan penjualan yang lebih rendah, mungkin menunjukkan kondisi ekonomi atau pasar yang berbeda di wilayah tersebut. ")

# Comparison
st.markdown("#### Total Product Cost by Month")
st.write("*COMPARISON CHART - LINE CHART*")
query2 = """select d.CalendarYear, d.MonthNumberOfYear, sum(f.TotalProductCost) as TotalProductCost
from dimtime d 
join factinternetsales f on f.OrderDateKey = d.TimeKey 
group by d.CalendarYear, d.MonthNumberOfYear 
order by d.CalendarYear, d.MonthNumberOfYear"""

data2 = pd.read_sql(query2, conn)

# fig2, ax2 = plt.subplots()
# for year, group in data2.groupby('CalendarYear'):
#     ax2.plot(group['MonthNumberOfYear'], group['TotalProductCost'], marker='o', label=str(year))
# ax2.set_xlabel=('Month')
# ax2.set_ylabel=('Total Cost')
# ax2.set_title('Total Product Cost by Month')
# ax2.legend(title='Year', loc='upper right')
# plt.xticks(rotation=45)
# st.pyplot(fig2)

st.line_chart(
    data2,
    x='MonthNumberOfYear',
    y='TotalProductCost',
    color='CalendarYear'
)
st.write("Grafik diatas menunjukkan total biaya produk per bulan dari tahun 2001 hingga 2004. Dapat dilihat dari grafik, total biaya di tahun 2001 di mulai dari bulan Juli yang relatif stabil dengan sedikit fluktuasi sepanjang tahun. Di tahun 2002, total biaya produk cenderung stabil, namun di bulan Juli, mengalami penurunan. Hingga akhir mengalami fluktuasi. Di tahun 2003, total biaya produk cukup stabil, hingga di bulan Juli mengalami kenaikan yang cukup pesat sampai akhir tahun. Perubahan yang fluktuatif yang stabil dari akhir tahun 2003 hingga pertengahan tahun 2004. Terjadi penurunan ekstrim total biaya produk di sekitar Juni menuju bulan Juli 2004.")


# COMPOSITION 
st.markdown("#### Total Order Quantity by Sales Territory")
st.write("*COMPOSITION CHART - STACKED COLUMN CHART*")
query4 = """select d.SalesTerritoryCountry,  d3.EnglishProductSubcategoryName, sum(f.OrderQuantity) as OrderQuantity
from dimsalesterritory d 
join factinternetsales f on f.SalesTerritoryKey = d.SalesTerritoryKey
join dimproduct d2 on f.ProductKey = d2.ProductKey 
join dimproductsubcategory d3 on d2.ProductSubcategoryKey = d3.ProductSubcategoryKey
group by d3.EnglishProductSubcategoryName, d.SalesTerritoryCountry """

data4 = pd.read_sql(query4, conn)

chart_bar = pd.DataFrame(
    {
        "SubCategoryProduct": data4['EnglishProductSubcategoryName'],
        "OrderQuantity": data4['OrderQuantity'],
        "SalesTerritoryCountry": data4['SalesTerritoryCountry'],
    }
)


st.bar_chart(chart_bar, x='SubCategoryProduct', y='OrderQuantity', color='SalesTerritoryCountry')
st.write("Grafik di atas menggambarkan jumlah total pesanan berdasarkan wilayah penjualan untuk berbagai kategori produk. Kategori barang Tires and Tubes memiliki jumlah pesanan yang paling tinggi di semua kategori produk di wilayah penjualan Amerika Serikat. Dari semua kategori produk, Amerika Serikat menjadi wilayah penjualan yang paling banyak jumlah pemesanannya dibanding dengan daerah yang lain. Wilayah seperti Australia, Canada, France, Germany, dan United Kingdom juga berkontribusi, tetapi dalam jumlah yang lebih kecil dibandingkan dengan Amerika Serikat. ")
st.write("Kategori barang Helmets, Bottles and Cages, dan Road Bikes menjadi kategori barang terbanyak yang Tires and Tubes, dan hampir merata jumlah pesanannya di semua wilayah penjualan. Kategori lain seperti Gloves, Hydration Packs, dan Touring Bikes memiliki jumlah pesanan yang lebih rendah dibandingkan kategori lainnya. ")

# DISTRIBUTION
st.markdown("#### Distribution Sum of Order Quantity by Quarter")
st.write("*DISTRIBUTION CHART - BAR CHART*")
query3 = """select d.CalendarQuarter, d.CalendarYear, sum(f.OrderQuantity) as OrderQuantity
from dimtime d 
join factinternetsales f on f.OrderDateKey = d.TimeKey 
group by d.CalendarQuarter, d.CalendarYear
order by d.CalendarYear, d.CalendarQuarter"""

data3 = pd.read_sql(query3, conn)

data3['QuarterYear'] = data3['CalendarQuarter'].astype(str) + ' Q' + data3['CalendarYear'].astype(str)

fig = px.bar(data3, x='QuarterYear', y='OrderQuantity', labels={'QuarterYear': 'Quarter and Year', 'OrderQuantity': 'Sum of Order Quantity'})
st.plotly_chart(fig)

fig.update_layout(
    title='Order Quantity by Quarter and Year',
    xaxis_title='Quarter and Year',
    yaxis_title='Sum of Order Quantity',
    xaxis_tickangle=-45
)
st.write("Grafik di atas menggambarkan tentang distribusi jumlah kuantitas pesanan dari satu kuartal ke kuartal lainnya dalam rentang dari tahun 2001 hingga 2004. Grafik ini menunjukkan bahwa ada variasi signifikan dalam jumlah kuantitas pesanan dari satu kuartal ke kuartal yang lain. Dapat dilihat pada gambar jika pada setiap kuartal di tahun 2001 dan 2002, jumlah kuantitas pesanan lebih sedikit dibandingkan dengan kuartal pada tahun yang lain. Di kuartal tahun 2003, jumlah kuantitas pesanan mulai meningkat. Hingga puncaknya pada kuartal kedua di tahun 2004, jumlah kuantitas pesanan yang paling tinggi di antara kuartal yang lain. Dan mengalami penurunan di kuartal ketiga pada tahun tersebut. Terdapat beberapa kesamaan di kuartal tertentu. Contohnya pada kuartal kedua di tahun 2003 dan 2004 yang memiliki jumlah pesanan yang sangat tinggi dibanding dengan kuartal yang lain meski di tahun yang berbeda. ")
