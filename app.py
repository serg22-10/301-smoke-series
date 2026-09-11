import streamlit as st

st.set_page_config(
    page_title="301 Smoke Series",
    page_icon="🔥",
    layout="centered"
)
# ======================================================
# POPUP · FINALIZAR PEDIDO
# ======================================================

@st.dialog("🔥 Finalizar pedido")
def finalizar_pedido(total):

    st.markdown("""
    <style>
    div[role="dialog"]{
        background:#090909 !important;
    }

    div[role="dialog"] h1,
    div[role="dialog"] h2,
    div[role="dialog"] h3,
    div[role="dialog"] p,
    div[role="dialog"] label{
        color:white !important;
    }

    div[role="dialog"] input,
    div[role="dialog"] textarea{
        background:#2A2A2A !important;
        color:white !important;
        border:1px solid #444 !important;
        border-radius:10px !important;
    }

    div[role="dialog"] input::placeholder,
    div[role="dialog"] textarea::placeholder{
        color:#BDBDBD !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------- LOGO ----------
    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        st.image("assets/logo.png", use_container_width=True)


    # ---------- CLIENTE ----------
    st.subheader("👤 Datos del cliente")

    nombre = st.text_input(
        "Nombre completo",
        placeholder="Ej. Sergio Gómez"
    )

    telefono = st.text_input(
        "WhatsApp",
        placeholder="8888-8888"
    )

    observaciones = st.text_area(
        "Observaciones (opcional)",
        placeholder="Ej. Sin salsa, retirar por otra persona…",
        height=80
    )


    # ---------- RESUMEN ----------
    st.subheader("🧾 Tu pedido")

    def mostrar(combo, titulo):
        if st.session_state[combo] > 0:

            st.markdown(
                f"**{titulo} × {st.session_state[combo]}**"
            )

            for a in ACOMP:
                q = st.session_state[f"{combo}_{a}"]
                if q > 0:
                    st.write(f"• {a} × {q}")

            st.write("")

    mostrar("explorer", "Explorer")
    mostrar("pitmaster", "Pitmaster")
    mostrar("half", "½ Rack BBQ")
    mostrar("full", "Full Rack BBQ")

    st.subheader("🕒 Retiro")
    st.success(f"Horario: {st.session_state.horario}")

    st.markdown(f"## 💰 TOTAL: ₡ {total:,}")

    listo = (
        nombre.strip() != "" and
        telefono.strip() != "" and
        st.session_state.horario != ""
    )

    st.button(
        "📲 Enviar por WhatsApp",
        type="primary",
        use_container_width=True,
        disabled=not listo
    )
# =========================
# DATOS
# =========================
PRECIOS = {
    "explorer": 4900,
    "pitmaster": 6900,
    "half": 12900,
    "full": 23900
}

LIMITES = {
    "explorer": 1,
    "pitmaster": 2,
    "half": 3,
    "full": 3
}

ACOMP = {
    "Papas balín": "assets/papas_balin.png",
    "Ensalada": "assets/ensalada.png",
    "Elote": "assets/elote.png",
    "Yuca": "assets/yuca.png",
}

for k in PRECIOS:
    st.session_state.setdefault(k, 0)

st.session_state.setdefault("horario","")

for combo in LIMITES:
    for a in ACOMP:
        st.session_state.setdefault(f"{combo}_{a}", 0)

# =========================
# FUNCIONES
# =========================
def cupo(combo):
    return LIMITES[combo] * st.session_state[combo]

def total_acomp(combo):
    return sum(st.session_state[f"{combo}_{a}"] for a in ACOMP)

def menos(key):
    st.session_state[key] = max(0, st.session_state[key] - 1)

def mas(key):
    st.session_state[key] += 1

def menos_a(combo, acomp):
    estado = f"{combo}_{acomp}"
    st.session_state[estado] = max(0, st.session_state[estado] - 1)

def mas_a(combo, acomp):
    if total_acomp(combo) < cupo(combo):
        st.session_state[f"{combo}_{acomp}"] += 1

# =========================
# ESTILO
# =========================
st.markdown("""
<style>

/* ===== APP ===== */

.stApp,
[data-testid="stAppViewContainer"]{
    background:#090909 !important;
}

header{
    visibility:hidden;
}

.block-container{
    max-width:430px;
    padding:1rem 10px 2rem;
}

/* ===== TEXTO ===== */

h1,h2,h3,h4,h5,h6,p,span,label{
    color:white !important;
}

/* ===== BANNER ===== */

.banner{
    background:#250000;
    border:1px solid #B1121B;
    border-radius:14px;
    padding:14px;
    text-align:center;
    color:white;
    margin-bottom:18px;
}

/* ===== IMÁGENES ===== */

.stImage img{
    border-radius:14px;
}

/* ===== PRECIO ===== */

.precio{
    color:#C1121F;
    text-align:center;
    font-size:32px;
    font-weight:800;
    margin:8px 0;
}

/* ===== CONTADOR COMBOS ===== */

.qty{
    height:30px;
    background:#111;
    border:1px solid #333;
    border-radius:15px;
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:15px;
    font-weight:700;
}

/* ===== BOTONES ===== */

.stButton > button{
    width:100%;
    height:30px;
    border:none;
    border-radius:15px;
    background:#C1121F;
    color:white;
    font-size:15px;
    font-weight:700;
    padding:0;
}

/* ===== ACOMPAÑAMIENTOS ===== */

.qty-mini{
    width:38px;
    height:38px;
    background:#111;
    border:1px solid #444;
    border-radius:50%;

    display:flex;
    align-items:center;
    justify-content:center;

    color:#FFF;
    font-size:18px;
    font-weight:800;

    margin:6px auto;
}

/* Centra la columna del selector */
.acomp-card [data-testid="column"]:last-child{
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:6px;
}

/* Botones del mismo tamaño que el contador */
.acomp-card div[data-testid="stButton"]{
    display:flex;
    justify-content:center;
}

.acomp-card div[data-testid="stButton"] > button{
    width:38px !important;
    min-width:38px !important;
    max-width:38px !important;

    height:38px !important;
    min-height:38px !important;
    max-height:38px !important;

    border-radius:50% !important;
    padding:0 !important;

    display:flex !important;
    align-items:center;
    justify-content:center;

    font-size:20px !important;
    font-weight:700 !important;

    margin:0 auto !important;
}

/* ===== TOTAL ===== */

.total{
    background:#111;
    border:1px solid #333;
    border-radius:16px;
    padding:18px;
    text-align:center;
}

@media (max-width:430px){

    .block-container{
        padding-left:8px;
        padding-right:8px;
    }

    .qty{
        height:28px;
        font-size:14px;
    }

    .stButton > button{
        height:28px;
        font-size:13px;
    }

    .acomp-card div[data-testid="stButton"] > button{
        width:36px !important;
        height:36px !important;
        min-width:36px !important;
        min-height:36px !important;
        font-size:18px !important;
    }

    .qty-mini{
        width:40px;
        height:32px;
        font-size:16px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
left, center, right = st.columns([1,2,1])

with center:
    st.image("assets/logo.png", use_container_width=True)

st.markdown("""
<div class="banner">
🔥 Cerramos pedidos los miércoles<br>
Entregas sábado y domingo
</div>
""", unsafe_allow_html=True)

st.markdown("## 🍖 Costillas Ahumadas")

# =========================
# CONTADOR
# =========================
def contador(key, menos_fn, mas_fn, args):

    with st.container(horizontal=True):

        if st.button("➖", key=f"m_{key}", use_container_width=True):
            menos_fn(*args)
            st.rerun()

        st.markdown(
            f"""
            <div style="
                min-width:64px;
                height:32px;
                border-radius:16px;
                background:#111;
                border:1px solid #333;
                display:flex;
                align-items:center;
                justify-content:center;
                color:white;
                font-size:16px;
                font-weight:700;">
                {st.session_state[key]}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("➕", key=f"p_{key}", use_container_width=True):
            mas_fn(*args)
            st.rerun()

# =========================
# ACOMPAÑAMIENTOS
# =========================
def selector(combo):

    if st.session_state[combo] == 0:
        return

    st.markdown(
        f"### 🥗 Acompañamientos ({total_acomp(combo)}/{cupo(combo)})"
    )

    for nombre, imagen in ACOMP.items():

        estado = f"{combo}_{nombre}"

        with st.container(border=True):

            # Nombre
            st.markdown(f"**{nombre}**")

            # Imagen + selector en una sola fila
            img, ctrl = st.columns([1.2, 0.8], gap="medium")

            with img:
                st.image(imagen, width=110)

            with ctrl:

                st.button(
                    "➕",
                    key=f"ap_{estado}",
                    on_click=mas_a,
                    args=(combo, nombre),
                    use_container_width=True
                )

                st.markdown(
                    f"<div class='qty-mini'>{st.session_state[estado]}</div>",
                    unsafe_allow_html=True
                )

                st.button(
                    "➖",
                    key=f"am_{estado}",
                    on_click=menos_a,
                    args=(combo, nombre),
                    use_container_width=True
                )
# =========================
# TARJETAS
# =========================
def tarjeta(nombre, desc, precio, imagen, key):

    with st.container(border=True):

        st.image(imagen, use_container_width=True)

        st.markdown(f"### {nombre}")
        st.caption(desc)

        st.markdown(
            f"<div class='precio'>₡ {precio:,}</div>",
            unsafe_allow_html=True
        )

        contador(key, menos, mas, (key,))

        if st.session_state[key] > 0:
            st.divider()
            selector(key)

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

# =========================
# HORARIOS
# =========================
st.divider()
st.markdown("## 🕒 Horario de retiro")

opciones = [
    ("🌞 SÁBADO 1 · 12:00–2:00 pm", "Sábado 1"),
    ("🌙 SÁBADO 2 · 6:00–8:00 pm", "Sábado 2"),
    ("☀️ DOMINGO 1 · 12:00–2:00 pm", "Domingo 1"),
]

for texto, valor in opciones:
    if st.button(texto, use_container_width=True):
        st.session_state.horario = valor

if st.session_state.horario == "":
    st.warning("⚠️ Seleccioná un horario para continuar.")
else:
    st.success(f"Horario de retiro: {st.session_state.horario}")

# =========================
# TOTAL
# =========================
total = sum(
    st.session_state[k] * v
    for k, v in PRECIOS.items()
)

st.divider()

st.markdown(f"""
<div class="total">
    <h3 style="color:white;margin:0;">TOTAL</h3>
    <h1 style="color:#B1121B;margin-top:8px;">
        ₡ {total:,}
    </h1>
</div>
""", unsafe_allow_html=True)

faltan = any(
    st.session_state[c] > 0 and total_acomp(c) != cupo(c)
    for c in LIMITES
)

if faltan:
    st.warning("⚠️ Completá los acompañamientos")

if st.button(
    "🔥 CONTINUAR PEDIDO",
    type="primary",
    use_container_width=True,
    disabled=(total == 0 or faltan or st.session_state.horario == "")
):
    finalizar_pedido(total)