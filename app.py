import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(
    page_title="Portal IA - UC",
    layout="wide",
    page_icon="🏛️",
    initial_sidebar_state="expanded"
)

# --- 2. FUNCIÓN PARA IMÁGENES LOCALES ---
def obtener_ruta_imagen(nombre_archivo):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directorio_actual, nombre_archivo)

# --- 3. ESTILO CSS (DISEÑO PROFESIONAL) ---
st.markdown("""
<style>
    /* Fondo general */
    .stApp {background-color: #f8f9fa;}
    
    /* Barra Lateral Azul UC */
    section[data-testid="stSidebar"] {
        background-color: #002469;
    }
    
    /* Textos del menú en blanco */
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] span, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
        color: white !important;
    }
    
    /* Títulos Principales en Azul */
    h1, h2, h3 { color: #002469 !important; }
    
    /* Tarjetas (Cards) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 20px;
        border: 1px solid #e0e0e0;
    }
    
    /* Caja de Contacto Destacada */
    .contacto-box {
        background-color: #e3f2fd;
        border-left: 5px solid #002469;
        padding: 15px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    # Carga de Logo
    ruta_logo = obtener_ruta_imagen("logo.png")
    if not os.path.exists(ruta_logo):
        ruta_logo = obtener_ruta_imagen("logo.jpg")

    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    else:
        st.header("🏛️ UC")
        st.warning("Falta 'logo.png'")
        
    st.markdown("---")
    st.header("📌 Menú")
    
    opcion = st.radio(
        "Navegación:",
        ["🏠 Inicio", "🚀 Catálogo de IAs", "📚 Guía y Soporte"]
    )
    
    st.markdown("---")
    
    # --- AQUÍ AGREGAMOS EL CONTACTO EN LA BARRA LATERAL ---
    st.markdown("### 📞 Contacto")
    st.markdown("**Alonso Meneses**")
    st.caption("📧 armenesesz@uc.cl")
    st.markdown("---")
    st.info("Dirección de Personas UC")

# --- 5. CONTENIDO PRINCIPAL ---

# === INICIO ===
if opcion == "🏠 Inicio":
    st.title("🏛️ Portal de Inteligencia Artificial")
    
    # --- BANNER CENTRADO ---
    ruta_banner = obtener_ruta_imagen("banner.jpg")
    if not os.path.exists(ruta_banner):
         ruta_banner = obtener_ruta_imagen("banner.png")

    if os.path.exists(ruta_banner):
        col_izq, col_centro, col_der = st.columns([1, 2, 1]) 
        with col_centro:
            st.image(ruta_banner, width=600)
    else:
        st.info("🖼️ (Guarda 'banner.jpg' en la carpeta para verlo aquí)")

    st.markdown("---")
    
    # Instrucciones
    st.markdown("""
    ### Bienvenido/a a tu centro de comando digital
    Esta plataforma centraliza las herramientas permitidas para el trabajo administrativo y docente.
    
    👈 **PARA COMENZAR:** Dirígete al menú azul de la izquierda y selecciona **"🚀 Catálogo de IAs"**.
    """)
    
    # Métricas
    c1, c2, c3 = st.columns(3)
    c1.metric("Herramientas", "7 IAs", "Operativas")
    c2.metric("Acceso", "Comunidad UC", "Libre")
    c3.metric("Soporte", "24/7", "Online")

    # Advertencia de Seguridad
    st.markdown("---")
    st.warning("⚠️ **IMPORTANTE: SEGURIDAD DE LA INFORMACIÓN**")
    st.markdown("""
    * **No subas datos confidenciales** (RUT, fichas médicas, datos bancarios).
    * **Verifica siempre la información** generada.
    * **Cita el uso de IA** en tus informes oficiales.
    """)

# === CATÁLOGO ===
elif opcion == "🚀 Catálogo de IAs":
    st.title("🚀 Catálogo de Soluciones")
    st.write("Explora las herramientas disponibles.")

    # FILA 1
    st.subheader("📝 Análisis y Redacción")
    col1, col2, col3 = st.columns(3)

    with col1: # COPILOT
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/Microsoft_365_Copilot_Icon.svg", width=50)
            st.markdown("### Copilot")
            st.write("**Experto en Office.** Crea fórmulas de Excel, analiza tablas y redacta en Word.")
            st.markdown("[🔗 **Abrir Copilot**](https://copilot.microsoft.com)")

    with col2: # CHATGPT
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg", width=50)
            st.markdown("### ChatGPT")
            st.write("**Creatividad.** Ideal para borradores, correos y traducciones rápidas.")
            st.markdown("[🔗 **Abrir ChatGPT**](https://chat.openai.com)")

    with col3: # GEMINI
        with st.container(border=True):
            st.image("https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg", width=50)
            st.markdown("### Gemini")
            st.write("**Lógica Avanzada.** Úsalo para planificar, leer imágenes y razonamiento complejo.")
            st.markdown("[🔗 **Abrir Gemini**](https://gemini.google.com)")

    # FILA 2
    st.subheader("🎨 Visual y Datos")
    col4, col5, col6 = st.columns(3)

    with col4: # REMINI
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/10329/10329267.png", width=50)
            st.markdown("### Remini")
            st.write("**Restauración.** Arregla fotos borrosas o antiguas de la universidad.")
            st.markdown("[🔗 **Abrir Remini**](https://remini.ai)")

    with col5: # GAMMA
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/3209/3209265.png", width=50)
            st.markdown("### Gamma")
            st.write("**Presentaciones.** Crea PPTs completos solo con el título.")
            st.markdown("[🔗 **Abrir Gamma**](https://gamma.app)")
            
    with col6: # JULIUS
        with st.container(border=True):
            st.image("https://cdn-icons-png.flaticon.com/512/2800/2800300.png", width=50)
            st.markdown("### Julius AI")
            st.write("**Analista de Datos.** Sube tu Excel y pídele gráficos sin usar fórmulas.")
            st.markdown("[🔗 **Abrir Julius**](https://julius.ai)")

# === GUÍA Y SOPORTE ===
elif opcion == "📚 Guía y Soporte":
    st.title("📚 Centro de Ayuda")
    st.markdown("""
    Si tienes dudas sobre el funcionamiento de esta plataforma, sugerencias de nuevas herramientas o necesitas reportar un problema, no dudes en contactarnos.
    """)
    
    # --- CAJA DE CONTACTO DESTACADA ---
    st.markdown("### 👤 Contacto Oficial")
    st.markdown("""
    <div class="contacto-box">
        <strong>Alonso Meneses</strong><br>
        Coordinador del Proyecto<br><br>
        📧 <a href="mailto:armenesesz@uc.cl">armenesesz@uc.cl</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Preguntas Frecuentes")
    with st.expander("¿Puedo usar mi cuenta personal?"):
        st.write("Se recomienda usar siempre el correo institucional UC para Copilot. Para ChatGPT y otras, puedes usar tu cuenta personal teniendo cuidado con los datos.")