import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import plotly.express as px

# HEAD
# Title
st.set_page_config(
    page_title="IMDB Dashboard",
    page_icon="📽️",
    layout="wide")
    # initial_sidebar_state="expanded"

# VISUALIZATION IMDB DATA

st.title("Data Visualization of IMDB Data")

# Read CSV files into dataframe
try:
    # global df
    df = pd.read_excel('imdb_data_combined.xlsx')

except pd.errors.ParserError as e:
    st.error(f"Error reading the file: {e}")


df['Rate'] = df['Rate'].astype(float)

# SIDEBAR
with st.sidebar:
    st.title('📽️ *IMDB Dashboard*')

    selected_ratio = st.selectbox('Select a aspect ratio', df['Aspect_Ratio'].unique())

    st.markdown("#### Adventureworks Dashboard")
    st.write("[Click here to the link](https://sifodavis-21082010120-adventureworks.streamlit.app/)")
    st.markdown("#### GitHub Link")
    st.write("[Click here to the link](https://github.com/kharistya281/FPDAVIS-21082010120.git)")


    st.write("Nama : Kharisma Agustya Zahra Salsabilla")
    st.write("NPM  : 21082010120")
    st.write("Matkul : Data Visualisasi Par A")
    


# =================================================
# Dashboard Main Panel 
col = st.columns((0.3, 0.7), gap='small')

with col[0]:
    st.markdown("#### General Information")
    
    # total budget
    total_budget = df[df['Aspect_Ratio'] == selected_ratio]['Budget'].sum()
    st.metric(label='Total Budget', value=f"$ {total_budget}")

    # total gross US 
    total_grossUS = df[df['Aspect_Ratio'] == selected_ratio]['Gross_Us'].sum()
    st.metric(label='Total Gross US', value=f"$ {total_grossUS}")

    # total gross world 
    total_grossWorld = df[df['Aspect_Ratio'] == selected_ratio]['Gross_World'].sum()
    st.metric(label='Total Gross World', value=f"$ {total_grossWorld}")

    st.write("Berisi informasi umum mengenai total budget, pendapatan kotor baik di Amerika Serikat maupun secara global berdasarkan aspect ratio yang digunakan pada film.")

with col[1]:
    # COMPARASION CHART 
    # bar chart (rating, )
    st.markdown("#### Total Budget and Gross World by Movie Rating")
    st.write("*COMPARISON CHART - BAR CHART*")
    df_sel = df[['Rating', 'Budget', 'Gross_World']].sort_values(by=['Rating'])

    hsl1 = df_sel.loc[(df_sel[['Budget', 'Gross_World']] != 0).all(axis=1)]

    chart_data = pd.DataFrame(
        {
            "Rating": hsl1['Rating'],
            "Budget": hsl1['Budget'],
            "Gross World": hsl1['Gross_World']
        }
    )

    st.bar_chart(
        chart_data, x="Rating", y=["Budget", "Gross World"]
    )
    st.write("""
Grafik di atas menunjukkan perbandingan jumlah budget dan pendapatan kotor global dari dari berbagai film berdasarkan rating film tersebut. Dari semua rating film, rating “PG-13” memiliki budget dan pendapatan kotor global tertinggi dibanding dengan rating yang lain. Film dengan rating “PG-13” paling banyak diminati karena mencakup audiens yang luas karena film dengan rating tersebut cocok untuk penonton usia 13 tahun keatas. Artinya film tersebut dapat menarik remaja, orang dewasa muda, bahkan orang dewasa yang lebih tua. Banyak film populer dengan berbagai genre dengan rating tersebut.  
""")
    st.write("""
Film dengan rating “G” memiliki budget dan pendapatan kotor global yang relatif rendah. Film dengan rating “R” berada di urutan kedua dengan jumlah budget dan pendapatan kotor global tertinggi setelah rating “PG-13”. Perbandingan antara anggaran.
""")

    # RELATION CHART 
    st.markdown("#### Relationship Between Gross US and Gross World by Movie Rating")
    st.write("*RELATIONSHIP CHART - SCATTER PLOT*")
    df_scatter = df[['Gross_Us', 'Gross_World', 'Rating']].sort_values(by=['Rating'])

    hsl_scat = df_scatter.loc[(df_scatter[['Gross_Us', 'Gross_World']] != 0).all(axis=1)]

    chart_scatter = pd.DataFrame(hsl_scat, columns=['Gross_Us', 'Gross_World', 'Rating'])

    st.scatter_chart(
        chart_scatter,
        x='Rating',
        y=['Gross_Us', 'Gross_World']
    )
    st.write("Grafik di atas menunjukkan hubungan antara rating film dengan pendapatan kotor di Amerika Serikat dan pendapatan kotor global. Rating “PG-13” dan “R” memiliki lebih banyak titik persebaran data, hal ini menunjukkan banyak film dengan rating tersebut. Hal ini menunjukkan variasi yang lebih besar dalam pendapatan kotor di kedua kategori tersebut. Beberapa film dengan rating “G” dan “PG” memiliki pendapatan yang sangat tinggi, baik di Amerika maupun global. Film dengan rating “PG-13” dan “R” menunjukkan perbedaan yang lebih besar dalam pendapatan kotor di kedua kategori ini.  Film dengan rating “Approved” dan “Not Rated” memiliki lebih sedikit data dan tampaknya menghasilkan pendapatan yang lebih rendah secara keseluruhan. ")



    # COMPOSITION CHART 
    # pie chart (rate sama total rated)
    st.markdown("#### Movie Rate Percentage Based on Total Giver Rate")
    st.write("*COMPOSITION CHART - DONUT CHART*")
    df_pie = df[['Rate','TotalRate']].sort_values(by=['Rate'])

    hsl = df_pie.groupby('Rate').sum()

    fig, ax = plt.subplots(figsize=(10,7))
    ax.pie(hsl['TotalRate'], labels=hsl.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    st.pyplot(fig)
    st.write("Grafik di atas menunjukkan persentase nilai film dengan jumlah rate yang diberikan oleh reviewer. Film dengan nilai 8,5 menjadi yang paling tinggi dengan persentase 25,2%, seperempat lebih sedikit dari total keseluruhan. Orang-orang memberikan nilai paling banyak di angka 8,5 karena nilai tersebut dianggap sebagai standar pemberian nilai yang sangat bagus bagi banyak orang. Nilai 8,5 dianggap menjadi titik tengah yang nyaman bagi banyak penonton yang ingin memberikan nilai tinggi untuk film yang mereka nikmati tanpa merasa terlalu berlebihan.")
    st.write("Disusul oleh film dengan nilai 8,6 dengan persentase 20,2%. Paling banyak nilai film yang diberikan di kisaran angka 8 dibandingkan dengan nilai 9. Nilai film paling rendah yakni 9,3 dengan persentase 4,5% dari total keseluruhan.")

    # DISTRIBUTION CHART 
    st.markdown("#### Distribution of Budget, Gross US and Gross World by Movie Release Year")
    st.write("*DISTRIBUTION CHART - LINE CHART*")
    df_line = df[['Gross_Us', 'Budget', 'Gross_World', 'Year']].sort_values(by=['Year'])

    hslLine = df_line.loc[(df_line[['Gross_Us', 'Budget', 'Gross_World']] != 0).all(axis=1)]

    chartLine = pd.DataFrame(hslLine, columns=['Gross_Us', 'Budget', 'Gross_World', 'Year'])

    st.line_chart(
        chartLine,
        x='Year',
        y=['Gross_Us', 'Budget', 'Gross_World']
    )
    st.write("Grafik di atas menunjukkan distribusi pendapatan kotor baik di Amerika Serikat maupun global dan anggaran dengan tahun rilis film. Grafik tersebut memberikan gambaran pertumbuhan dan perkembangan industri film dari tahun 1930 hingga 2024 saat ini. Di periode awal sekitar tahun 1930 hingga 1960. Pada periode ini, baik budget, pendapatan kotor di Amerika Serikat maupun pendapatan kotor global relatif rendah dan stabil dengan sedikit variasi. Pada periode pertengahan sekitar tahun 1960 hingga 1990. Mulai terlihat peningkatan dari budget dan pendapatan kotor, terutama di tahun 1970-an. ")
    st.write("Di periode modern sekitar tahun 1990 hingga 2020, menunjukkan fluktuasi yang lebih besar pada budget dan pendapatan kotor. Banyak lonjakan besar yang menunjukkan film dengan budget tinggi dan pendapatan kotor yang tinggi baik di Amerika Serikat maupun secara global. Periode terkini sekitar tahun 2020 hingga 202 saat ini, meskipun data pada periode ini belum sepenuhnya terisi. Terlihat tren yang konsisten dalam budget dan pendapatan kotor, yang menunjukkan pertumbuhan industri film. ")



