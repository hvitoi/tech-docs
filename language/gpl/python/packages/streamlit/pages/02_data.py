import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data & Charts", layout="wide")
st.title("Data & Charts")

rng = np.random.default_rng(42)

@st.cache_data
def make_df() -> pd.DataFrame:
    return pd.DataFrame({
        "product": [f"Item {i}" for i in range(20)],
        "category": rng.choice(["A", "B", "C"], 20),
        "sales": rng.integers(100, 5000, 20),
        "growth": rng.uniform(-0.3, 0.5, 20).round(2),
        "active": rng.choice([True, False], 20),
    })

df = make_df()

# ── Metrics ────────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Revenue", "$84,200", "+12%")
col2.metric("Churn", "3.2%", "-0.5%", delta_color="inverse")
col3.metric("NPS", "72", "+5 pts")

st.divider()

# ── DataFrame ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("st.dataframe")
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "sales": st.column_config.NumberColumn("Sales ($)", format="$%d"),
            "growth": st.column_config.ProgressColumn("Growth", min_value=-0.3, max_value=0.5, format="%.0%%"),
            "active": st.column_config.CheckboxColumn("Active"),
        },
    )

with col2:
    st.subheader("st.json")
    st.json({"total": int(df.sales.sum()), "avg": round(float(df.sales.mean()), 1), "top": df.nlargest(3, "sales")["product"].tolist()})

st.divider()

# ── Charts ────────────────────────────────────────────────────────────────────
ts = pd.DataFrame(
    rng.integers(50, 200, (30, 3)).cumsum(axis=0),
    columns=["Product A", "Product B", "Product C"],
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("st.line_chart")
    st.line_chart(ts)

with col2:
    st.subheader("st.bar_chart")
    st.bar_chart(df.groupby("category")["sales"].sum())
