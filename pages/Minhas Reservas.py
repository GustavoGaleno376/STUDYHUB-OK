import streamlit as st
import datetime

if "reservations" not in st.session_state:
    st.session_state.reservations = []

if "usu_reserv" not in st.session_state or not st.session_state.usu_reserv.get("nome"):
    st.warning("Você precisa se cadastrar antes de acessar as reservas.")
    st.stop()

def show_room_photo(room_name):
    room_photos = {
        "Auditório": "https://midias.agoravalejaguaribe.com.br/599d8830f02da605fa693e3460ce6ee3.jpg",  # Substitua com o URL da foto real
        "Laboratório": "https://www.univates.br/eventos//media/alugue/laboratorios_informatica/labinfo_02.jpg",
        "Biblioteca": "https://www.unoeste.br/Content/Imagens/Biblioteca/U5/2023/ja1.jpg",
        "Sala ds1": "https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3048663:1613606521/sala-de-aula.jpg?f=16x9&$p$f=a0b6e86",
        "Sala sist1": "https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3048663:1613606521/sala-de-aula.jpg?f=16x9&$p$f=a0b6e86",
        "Sala agn1": "https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3048663:1613606521/sala-de-aula.jpg?f=16x9&$p$f=a0b6e86",
        "Sala adm1": "https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3048663:1613606521/sala-de-aula.jpg?f=16x9&$p$f=a0b6e86",
    }
    return room_photos.get(room_name, "")

page = st.sidebar.selectbox("Escolha uma página", ["Fazer Reserva", "Minhas Reservas"])

if page == "Fazer Reserva":
    st.title("Controle de Reservas")
    st.write(f"Bem-vindo(a), {st.session_state.usu_reserv['nome']}!")

    available_rooms = [
        "Auditório",
        "Laboratório",
        "Biblioteca",
        "Sala ds1",
        "Sala sist1",
        "Sala agn1",
        "Sala adm1",
    ]

    if st.session_state.reservations:
        st.subheader("Reservas Feitas:")
        for res in st.session_state.reservations:
            st.write(
                f"Sala: {res['room']} - Data: {res['date']} - Horário: {res['time']} - Motivo: {res['reason']}"
            )
    else:
        st.write("Nenhuma reserva feita ainda.")

    st.subheader("Nova Reserva")
    room = st.selectbox("Escolha uma sala", available_rooms)
    date = st.date_input("Escolha a data", min_value=datetime.date.today())
    motivo = st.text_input("Diga o motivo")
    time_input = st.text_input("Digite o horário (formato HH:MM)", "09:00")

    try:
        time = datetime.datetime.strptime(time_input, "%H:%M").time()
    except ValueError:
        st.warning("Formato de hora inválido! Utilize o formato HH:MM (ex: 14:30).")
        time = None

    if st.button("Reservar"):
        if time:
            reservation_exists = any(
                res["room"] == room and res["date"] == str(date) and res["time"] == str(time)
                for res in st.session_state.reservations
            )

            if reservation_exists:
                st.warning("Esta sala já está reservada nesse horário.")
            else:
                st.session_state.reservations.append(
                    {"room": room, "date": str(date), "time": str(time), "reason": motivo}
                )
                st.success(f"Sala {room} reservada para {date} às {time}. Motivo: {motivo}")
        else:
            st.warning("Por favor, insira uma hora válida.")

elif page == "Minhas Reservas":
    st.title("Minhas Reservas")

    if st.session_state.reservations:
        st.subheader("Reservas Feitas:")
        for res in st.session_state.reservations:
            room_photo = show_room_photo(res['room'])
            st.write(f"Sala: {res['room']} - Data: {res['date']} - Hora: {res['time']} - Motivo: {res['reason']}")
            if room_photo:
                st.image(room_photo, caption=res['room'], use_container_width=True)
    else:
        st.write("Nenhuma reserva feita ainda.")

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

image_path = "imgs/minhas reservas 0.2.png" 

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