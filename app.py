import streamlit as st

st.set_page_config(page_title="Leon-Builder v67", layout="centered")

# --- ESTILO PERSONALIZADO ---
st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🦁 León-Builder: Configuración Maestra")

# --- SECCIÓN 1: PENSAMIENTO DE LA IA (DINÁMICO) ---
st.subheader("🧠 Pensamiento del León en el Laboratorio")

# Lógica del pensamiento según la configuración
def generar_pensamiento(r, a, f):
    if r > 50 and a > 50:
        return "⚠️ Cristian, esta configuración es extremadamente agresiva. El riesgo de liquidación es alto. ¿Estás probando el hardware al límite?"
    elif f == "0.618 (Gold)":
        return "✨ Excelente elección. El nivel 0.618 tiene una probabilidad histórica del 74% en MEXC según mis últimos 30 registros."
    else:
        return "🦁 Estoy analizando los muros de volumen... El mercado está tranquilo, la configuración parece sólida."

# --- SECCIÓN 2: CONFIGURACIONES (MÓDULOS) ---
with st.expander("📊 Gestión de Riesgo (1-25)", expanded=True):
    riesgo = st.slider("Riesgo por operación %", 1, 100, 10)
    apalancamiento = st.select_slider("Apalancamiento", options=[1, 5, 10, 20, 50, 100, 200])
    stop_loss = st.selectbox("Tipo de Stop Loss", ["Fijo", "Trailing", "Basado en ATR"])

with st.expander("📉 Análisis Técnico (26-50)"):
    tiempo = st.select_slider("Temporalidad", options=["1m", "5m", "15m", "1h", "4h"])
    fibo = st.selectbox("Nivel de Fibonacci", ["0.382", "0.500", "0.618 (Gold)", "0.786"])
    muros = st.toggle("Lectura de Muros Pro (Order Book)", value=True)
    volumen_min = st.number_input("Volumen mínimo (USDT)", value=10000)

with st.expander("🤖 IA y Automatización (51-75)"):
    modo_ia = st.radio("Comportamiento IA", ["Conservador", "Dinámico", "Evolutivo"])
    noticias = st.toggle("Filtro de Sentimiento (News/Social)", value=True)
    reentradas = st.slider("Máximo de Re-entradas (DCA)", 0, 5, 2)

# Mostrar el pensamiento en un cuadro destacado
st.info(generar_pensamiento(riesgo, apalancamiento, fibo))

# --- SECCIÓN 3: RESULTADOS SIMULADOS ---
st.markdown("---")
col1, col2 = st.columns(2)
# Simulación de probabilidad dinámica
prob = 85 if fibo == "0.618 (Gold)" else 60
col1.metric("Probabilidad Éxito", f"{prob}%", "+2%")
col2.metric("Estado del Laboratorio", "Aprendiendo", "Dell Server")

if st.button("🚀 SUBIR CONFIGURACIÓN AL LEÓN"):
    st.balloons()
    st.success("Configuración enviada al servidor Dell. Iniciando simulación de PNL...")
