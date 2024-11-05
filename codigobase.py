# -*- coding: utf-8 -*-
"""codigoBase.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TtdFpwwT8ZhLHl0lFVYNoJKIuDXiZ-OJ
"""

#!pip install streamlit

import pandas as pd
import plotly.express as px
import streamlit as st

# DATASET COVID 19 BRASIL
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# Traduzindo o nome das colunas da tabela para portugues
df = df.rename(columns={'newDeaths':'Novos óbitos', 'newCases':'Novos casos', 'deaths':'Total óbitos', 'deaths_per_100k_inhabitants':'Obitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants':'Total de casos por 100 mil habitantes'})

# Selecinar o Estado
estados = list(df.state.unique())
state = st.sidebar.selectbox('Qual Estado', estados)


# column = 'Total de casos por 100 mil habitantes'
colunas = ['Novos óbitos', 'Novos casos', 'Total óbitos', 'Obitos por 100 mil habitantes', 'Total de casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação', colunas)


df = df[df.state == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5, 'y':0.9, 'xanchor':'center', 'yanchor':'top'})

st.title("DADOS COVID  - BRASIL")
st.write('Nesta aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem')

st.plotly_chart(fig, use_container_width=True)

st.caption("Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br")
