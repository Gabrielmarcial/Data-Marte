# importando as bibliotecas
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image

# Adicionando um titulo
st.title('Construindo Relatórios para Data Science com Streamlit')

# importando conjunto de dados
train = pd.read_csv(' ') # '' --> caminho para o arquivo com os dados  

# Utilizando Markdown
st.markdown('---')
st.markdown('# Sobre a Base de Dados')
st.markdown('''O naufrágio do titanic aconteceu em 15 de abril de 1992 no atlântico norte colidindo com um iceberg.

Quatro dias depois de sua viagem inaugural, o considerado ‘inafundável’ navio deixou 1502 mortos dos 2224 passageiros e tripulantes.

Mesmo com um fator sorte envolvido no desastre parece que alguns grupos tiveram mais chances que outros de sobrevivência.

Vamos trabalhar com A base de dados : 

conjunto de treinamento (train.csv)


__*Dicionário dos dados*__
- PassengerId (Número de identificação dos passageiros)
- survival (Sobrevivencia, 0 = não e 1 = sim)
- pclass (Classe de ingresso, 1 = 1° 2 = 2° 3 = 3° )
- Name (Nome do passageiro)
- sex (Sexo do passageiro)
- Age (Idade)
- sibsp ( irmãos / cônjuges a bordo do Titanic)
- parch (de pais / filhos a bordo do Titanic)
- ticket (Número do bilhete)
- fare (Tarifa de passageiro)
- cabin (Número da cabine)
- embarked (Porto de embarcação , C = Cherbourg, Q = Queenstown, S = Southampton)''')
st.markdown('---')

# Visualizando os dados
st.markdown('### __Base de dados:  Desastre Titanic__ ')
st.dataframe(train)

st.markdown('---')


# Visualização Gráfica
st.title('Visualização Gráfica')
# Valores ausentes
fig = px.bar(x = [0,0,0,0,0,177,0,0,0,0,687,2],
            y = ['PassengerId','Survived','Pclass','Name' ,
     'Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'],
            orientation='h', title=" Valores faltantes ",
             labels={'x':'Quantidade','y':'Dados'})
st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

#Tipos de variaveis

fig = px.bar(x = [6,5],
            y = ['Categóricas','Numéricas'],
            orientation='h', title=" Tipos de dados ",
             labels={'x':'Quantidade','y':'Variaves'},width=800, height=400)
st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

# Grafico de correlção
fig, ax = plt.subplots(figsize=(5, 5))
sns.heatmap(train.corr(), annot=True, cmap='Blues')
ax.set_title('Correlação dos dados')
fig.tight_layout()
st.pyplot(fig)


# Sobreviventes

fig = px.bar(x = ['Sobreviveu (1)' , 'Não Sobreviveu (0)'], y = [342,549],
            title=" Sobreviventes ",labels={'y':'Quantidade','x':'Dado'})
st.plotly_chart(fig, use_container_width=False, sharing='streamlit')


#Utilizaçõa de colunas

# Grafico do Sexo dos Passageiros
col1, col2 = st.beta_columns(2)
with col1 :
    fig = px.histogram(train, x="Sex", nbins=50, title='Sexo dos Passageiros', labels={"Sex": 'Sexo'},width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
with col2 :
    fig = px.bar(train, x="Sex", y="Survived", color="Sex", title=" Sobreviventes x Sexo ",
                 labels={'Sex': 'Sexo', 'Survived': 'Sobreviventes'},width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

# Grafico Da Classe dos Passageiros

col1, col2 = st.beta_columns(2)
with col1 :
    fig = px.histogram(train, x="Pclass", nbins=10, title='Classe dos Passageiros',
                       labels={"Pclass": 'Classe', 'count': 'Quantidade por Classe'},width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

with col2 :
    fig = px.bar(train, x="Pclass", y="Survived", color="Pclass", title="Sobreviventes x Classe",
                 labels={"Pclass": 'Classe do Passageiro', 'Survived': 'Sobreviventes'},width=400, height=400)
    st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

# Grafico da Idade dos Passageiros
fig = px.histogram(train, x="Age", nbins=200, title='Idade dos Passageiros',
                   labels={'Age': 'Idade'})
st.plotly_chart(fig, use_container_width=False, sharing='streamlit')


#Referencias e adicionando sidebar

# adicionando uma imagem
image = Image.open('cropped-logo_datamarte-2-1024x534.jpg')
st.sidebar.image(image, caption='DataMarte2020',use_column_width=True)

# Blog
st.sidebar.markdown('Feito por : Gabriel Marcial')

st.sidebar.markdown("Redes Sociais :")
st.sidebar.markdown("- [Linkedin](https://www.linkedin.com/in/gabriel-marcial-6ba93a1a1/)")
st.sidebar.markdown("- [Blog: Data Marte](https://datamarte.com/)")
st.sidebar.markdown("- [Github](https://github.com/Gabrielmarcial)")

