import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Portal IA - UC", layout="wide", page_icon="🏛️")

# --- 2. ESTILO VISUAL CORREGIDO ---
st.markdown("""
<style>
    /* 1. Fondo y Texto General (OSCURO para que se lea) */
    .stApp {
        background-color: #f8f9fa;
        color: #333333; /* Gris oscuro */
    }
    
    /* Asegurar que los párrafos del cuerpo sean oscuros */
    .stApp p, .stMarkdown p {
        color: #333333 !important;
    }

    /* 2. Barra Lateral (AZUL con texto BLANCO) */
    section[data-testid="stSidebar"] {
        background-color: #002469;
    }
    /* Todo el texto dentro de la barra lateral será blanco */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* 3. Títulos (Azul UC) */
    h1, h2, h3 {
        color: #002469 !important;
    }

    /* 4. Tarjetas (Fondo blanco, texto oscuro) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ddd;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Caja de Contacto */
    .contacto-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #002469;
        color: #002469 !important;
    }
    .contacto-box h4 {
        color: #002469 !important;
        margin: 0;
    }
    .contacto-box a {
        color: #002469 !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. BARRA LATERAL ---
with st.sidebar:
    # Carga de Logo
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    elif os.path.exists("logo.jpg"):
        st.image("logo.jpg", use_container_width=True)
    else:
        st.warning("⚠️ Falta 'logo.png'")

    st.write("---")
    st.header("📌 Menú")
    opcion = st.radio("Navegación:", ["🏠 Inicio", "🚀 Catálogo de IAs", "📚 Guía y Soporte"])
    st.write("---")
    
    # CONTACTO 
    st.subheader("📞 Contacto")
    st.markdown("**Alonso Meneses**")
    st.caption("📧 armenesesz@uc.cl")
    st.write("---")
    st.info("Dirección de Personas UC")

# --- 4. CONTENIDO PRINCIPAL ---

# === INICIO ===
if opcion == "🏠 Inicio":
    st.title("🏛️ Portal de Inteligencia Artificial")
    
    # BANNER CENTRADO
    col_izq, col_centro, col_der = st.columns([1, 2, 1])
    with col_centro:
        if os.path.exists("banner.jpg"):
            st.image("banner.jpg", width=500)
        elif os.path.exists("banner.png"):
            st.image("banner.png", width=500)
        else:
            st.info("🖼️ Falta 'banner.jpg'")

    # INSTRUCCIONES
    st.markdown("---")
    st.markdown("""
    ### 👋 Bienvenido/a
    Esta plataforma centraliza las herramientas de IA para la comunidad UC.
    
    👉 **¿QUÉ DEBO HACER?**
    1. Ve al menú azul de la izquierda.
    2. Selecciona **"🚀 Catálogo de IAs"**.
    3. Elige la herramienta que necesites.
    """)
    
    # Métricas
    c1, c2, c3 = st.columns(3)
    c1.metric("Herramientas", "7 IAs", "Activas")
    c2.metric("Usuarios", "Comunidad UC", "Libre")
    c3.metric("Soporte", "24/7", "Online")
    
    st.markdown("---")
    st.warning("⚠️ **Recuerda:** No subas datos confidenciales (RUT, Fichas) a estas plataformas.")

# === CATÁLOGO ===
elif opcion == "🚀 Catálogo de IAs":
    st.title("🚀 Bibliotecas de IA")
    st.write("Selecciona una herramienta para abrirla:")
    
    # FILA 1
    st.subheader("📝 Redacción y Análisis")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/Microsoft_365_Copilot_Icon.svg", width=50)
            st.subheader("Copilot")
            st.write("Tu experto en **Excel y Office**. Analiza datos y redacta correos.")
            st.markdown("[🔗 **Abrir Copilot**](https://copilot.microsoft.com)")

    with c2:
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg", width=50)
            st.subheader("ChatGPT")
            st.write("Creatividad, traducciones y borradores rápidos.")
            st.markdown("[🔗 **Abrir ChatGPT**](https://chat.openai.com)")

    with c3:
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg", width=50)
            st.subheader("Gemini")
            st.write("Lógica avanzada, lectura de imágenes y planificación.")
            st.markdown("[🔗 **Abrir Gemini**](https://gemini.google.com)")

    # FILA 2
    st.subheader("🎨 Visual y Datos")
    c4, c5, c6 = st.columns(3)

    with c4:
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/10329/10329267.png", width=50)
            st.subheader("Remini")
            st.write("Restaura fotos antiguas o borrosas de la universidad.")
            st.markdown("[🔗 **Abrir Remini**](https://remini.ai)")
            
    with c5:
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/3209/3209265.png", width=50)
            st.subheader("Gamma")
            st.write("Crea presentaciones (PPT) automáticas con un título.")
            st.markdown("[🔗 **Abrir Gamma**](https://gamma.app)")

    with c6:
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/2800/2800300.png", width=50)
            st.subheader("Julius AI")
            st.write("Analista de datos. Sube Excel y pide gráficos.")
            st.markdown("[🔗 **Abrir Julius**](https://julius.ai)")
            
    # FILA 3
    c7, c8 = st.columns([1,2])
    with c7:
         with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/4504/4504605.png", width=50)
            st.subheader("HeyGen")
            st.write("Videos con avatares parlantes.")
            st.markdown("[🔗 **Abrir HeyGen**](https://www.heygen.com)")

# === SOPORTE ===
elif opcion == "📚 Guía y Soporte":
    st.title("📚 Centro de Ayuda")
    st.markdown("""
    Si tienes problemas o dudas, contacta al coordinador del proyecto.
    """)
    st.markdown("""
    <div class="contacto-box">
        <h4>👤 Contacto Oficial</h4>
        <strong>Alonso Meneses</strong><br>
        📧 <a href="mailto:armenesesz@uc.cl">armenesesz@uc.cl</a>
    </div>
    """, unsafe_allow_html=True)