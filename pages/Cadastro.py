import streamlit as st


if "usu_reserv" not in st.session_state:
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}

st.title("Cadastro de Usuário")


nome = st.text_input("Nome:", value=st.session_state["usu_reserv"]["nome"])
email = st.text_input("Email:", value=st.session_state["usu_reserv"]["email"])
senha = st.text_input("Senha:", type="password", value=st.session_state["usu_reserv"]["senha"])

if st.button("Cadastrar"):
    if len(nome) < 4:
        st.warning("O nome deve ter pelo menos 4 caracteres.")
    elif len(email) < 6:
        st.warning("Digite um email válido.")
    elif len(senha) < 7:
        st.warning("A senha deve ter pelo menos 7 caracteres.")
    else:
        
        st.session_state["usu_reserv"] = {"nome": nome, "email": email, "senha": senha}
        st.success(f"Bem-vindo(a), {nome}! Seu cadastro foi realizado com sucesso.")



st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Georgia', serif;
        }
    </style>
""", unsafe_allow_html=True)


def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string


import streamlit as st
import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string


image_path = "imgs/cadastro 0.5.jpg" 


image_base64 = image_to_base64(image_path)


st.markdown(f"""
    <style>
        .stApp{{
            background-image: url('data:image/jpeg;base64,{image_base64}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh;  /* Garante que o fundo ocupe toda a tela */
            margin: 0;
        }}
    </style>
""", unsafe_allow_html=True)


st.sidebar.image("imgs/ESTUDIO-removebg-preview.png")
import streamlit as st
import streamlit as st

import streamlit as st


