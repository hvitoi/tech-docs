import streamlit as st
import time

st.set_page_config(page_title="Layout & State", layout="wide")
st.title("Layout & State")

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Sidebar")
    theme = st.selectbox("Theme", ["Light", "Dark"])
    st.info(f"Theme: {theme}")

# ── Columns ────────────────────────────────────────────────────────────────────
st.subheader("Columns")
col1, col2, col3 = st.columns([2, 1, 1])
col1.write("**Wide column** (flex: 2)")
col2.success("Col 2")
col3.error("Col 3")

st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
st.subheader("Tabs")
tab1, tab2, tab3 = st.tabs(["Alpha", "Beta", "Gamma"])
tab1.write("Content for Alpha.")
tab2.code("print('Hello from Beta')")
tab3.bar_chart({"Q1": 10, "Q2": 20, "Q3": 15, "Q4": 25})

st.divider()

# ── Expander & Popover ────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    with st.expander("Expander"):
        st.write("Hidden until opened.")

with col2:
    with st.popover("Popover"):
        st.write("Floating overlay.")
        st.text_input("Name")

st.divider()

# ── Session state ──────────────────────────────────────────────────────────────
st.subheader("Session state")
if "items" not in st.session_state:
    st.session_state.items = []

item = st.text_input("Add item")
if st.button("Add") and item:
    st.session_state.items.append(item)

if st.session_state.items:
    st.write(st.session_state.items)
    if st.button("Clear"):
        st.session_state.items = []

st.divider()

# ── Cache ─────────────────────────────────────────────────────────────────────
st.subheader("st.cache_data")

@st.cache_data(ttl=30)
def slow_fetch(n: int) -> list:
    time.sleep(1)
    return list(range(n))

n = st.slider("n", 5, 20, 10)
t0 = time.perf_counter()
data = slow_fetch(n)
ms = (time.perf_counter() - t0) * 1000
label = "cache hit" if ms < 50 else "cache miss"
st.write(f"`{data}` — **{label}** ({ms:.0f} ms)")
