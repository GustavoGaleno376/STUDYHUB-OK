import streamlit as st

if "usu_reserv" not in st.session_state:
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}

if not all(st.session_state["usu_reserv"].values()):
    st.warning("Nenhum cadastro encontrado. Por favor, realize o cadastro antes de acessar seu perfil.")
    st.stop()  # Impede a execução do restante do código

st.title("Meu Perfil")

st.subheader("Suas Informações")
st.write(f"**Nome:** {st.session_state['usu_reserv']['nome']}")
st.write(f"**Email:** {st.session_state['usu_reserv']['email']}")

st.subheader("Atualizar Dados")
novo_nome = st.text_input("Atualize seu Nome:", value=st.session_state["usu_reserv"]["nome"])
novo_email = st.text_input("Atualize seu Email:", value=st.session_state["usu_reserv"]["email"])

if st.button("Salvar Alterações"):
    st.session_state["usu_reserv"]["nome"] = novo_nome
    st.session_state["usu_reserv"]["email"] = novo_email
    st.success("Seus dados foram atualizados com sucesso!")

if st.button("Redefinir Cadastro"):
    st.session_state["usu_reserv"] = {"nome": "", "email": "", "senha": ""}
    st.success("Seu cadastro foi redefinido. Por favor, faça o cadastro novamente.")

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

#imagem
import streamlit as st
import base64

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

image_path = "imgs/meu perfil 0.1.png" 

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

# imagem barra 
st.sidebar.image("imgs/ESTUDIO-removebg-preview.png")
import streamlit as st
