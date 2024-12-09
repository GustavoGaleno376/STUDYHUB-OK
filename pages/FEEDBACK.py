import streamlit as st


if "feedbacks" not in st.session_state:
    st.session_state.feedbacks = []


def show_feedbacks():
    if st.session_state.feedbacks:
        st.subheader("Feedbacks Anteriores:")
        for feedback in st.session_state.feedbacks:
            st.write(f"Classificação: {feedback['rating']} estrelas")
            st.write(f"Comentários: {feedback['comments']}")
            st.write(f"Data: {feedback['date']}")
            st.write("---")
    else:
        st.write("Nenhum feedback registrado ainda.")

st.title("Deixe seu Feedback")


show_feedbacks()


st.subheader("Novo Feedback")


rating = st.slider("Qual sua classificação para o sistema?", 1, 5, 3)


comments = st.text_area("Deixe seu comentário sobre o sistema")


from datetime import date
today = date.today()
feedback_date = today.strftime("%d/%m/%Y")


if st.button("Enviar Feedback"):
    if comments:
        
        st.session_state.feedbacks.append({"rating": rating, "comments": comments, "date": feedback_date})
        st.success("Obrigado pelo seu feedback!")
        
        st.experimental_rerun()
    else:
        st.warning("Por favor, insira um comentário.")


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


image_path = "imgs/Design sem nome (1).jpg" 


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