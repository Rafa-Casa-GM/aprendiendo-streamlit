import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
@st.cache
def load_data():
    data = pd.read_csv('Peliculas.csv')
    return data

data = load_data()

# Sidebar - Filtros
st.sidebar.header('Filtros')

title = st.sidebar.text_input('Buscar por título')
genre = st.sidebar.multiselect('Seleccionar género', data['Genre'].unique())
director = st.sidebar.multiselect('Seleccionar director', data['Director'].unique())
year = st.sidebar.slider('Año', int(data['Year'].min()), int(data['Year'].max()))
rating = st.sidebar.slider('Calificación', float(data['Rating'].min()), float(data['Rating'].max()))

# Filtrar datos
filtered_data = data[(data['Title'].str.contains(title)) &
                     (data['Genre'].isin(genre) if genre else True) &
                     (data['Director'].isin(director) if director else True) &
                     (data['Year'] >= year) &
                     (data['Rating'] >= rating)]

# Mostrar datos filtrados
st.write(filtered_data)

# Gráficos
st.header('Gráficos')

# Histograma de Calificaciones
st.subheader('Distribución de Calificaciones')
fig, ax = plt.subplots()
ax.hist(filtered_data['Rating'], bins=20, color='blue', alpha=0.7)
ax.set_xlabel('Calificación')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

# Ingresos por Año
st.subheader('Ingresos por Año')
fig, ax = plt.subplots()
average_revenue_per_year = filtered_data.groupby('Year')['Revenue (Millions)'].mean()
ax.plot(average_revenue_per_year.index, average_revenue_per_year.values, marker='o')
ax.set_xlabel('Año')
ax.set_ylabel('Ingresos Promedio (Millones)')
st.pyplot(fig)

# Ejecutar la aplicación
if __name__ == '__main__':
    st.title('Análisis de Películas')
    st.write('Esta es una aplicación simple para explorar datos de películas.')
