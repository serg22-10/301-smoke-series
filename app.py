import streamlit as st

st.set_page_config(
    page_title="301 Smoke Series",
    page_icon="🔥",
    layout="wide"
)

# ---------- ESTILO ----------
st.markdown("""
<style>
.stApp{
    background:#0B0B0B;
}
h1,h2,h3,p{
    color:white;
}
.banner{
    background:#2B0000;
    border:1px solid #D61F1F;
    border-radius:16px;
    padding:16px;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🔥 301 SMOKE SERIES")
st.caption("Cartago · Costillas Ahumadas")

cupos = 15

st.markdown(f"""
<div class="banner">
<h2 style="margin:0;">Quedan {cupos} espacios disponibles</h2>
<p style="color:#FCA5A5;margin-top:8px;">
Cierre de pedidos: miércoles · Entregas sábado y domingo
</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Bienvenido")

st.write("En el siguiente paso agregaremos los cuatro combos con tus imágenes.")
