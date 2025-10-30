import streamlit as st
from PIL import Image

# ===== CONFIGURACIÓN GENERAL =====
st.set_page_config(
    page_title="Bae - App Multimodal",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== ESTILOS PERSONALIZADOS (IDENTIDAD VISUAL BAE) =====
st.markdown("""
    <style>
    /* Fondo general */
    body {
        background-color: #FFF8EA;
        color: #333333;
        font-family: 'Poppins', sans-serif;
    }

    /* Encabezados */
    h1 {
        color: #DD8E6B;
        text-align: center;
        font-weight: 800;
    }

    h2, h3, h4 {
        color: #C06C84;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #FFF2C3;
        color: #333333;
        padding: 20px;
    }

    /* Botones */
    div.stButton > button:first-child {
        background-color: #DD8E6B;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s;
    }

    div.stButton > button:first-child:hover {
        background-color: #C06C84;
        color: white;
    }

    /* Selectbox, radio y checkbox */
    .stSelectbox, .stRadio, .stCheckbox {
        background-color: #FFF2C3;
        border-radius: 10px;
        padding: 5px;
    }

    /* Inputs */
    .stTextInput > div > div > input {
        background-color: #FFFFFF;
        border: 1px solid #DD8E6B;
        border-radius: 10px;
        padding: 8px;
    }

    /* Imagen */
    img {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ===== CONTENIDO PRINCIPAL =====
st.title("🌸 Portafolio BAE - Interfaces Multimodales")

st.header("Explora cómo la inteligencia emocional y la tecnología se unen para crear experiencias humanas.")
st.write("Aquí comenzamos a desarrollar aplicaciones que integran backend y frontend con un enfoque centrado en el bienestar del usuario — en este caso, del bebé y su entorno.")

# Imagen principal
image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Diseño de interfaces multimodales', use_container_width=True)

# Entrada de texto
texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

# ===== COLUMNAS =====
st.subheader("Explora los diferentes modos de interacción")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌼 Primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia del usuario al integrar varios sentidos.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('¡Correcto! 🌟')

with col2:
    st.subheader("🎧 Segunda columna")
    modo = st.radio("¿Qué modalidad predomina en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.info('La vista guía gran parte de la experiencia del usuario.')
    elif modo == 'Auditiva':
        st.info('El sonido crea cercanía y confianza en la interacción.')
    elif modo == 'Táctil':
        st.info('El tacto aporta sensibilidad y naturalidad a la experiencia.')

# ===== BOTONES =====
st.subheader("Interacción con botones")
if st.button('Presiona el botón'):
    st.success('¡Gracias por presionar! 💕')
else:
    st.write('Aún no has presionado el botón.')

# ===== SELECTBOX =====
st.subheader("Selecciona la modalidad")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico"),
)
if in_mod == "Audio":
    set_mod = "Reproducir audio"
elif in_mod == "Visual":
    set_mod = "Reproducir video"
elif in_mod == "Háptico":
    set_mod = "Activar vibración"
st.write("La acción seleccionada es:", set_mod)

# ===== SIDEBAR =====
with st.sidebar:
    st.image("logo_bae.png", width=150)
    st.subheader("Configuración de modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )
    st.markdown("---")
    st.write("🍼 **Bae** — Tecnología para cuidar y entender mejor el desarrollo de los bebés.")

