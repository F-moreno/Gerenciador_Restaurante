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
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(4),
        Mesa(6),
        Mesa(6),
        Mesa(6),
        Mesa(6),
        Mesa(6),
        Mesa(6),
        Mesa(8),
        Mesa(8),
        Mesa(8),
        Mesa(8),
    ]
    return mesas


@st.cache_data
def carregaClientes():
    df = pd.read_csv("modulos/dados/clientes.csv")
    
    # Criar instâncias de Cliente a partir das linhas do DataFrame
    #clientes = [Cliente(**cliente) for _, cliente in df.iterrows()]

    return df

@st.cache_data
def carregaReservas():
    df = pd.read_csv(r"modulos/dados/reservas.csv")

    # Criar instâncias de Cliente a partir das linhas do DataFrame
    #reservas = [Reserva(**reserva) for _, reserva in df.iterrows()]

    return df

def main():
    mesas = carregaMesas()
    clientes = carregaClientes()
    reservas= carregaReservas()

    logo = Image.open(r"modulos/img/logo.png")
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
                    key=f"form_mesa_{mesa.id}", clear_on_submit=True
                ):  # set clear_on_submit=True so that the form will be reset/cleared once it's submitted
                    # st.write('Please help us improve!')
                    id_cliente = st.text_input(label="Id Cliente", key=f"id_cliente_{mesa.id}")  # Collect user feedback
                    submitted = st.form_submit_button("Inserir Cliente")
                    if submitted:
                        mesa.inserirCliente(id_cliente)
                        st.success(f"Cliente {id_cliente} inserido na Mesa {mesa.id}")

    def Relatorio():
        # Permite gerar um relatorio a partir do banco de clientes

    
        # cria botao que quando clicado carrega os dados em df_head na tela
        if st.button("Clientes", key="1"):
            st.write(clientes)
            select=clientes
        else:
            st.write("---")

        #Gera relatorio de reservas a partir do banco de reservas
        #df_reservas = pd.DataFrame([vars(reserva) for reserva in reservas[:999]])
        if st.button("Reservas", key="2"):

            top3=reservas['IdCliente'].value_counts().head(3)
            top3_clientes = clientes[clientes['Id'].isin(top3)]
            contagem_reservas = reservas[reservas['IdCliente'].isin(top3)]['IdCliente'].value_counts()

            # Juntando os DataFrames usando merge e ajustando o índice
            resultado = pd.merge(top3_clientes, contagem_reservas, how='left', left_on='Id', right_index=True)



            # Mostrando o resultado
            st.write(resultado)
            select=reservas

        else:
            st.write("---")
        # Allow users to check the results of the third code snippet by clicking the 'Check Results' button
        import io

        buffer = io.StringIO()
        select.info(buf=buffer)
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
