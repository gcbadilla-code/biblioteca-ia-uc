import streamlit as st
import os

# --- 1. CONFIGURACIÓN (ICONO NEGRO Y TÍTULO OFICIAL) ---
st.set_page_config(
    page_title="Portal IA - Pontificia Universidad Católica de Chile",
    layout="wide",
    page_icon="🛡️", # Usamos un escudo que se ve oscuro/negro en la mayoría de navegadores
    initial_sidebar_state="expanded"
)

# --- 2. FUNCIÓN DE IMÁGENES ---
def mostrar_imagen(nombre_base, ancho=None, banner_completo=False):
    ruta = None
    if os.path.exists(f"{nombre_base}.png"): ruta = f"{nombre_base}.png"
    elif os.path.exists(f"{nombre_base}.jpg"): ruta = f"{nombre_base}.jpg"
    
    if ruta:
        if banner_completo:
            # Para que el banner ocupe TODO el ancho y se vea HD
            st.image(ruta, use_container_width=True)
        elif ancho:
            st.image(ruta, width=ancho)
        else:
            st.image(ruta, use_container_width=True)
    else:
        st.warning(f"⚠️ Falta imagen: {nombre_base}.png")

# --- 3. ESTILO VISUAL (TIPOGRAFÍA ROBOTO UC) ---
st.markdown("""
<style>
    /* IMPORTAR FUENTE ROBOTO (OFICIAL UC) */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

    /* APLICAR FUENTE ROBOTO A TODO */
    html, body, [class*="css"], p, h1, h2, h3, h4, li, span, div, a {
        font-family: 'Roboto', sans-serif !important;
        color: #212529 !important; /* Negro corporativo */
    }
    
    /* Barra Lateral Azul UC */
    section[data-testid="stSidebar"] { background-color: #002469 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    
    /* Tarjetas (Cards) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border: 1px solid #e0e0e0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05); /* Sombra más sutil y elegante */
        padding: 25px;
        border-radius: 8px;
        text-align: center;
    }

    /* Títulos con peso oficial */
    h1, h2, h3 { font-weight: 700 !important; color: #002469 !important; }
    
    /* Enlaces */
    a { color: #002469 !important; font-weight: 700; text-decoration: none; }
    a:hover { text-decoration: underline; }

    /* Cajas de texto corporativas */
    .instruccion-box {
        background-color: #f0f4f8;
        border-left: 4px solid #002469;
        padding: 20px;
        color: #002469 !important;
    }
    .advertencia-box {
        background-color: #fffdf0;
        border-left: 4px solid #ffc107;
        padding: 20px;
        color: #856404 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. BARRA LATERAL ---
with st.sidebar:
    mostrar_imagen("logo")
    st.write("---")
    st.header("📌 Navegación")
    opcion = st.radio("Ir a:", ["🏠 Inicio", "🚀 Catálogo de IAs", "📚 Guía y Soporte"])
    st.write("---")
    st.subheader("📞 Contacto")
    st.markdown("**Alonso Meneses**")
    st.caption("📧 armenesesz@uc.cl")
    st.write("---")
    st.markdown("© 2025 Dirección de Personas UC")

# --- 5. CONTENIDO PRINCIPAL ---

# === INICIO ===
if opcion == "🏠 Inicio":
    # Banner a pantalla completa (HD)
    mostrar_imagen("banner", banner_completo=True)

    st.title("Portal de Inteligencia Artificial UC")
    st.markdown("### Bienvenido/a a tu Centro de Comando Digital")
    st.write("Plataforma centralizada para el acceso a herramientas de IA permitidas para la comunidad universitaria.")

    st.markdown("""
    <div class="instruccion-box">
        <h4>👉 ¿CÓMO EMPEZAR?</h4>
        <p>1. Dirígete al <strong>menú azul de la izquierda</strong>.</p>
        <p>2. Haz clic en <strong>"🚀 Catálogo de IAs"</strong>.</p>
        <p>3. Selecciona la herramienta que necesites.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Herramientas", "7 IAs", "Disponibles")
    c2.metric("Acceso", "Comunidad UC", "Gratuito")
    c3.metric("Categorías", "3 Áreas", "Texto, Visual, Datos")
    
    st.write("---")
    
    st.markdown("""
    <div class="advertencia-box">
        <h4>⚠️ SEGURIDAD DE LA INFORMACIÓN</h4>
        <ul>
            <li><strong>NO ingreses datos confidenciales:</strong> Rut, fichas, datos bancarios.</li>
            <li><strong>Verifica siempre:</strong> Tú eres el responsable del contenido.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# === CATÁLOGO ===
elif opcion == "🚀 Catálogo de IAs":
    st.title("🚀 Catálogo de Soluciones")
    st.write("Explora las herramientas disponibles por categoría.")
    
    # SECCIÓN 1
    st.subheader("📝 Redacción y Oficina")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.container(border=True):
            mostrar_imagen("copilot", ancho=120)
            st.markdown("### Copilot")
            st.write("Tu experto en Microsoft Office. Ideal para Excel, analizar datos y redactar correos.")
            st.markdown("[🔗 **Abrir Copilot**](https://copilot.microsoft.com)")

    with c2:
        with st.container(border=True):
            mostrar_imagen("chatgpt", ancho=120)
            st.markdown("### ChatGPT")
            st.write("Motor de creatividad. Úsalo para ideas, borradores y traducciones.")
            st.markdown("[🔗 **Abrir ChatGPT**](https://chat.openai.com)")

    with c3:
        with st.container(border=True):
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
            mostrar_imagen("remini", ancho=120)
            st.markdown("### Remini")
            st.write("Restaura fotos antiguas o borrosas a alta calidad.")
            st.markdown("[🔗 **Abrir Remini**](https://remini.ai)")
            
    with c5:
        with st.container(border=True):
            mostrar_imagen("gamma", ancho=120)
            st.markdown("### Gamma")
            st.write("Crea presentaciones (PPT) completas solo con un título.")
            st.markdown("[🔗 **Abrir Gamma**](https://gamma.app)")

    with c6:
        with st.container(border=True):
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