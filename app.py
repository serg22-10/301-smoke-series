import streamlit as st

st.set_page_config(page_title="301 Smoke Series", layout="wide")

st.markdown("""
<style>
.stApp {background:#0B0B0B;}
h1,h2,h3,p {color:white;}
.banner{
    background:#2B0000;
    border:1px solid #D61F1F;
    border-radius:14px;
    padding:16px;
}
</style>
""", unsafe_allow_html=True)

# LOGO
st.image("logo.png", width=280)

st.markdown("""
<div class="banner">
<h2>🔥 Quedan 15 espacios disponibles</h2>
<p>Pedidos cierran los miércoles · Entrega sábado y domingo</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🍖 Elegí tus combos")

c1, c2 = st.columns(2)

with c1:
    st.image("explorer.jpg", use_container_width=True)
    st.write("### Explorer")
    st.write("₡4.900")
    st.number_input("Explorer", 0, 10, 0)

    st.image("halfrack.jpg", use_container_width=True)
    st.write("### ½ Rack BBQ")
    st.write("₡12.900")
    st.number_input("Half", 0, 10, 0)

with c2:
    st.image("pitmaster.jpg", use_container_width=True)
    st.write("### Pitmaster")
    st.write("₡6.900")
    st.number_input("Pit", 0, 10, 0)

    st.image("fullrack.jpg", use_container_width=True)
    st.write("### Rack Entero")
    st.write("₡23.900")
    st.number_input("Full", 0, 10, 0)
