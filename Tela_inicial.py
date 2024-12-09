import streamlit as st

st.title ("STUDYHUB")
st.subheader('''
 Bem-vindo ao Study Hub, o seu aliado na educação moderna!!
      ''')
st.write('''O Study Hub é uma plataforma inovadora projetada para facilitar a reserva de salas de aula de maneira rápida, eficiente e acessível.
Seja você um professor, estudante ou instituição de ensino.
''')
image_url = "https://ibb.co/SwWh2hx"



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


image_path = "imgs/tea0.8.png" 


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











