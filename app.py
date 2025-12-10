import streamlit as st
import os

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="Portal IA - UC", layout="wide", page_icon="🏛️")

# --- 2. FUNCIÓN DE IMÁGENES ---
def mostrar_imagen(nombre_base, ancho=None):
    ruta = None
    if os.path.exists(f"{nombre_base}.png"):
        ruta = f"{nombre_base}.png"
    elif os.path.exists(f"{nombre_base}.jpg"):
        ruta = f"{nombre_base}.jpg"
    
    if ruta:
        if ancho is not None:
            # Si le damos un ancho específico, lo usa
            st.image(ruta, width=ancho)
        else:
            # Si no, usa el ancho completo del contenedor (para banners)
            st.image(ruta, use_container_width=True)
    else:
        st.warning(f"⚠️ Falta imagen: {nombre_base}.png")

# --- 3. ESTILO VISUAL ---
st.markdown("""
<style>
    /* Texto General Oscuro */
    .stApp, p, h1, h2, h3, li, div { color: #212529 !important; }
    
    /* Barra Lateral Azul */
    section[data-testid="stSidebar"] { background-color: #002469 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    
    /* Tarjetas */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 20px;
        border-radius: 10px;
        text-align: center; /* Centrar contenido de las tarjetas */
    }
    /* Enlaces */
    a { color: #002469 !important; font-weight: bold; }
    
    /* Cajas de texto */
    .instruccion-box {
        background-color: #e8f4fd;
        border-left: 5px solid #002469;
        padding: 15px;
        color: #002469 !important;
        text-align: left;
    }
    .advertencia-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 15px;
        color: #856404 !important;
        text-align: left;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. BARRA LATERAL ---
with st.sidebar:
    mostrar_imagen("logo") # El logo se ajusta solo
    
    st.write("---")
    st.header("📌 Menú")
    opcion = st.radio("Ir a:", ["🏠 Inicio", "🚀 Catálogo de IAs", "📚 Guía y Soporte"])
    st.write("---")
    
    st.subheader("📞 Contacto")
    st.markdown("**Alonso Meneses**")
    st.caption("📧 armenesesz@uc.cl")
    st.write("---")
    st.info("Dirección de Personas UC")

# --- 5. CONTENIDO PRINCIPAL ---

# === INICIO ===
if opcion == "🏠 Inicio":
    st.title("🏛️ Portal de Inteligencia Artificial")
    
    # Banner centrado
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        mostrar_imagen("banner") # El banner se ajusta solo

    st.write("---")

    st.markdown("### 👋 Bienvenido/a a tu Centro de Comando Digital")
    st.write("Esta plataforma ha sido diseñada para centralizar y facilitar el acceso a las herramientas de Inteligencia Artificial permitidas para la comunidad universitaria.")

    st.markdown("""
    <div class="instruccion-box">
        <h4>👉 ¿CÓMO EMPEZAR?</h4>
        <p>1. Dirígete al <strong>menú azul de la izquierda</strong>.</p>
        <p>2. Haz clic en la opción <strong>"🚀 Catálogo de IAs"</strong>.</p>
        <p>3. Selecciona la herramienta que mejor se adapte a tu necesidad.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Herramientas", "7 IAs", "Disponibles")
    col2.metric("Acceso", "Comunidad UC", "Gratuito")
    col3.metric("Categorías", "3 Áreas", "Texto, Visual, Datos")
    
    st.write("---")
    
    st.markdown("""
    <div class="advertencia-box">
        <h4>⚠️ SEGURIDAD DE LA INFORMACIÓN</h4>
        <ul>
            <li><strong>NO ingreses datos confidenciales:</strong> Rut, fichas clínicas, datos bancarios.</li>
            <li><strong>Verifica la información:</strong> Las IAs pueden cometer errores.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === CATÁLOGO (ICONOS MÁS GRANDES AQUÍ) ===
elif opcion == "🚀 Catálogo de IAs":
    st.title("🚀 Catálogo de Soluciones")
    st.write("Explora las herramientas disponibles:")
    
    # SECCIÓN 1
    st.subheader("📝 Redacción y Oficina")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            # CAMBIO: ancho=120 (antes era 60)
            mostrar_imagen("copilot", ancho=120) 
            st.markdown("### Copilot")
            st.write("Tu experto en Microsoft Office. Ideal para Excel, analizar datos y redactar correos.")
            st.markdown("[🔗 **Abrir Copilot**](https://copilot.microsoft.com)")

    with c2:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("chatgpt", ancho=120)
            st.markdown("### ChatGPT")
            st.write("Motor de creatividad. Úsalo para ideas, borradores y traducciones.")
            st.markdown("[🔗 **Abrir ChatGPT**](https://chat.openai.com)")

    with c3:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("gemini", ancho=120)
            st.markdown("### Gemini")
            st.write("Razonamiento lógico. Analiza imágenes y procesa mucha información.")
            st.markdown("[🔗 **Abrir Gemini**](https://gemini.google.com)")

    # SECCIÓN 2
    st.write("---")
    st.subheader("🎨 Diseño y Video")
    c4, c5, c6 = st.columns(3)

    with c4:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("remini", ancho=120)
            st.markdown("### Remini")
            st.write("Restaura fotos antiguas o borrosas a alta calidad.")
            st.markdown("[🔗 **Abrir Remini**](https://remini.ai)")
            
    with c5:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("gamma", ancho=120)
            st.markdown("### Gamma")
            st.write("Crea presentaciones (PPT) completas solo con un título.")
            st.markdown("[🔗 **Abrir Gamma**](https://gamma.app)")

    with c6:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("heygen", ancho=120)
            st.markdown("### HeyGen")
            st.write("Crea videos con avatares virtuales que hablan tu texto.")
            st.markdown("[🔗 **Abrir HeyGen**](https://www.heygen.com)")

    # SECCIÓN 3
    st.write("---")
    st.subheader("📊 Datos")
    c7, c8 = st.columns([1, 2])
    
    with c7:
        with st.container(border=True):
            # CAMBIO: ancho=120
            mostrar_imagen("julius", ancho=120)
            st.markdown("### Julius AI")
            st.write("Científico de datos. Sube Excel y pide gráficos sin fórmulas.")
            st.markdown("[🔗 **Abrir Julius**](https://julius.ai)")

# === SOPORTE ===
elif opcion == "📚 Guía y Soporte":
    st.title("📚 Centro de Ayuda")
    st.markdown("Si tienes dudas o necesitas reportar un problema, estamos para ayudarte.")
    
    st.markdown("""
    <div class="instruccion-box">
        <h4>👤 Contacto Oficial</h4>
        <p><strong>Alonso Meneses</strong></p>
        <p>📧 <a href="mailto:armenesesz@uc.cl">armenesesz@uc.cl</a></p>
    </div>
    """, unsafe_allow_html=True)