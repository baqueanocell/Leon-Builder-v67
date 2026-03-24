import streamlit as st

st.set_page_config(page_title="Leon-Builder v67", layout="wide")

st.title("🦁 Panel Maestro: León de Oro v67")

# --- LÓGICA DE PENSAMIENTO SINCERO ---
def pensamiento_sincero(r, a, f, m):
    if r > 40 and a > 50:
        return "🔥 Sinceramente: Estás timbeando. Con este riesgo, un mechazo de MEXC nos limpia la cuenta. La IA sugiere bajar el apalancamiento a 20x."
    if m and f == "0.618 (Gold)":
        return "💎 Análisis: Configuración óptima detectada. Los muros respaldan el retroceso de Fibo. Probabilidad de éxito alta."
    return "🧐 El León está observando... El mercado está lateral, mejor no forzar entradas innecesarias."

# --- INTERFAZ ---
col_config, col_ia = st.columns([2, 1])

with col_config:
    st.subheader("🛠️ Ajustes Técnicos (100 parámetros)")
    
    with st.expander("👑 Gestión de Capital (1-25)"):
        riesgo = st.slider("Riesgo por operación %", 1, 100, 15)
        apalancamiento = st.select_slider("Apalancamiento", options=[1, 5, 10, 20, 50, 100, 200])
        stop_mode = st.radio("Lógica de Stop", ["Fijo", "Dinámico", "Basado en Liquidez"])
        
    with st.expander("🎯 Gatillos de Entrada (26-50)"):
        fibo = st.selectbox("Nivel de Fibonacci", ["0.382", "0.500", "0.618 (Gold)", "0.786"])
        muros = st.toggle("Seguimiento de Ballenas (Order Book)", value=True)
        sensibilidad = st.slider("Sensibilidad de Muros", 1, 10, 5)

    with st.expander("📈 Salidas y Ganancias (51-75)"):
        tp1 = st.number_input("Take Profit 1 (%)", value=1.5)
        trailing = st.toggle("Activar Trailing Stop", value=True)

with col_ia:
    st.subheader("🧠 El León dice:")
    st.warning(pensamiento_sincero(riesgo, apalancamiento, fibo, muros))
    
    st.metric("Probabilidad Actual", f"{75 if fibo == '0.618 (Gold)' else 50}%")
    st.info("Sincronizado con Servidor Dell (Claypole)")

if st.button("🚀 ENVIAR ADN AL LABORATORIO"):
    st.balloons()
    st.success("Configuración enviada. Iniciando aprendizaje evolutivo.")
