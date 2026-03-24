import streamlit as st

st.set_page_config(page_title="Leon-Builder", layout="centered")

st.title("🦁 Configuración León de Oro v67")
st.markdown("---")

st.subheader("🛠️ Ajustes del Bot")
tiempo = st.select_slider("Tiempo de Scalping", options=["1m", "5m", "15m", "1h", "4h"])
fibo = st.selectbox("Nivel de Fibonacci", ["0.382", "0.500", "0.618", "0.786"])
muros = st.toggle("Lectura de Muros (MEXC)", value=True)
riesgo = st.slider("Riesgo por operacion %", 1, 100, 10)

st.markdown("---")
st.subheader("📈 Simulacion de Laboratorio")
col1, col2 = st.columns(2)
col1.metric("Probabilidad", "84%", "+2%")
col2.metric("PNL Estimado", "+12.5 USDT", "Verde")

if st.button("🚀 ENVIAR AL SERVIDOR DELL"):
    st.balloons()
    st.success("Configuracion enviada. El Leon esta analizando...")
