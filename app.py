import streamlit as st

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(
    page_title="301 Smoke Series",
    page_icon="🔥",
    layout="centered"
)

# =====================================================
# ESTADO
# =====================================================
PRECIOS = {
    "explorer": 4900,
    "pitmaster": 6900,
    "half": 12900,
    "full": 23900
}

for k in PRECIOS:
    if k not in st.session_state:
        st.session_state[k] = 0

if "horario" not in st.session_state:
    st.session_state.horario = "Sábado 1"

def mas(k):
    st.session_state[k] += 1

def menos(k):
    if st.session_state[k] > 0:
        st.session_state[k] -= 1

# =====================================================
# CSS
# =====================================================
st.markdown("""
<style>
.stApp{
    background:#090909;
    overflow-x:hidden;
}
header{visibility:hidden;}

.block-container{
    max-width:430px;
    padding:1rem 12px 2rem;
}

h1,h2,h3,h4,h5,h6,p{
    color:white !important;
}

.banner{
    background:#250000;
    border:1px solid #B1121B;
    border-radius:14px;
    padding:14px;
    text-align:center;
    margin-bottom:18px;
    color:white;
}

.precio{
    color:#B1121B;
    text-align:center;
    font-size:34px;
    font-weight:800;
    margin:8px 0 14px;
}

.qty{
    height:56px;
    width:100%;
    background:#111;
    border:1px solid #333;
    border-radius:12px;
    display:flex;
    justify-content:center;
    align-items:center;
    color:white;
    font-size:26px;
    font-weight:700;
}

.stButton > button{
    width:100%;
    height:56px;
    border:none;
    border-radius:12px;
    background:#C1121F;
    color:white;
    font-size:22px;
    font-weight:700;
    padding:0;
    line-height:1;
}

.stButton > button:hover{
    background:#981018;
}

.total{
    background:#111;
    border:1px solid #333;
    border-radius:16px;
    padding:18px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
_, logo, _ = st.columns([1,2,1])

with logo:
    st.image("assets/logo.png", use_container_width=True)

st.markdown("""
<div class="banner">
🔥 Cerramos pedidos los miércoles<br>
Entregas sábado y domingo
</div>
""", unsafe_allow_html=True)

st.markdown("## 🍖 Costillas Ahumadas")

# =====================================================
# TARJETA
# =====================================================
def tarjeta(nombre, desc, precio, imagen, key):

    with st.container(border=True):

        st.image(imagen, use_container_width=True)

        st.markdown(
            f"<h3 style='text-align:center'>{nombre}</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<p style='text-align:center'>{desc}</p>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='precio'>₡ {precio:,}</div>",
            unsafe_allow_html=True
        )

        # UNA SOLA FILA
        c1, c2, c3 = st.columns([1,1.4,1], gap="small")

        with c1:
            st.button(
                "➖",
                key=f"menos_{key}",
                on_click=menos,
                args=(key,),
                use_container_width=True
            )

        with c2:
            st.markdown(
                f"<div class='qty'>{st.session_state[key]}</div>",
                unsafe_allow_html=True
            )

        with c3:
            st.button(
                "➕",
                key=f"mas_{key}",
                on_click=mas,
                args=(key,),
                use_container_width=True
            )

# =====================================================
# COMBOS
# =====================================================
tarjeta(
    "Explorer",
    "2 ribs + 1 acompañamiento",
    4900,
    "assets/explorer.jpg",
    "explorer"
)

st.write("")

tarjeta(
    "Pitmaster",
    "3 ribs + 2 acompañamientos",
    6900,
    "assets/pitmaster.jpg",
    "pitmaster"
)

st.write("")

tarjeta(
    "½ Rack BBQ",
    "6–7 ribs + 3 acompañamientos",
    12900,
    "assets/halfrack.jpg",
    "half"
)

st.write("")

tarjeta(
    "Full Rack",
    "12–14 ribs + 3 acompañamientos",
    23900,
    "assets/fullrack.jpg",
    "full"
)

# =====================================================
# HORARIOS
# =====================================================
st.markdown("---")
st.markdown("## 📅 Horario de entrega")

if st.button("🌞 SÁBADO 1 · 12:00–2:00 pm", use_container_width=True):
    st.session_state.horario = "Sábado 1"

if st.button("🌙 SÁBADO 2 · 6:00–8:00 pm", use_container_width=True):
    st.session_state.horario = "Sábado 2"

if st.button("☀️ DOMINGO 1 · 12:00–2:00 pm", use_container_width=True):
    st.session_state.horario = "Domingo 1"

st.markdown(
    f"<p style='text-align:center;color:#B1121B;font-weight:bold;font-size:18px'>Horario: {st.session_state.horario}</p>",
    unsafe_allow_html=True
)

# =====================================================
# TOTAL
# =====================================================
total = (
    st.session_state.explorer * 4900 +
    st.session_state.pitmaster * 6900 +
    st.session_state.half * 12900 +
    st.session_state.full * 23900
)

st.markdown("---")

st.markdown(f"""
<div class='total'>
    <h3 style='color:white;margin:0'>TOTAL</h3>
    <h1 style='color:#B1121B;font-size:48px;margin-top:8px'>
        ₡ {total:,}
    </h1>
</div>
""", unsafe_allow_html=True)

st.write("")

st.button(
    "🔥 CONTINUAR PEDIDO",
    use_container_width=True,
    type="primary"
)