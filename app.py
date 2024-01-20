import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import time
from PIL import Image
from modulos.classes import *
import numpy as np
import pandas as pd
import io


@st.cache_data
def carregaMesas():
    mesas = [
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(6),
        Mesa(6),
        Mesa(6),
        Mesa(8),
    ]
    return mesas


@st.cache_data
def carregaClientes():
    df = pd.read_csv(r"modulos/dados/clientes.csv", index_col=0)

    # Criar instâncias de Cliente a partir das linhas do DataFrame
    clientes = [Cliente(**cliente) for _, cliente in df.iterrows()]

    return clientes


def main():
    mesas = carregaMesas()
    clientes = carregaClientes()

    logo = Image.open(r"img/logo.png")
    col1, col2 = st.columns((1, 4))
    with col1:  # To display brand log
        st.image(logo, width=130)
    with col2:  # To display the header text using css style
        st.markdown(
            """ <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="font">"La Cucina di Marcotti"</p>', unsafe_allow_html=True
        )
        st.write("Cucina Italiana.")

    with st.sidebar:
        opcao = option_menu(
            "Galeria",
            [
                "Salão",
                "Cozinha",
                "Menu",
                "Administrativo",
                "Relatórios",
                "Sobre",
            ],
            icons=[
                "house",
                "egg-fried",
                "book",
                "person lines fill",
                "kanban",
                "question-lg",
            ],
            menu_icon="app-indicator",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "#000"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "#02ab21"},
            },
        )

    def Salao():
        st.subheader("Salão")
        for mesa in mesas:
            if st.button(f"Mesa: {mesa.id} {mesa.status}"):
                with st.form(
                    key="columns_in_form2", clear_on_submit=True
                ):  # set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                    # st.write('Please help us improve!')
                    id_cliente = st.text_input(
                        label="Id Cliente"
                    )  # Collect user feedback
                    submitted = st.form_submit_button("Submit")
                    if submitted:
                        st.write(
                            "Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!"
                        )
                        mesa.inserirCliente()

    def Relatorio():
        # Permite gerar um relatorio a partir do banco de clientes

        df_head = pd.DataFrame([vars(cliente) for cliente in clientes[:30]])
        # cria botao que quando clicado carrega os dados em df_head na tela
        if st.button("Check Results", key="1"):
            st.write(df_head)
        else:
            st.write("---")

        # Allow users to check the results of the third code snippet by clicking the 'Check Results' button
        import io

        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        if st.button("Check Results", key="3"):
            st.text(s)
        else:
            st.write("---")

    def Sobre():
        st.subheader("Sobre o App:")

        st.write(
            "Bem-vindo ao [Nome do App]!\n"
            + "\n"
            + "Desenvolvedor:\n"
            + "Fernando Santos Moreno\n"
            + "\n"
            + "Área de Suporte:\n"
            + "[Email de Suporte]\n"
            + "[Links para Redes Sociais ou Página de Suporte]\n"
            + "\n"
            + "Copyright © 2024\n"
            + "Todos os direitos reservados.\n"
            + "\n"
            + "Versão:\n"
            + "V 1.0.0.2024.1\n"
            + "\n"
            + "Obrigado por escolher Nosso Sistema"
        )

    def Cozinha():
        pass

    if opcao == "Salão":
        Salao()
    elif opcao == "Cozinha":
        Cozinha()
    elif opcao == "Relatórios":
        Relatorio()
    elif opcao == "Sobre":
        Sobre()


main()
