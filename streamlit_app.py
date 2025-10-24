import streamlit as st

# Title
st.title('Gestão da Aprendizagem - Bahia')
st.write('App Streamlit')

# Dataframe

# Cabeçalho
st.set_page_config(page_title="App Streamlit", layout="wide")

st.title("📊 GA - Bahia")
st.write("👨‍💻 Autor: **Marllon Gama Quintaes**")
st.write("🎯 Tema: **Análise dos dados da Gestão da Aprendizagem da Secretaria de Educação do Estado da Bahia**")

# Estrutura de seções
menu = st.sidebar.radio("📂 Seções", ["Introdução", "Carregar Planilha", "Visualizar Dados", "Gráficos", "Conclusões"])

# Introdução
if menu == "Introdução":
    with st.container():
        st.header("📖 Introdução")
        st.write("""
    Os dados aqui apresentados são relacionados a proficiencia dos estudantes da rede estadual da Bahia.
        """)
        st.info("Você pode navegar pelas seções usando o menu lateral à esquerda.")

# Dados
elif menu == "Dados":
    st.header("📂 Visualização e Estatísticas dos Dados")

    # Leitura do dataset
    df = pd.read_csv("base_indicadores_2025_v4.csv")

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
    df = pd.read_csv("base_indicadores_2025_v4.csv")

    # Gráfico 1: Custo médio por região
    with st.expander("📍 Gráfico 1 - Custo médio por região"):
        avg_charges = df.groupby("region")["charges"].mean().sort_values()
        st.bar_chart(avg_charges)

    # Gráfico 2: Dispersão - idade x custo
    with st.expander("📈 Gráfico 2 - Dispersão entre Idade e Custo do Seguro"):
        fig, ax = plt.subplots()
        ax.scatter(df["age"], df["charges"], alpha=0.6)
        ax.set_xlabel("Idade")
        ax.set_ylabel("Custo do Seguro (charges)")
        ax.set_title("Dispersão: Idade x Custo do Seguro")
        st.pyplot(fig)

# Conclusões
elif menu == "Conclusões":
    st.header("📝 Conclusões")
    st.write("""
    - Há uma **tendência de aumento no custo do seguro** com a idade e com o hábito de fumar.  
    - As regiões apresentam **variações médias de custo**, possivelmente ligadas a fatores socioeconômicos.  
    - Este MVP cumpre os requisitos da **Etapa 3**, incluindo tabela descritiva e visualizações gráficas.
    """)
    st.success("✅ MVP completo e funcional!")

# Rodapé
st.markdown("---")
st.caption("MVP - Etapa 3 | Streamlit + Pandas | Prof. Maxwell Monteiro | Autor: Marllon Gama")