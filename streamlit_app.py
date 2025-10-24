import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title('Gestão da Aprendizagem - Bahia')
st.write('App Streamlit')

# Dataframe

# Cabeçalho
st.set_page_config(page_title="App Streamlit", layout="wide")

st.title("📊 GA - Bahia")
st.write("👨‍💻 Autor: **Marllon Gama Quintaes**")
st.write("🎯 Tema: **Análise dos dados da Gestão da Aprendizagem da Secretaria de Educação do Estado da Bahia - Núcleo Territorial Educacional 2, Velho Chico**")

# Estrutura de seções
menu = st.sidebar.radio("📂 Seções", ["Introdução", "Visualizar Dados", "Gráficos"])

# Introdução
if menu == "Introdução":
    with st.container():
        st.header("📖 Introdução")
        st.write("""
    Os dados aqui apresentados são relacionados a proficiencia dos estudantes da rede estadual da Bahia.
        """)
        st.info("Você pode navegar pelas seções usando o menu lateral à esquerda.")

# Dados
elif menu == "Visualizar Dados":
    st.header("📂 Visualização e Estatísticas dos Dados")

    # Leitura do dataset
    df = pd.read_excel("GA_BA_NTE02.xlsx")

    # Exibir primeiras linhas
    st.subheader("🔹 Pré-visualização dos Dados")
    st.dataframe(df.head())

    # Estatísticas descritivas
    st.subheader("📊 Estatísticas Descritivas")
    st.dataframe(df.describe())

    # Mostrar informações básicas
    st.subheader("🧮 Informações Gerais")
    st.write(f"Número de estudantes linhas: {df.shape[0]}")
    st.write("Colunas disponíveis:", list(df.columns))

# Gráficos
elif menu == "Gráficos":
    st.header("📊 Visualizações Gráficas")
    df = pd.read_excel("GA_BA_NTE02.xlsx")

    # Gráfico 1: 
    with st.expander("📍 1a Avaliação - Nota média em Linguagens por Modalidade"):
        avg_pt1 = df.groupby("modalidade")["prof_1av_linguagens"].mean().sort_values()
        st.bar_chart(avg_pt1)
    
    with st.expander("📍 2a Avaliação - Nota média em Linguagens por Modalidade"):
        avg_pt2 = df.groupby("modalidade")["prof_2av_linguagens"].mean().sort_values()
        st.bar_chart(avg_pt2)

    with st.expander("📍 1a Avaliação - Nota média em Matemática por Modalidade"):
        avg_mt1 = df.groupby("modalidade")["prof_1av_matemática"].mean().sort_values()
        st.bar_chart(avg_mt1)
    
    with st.expander("📍 2a Avaliação - Nota média em Matemática por Modalidade"):
        avg_mt2 = df.groupby("modalidade")["prof_2av_matemática"].mean().sort_values()
        st.bar_chart(avg_mt2)

    # Calcular médias por modalidade
    df_medias = df.groupby("modalidade")[[
        "prof_1av_linguagens", "prof_2av_linguagens",
        "prof_1av_matemática", "prof_2av_matemática"
    ]].mean().reset_index()

    # Transformar para formato longo
    df_long = df_medias.melt(id_vars="modalidade",
                            var_name="Avaliacao_Disciplina",
                            value_name="Nota Média")

    # Separar avaliação e disciplina
    df_long[["Avaliacao", "Disciplina"]] = df_long["Avaliacao_Disciplina"].str.extract(r"(1av|2av)_(.*)")
    df_long["Avaliacao"] = df_long["Avaliacao"].map({"1av": "1ª Avaliação", "2av": "2ª Avaliação"})
    df_long["Disciplina"] = df_long["Disciplina"].str.replace("_", " ").str.capitalize()

    # Criar uma coluna combinada (Disciplina + Avaliação)
    df_long["Legenda"] = df_long["Disciplina"] + " - " + df_long["Avaliacao"]

    # Gráfico
    with st.expander("📊 Média de Proficiência por Modalidade e Avaliação"):
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(
            data=df_long,
            x="modalidade",
            y="Nota Média",
            hue="Legenda",
            palette="viridis",
            ci=None
        )

        # Adicionar rótulos nas barras
        for p in ax.patches:
            ax.text(
                p.get_x() + p.get_width() / 2,
                p.get_height() + 0.5,
                f"{p.get_height():.1f}",
                ha="center",
                va="bottom",
                fontsize=9
            )

        plt.title("Média de Proficiência por Modalidade (Linguagens e Matemática - 1ª e 2ª Avaliação)")
        plt.xlabel("Modalidade")
        plt.ylabel("Nota Média")
        plt.xticks(rotation=45)
        plt.legend(title="Disciplina e Avaliação")
        st.pyplot(plt)

# Rodapé
st.markdown("---")
st.caption("MVP - Etapa 3 | Streamlit + Pandas | Prof. Maxwell Monteiro | Autor: Marllon Gama")