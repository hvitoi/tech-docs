import streamlit as st

st.set_page_config(page_title="Streamlit Playground", page_icon="🎈", layout="wide")

st.title("Streamlit Playground")
st.caption("Run: `uv run streamlit run app.py`")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Counter")
    # the session state is simply a dictionary
    if "count" not in st.session_state:
        st.session_state.count = 0
    if st.button("Increment"):
        st.session_state.count += 1
    st.metric("Count", st.session_state.count)

with col2:
    st.subheader("Text transform")
    text = st.text_input("Input", value="Hello, Streamlit!")
    mode = st.segmented_control("Mode", ["upper", "lower", "title"], default="title")
    st.code(getattr(text, mode or "title")())
