import streamlit as st

# App Configuration
st.set_page_config(page_title="Percentage Calculator", page_icon="📊")

# Custom CSS to make it look "App-like"
st.markdown("""
    <style>
    .main {
        max-width: 400px;
        margin: 0 auto;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #2563eb;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Percentage Calculator")

# Initialize session state
if "display_text" not in st.session_state:
    st.session_state.display_text = "0"
if "result" not in st.session_state:
    st.session_state.result = None

# Create Tabs for different functions
tab1, tab2, tab3 = st.tabs(["Is what %?", "Find Value", "Change %"])

with tab1:
    st.subheader("What % of A is B?")
    val_a = st.number_input("Total Value (A)", value=0.0, step=1.0, key="a1")
    val_b = st.number_input("Sub-Value (B)", value=0.0, step=1.0, key="b1")

    if st.button("Calculate", key="calc1"):
        if val_a != 0:
            res = (val_b / val_a) * 100
            st.session_state.display_text = f"{res:.2f}%"
            st.session_state.result = f"{res:.2f}"
        else:
            st.session_state.display_text = "Error: A cannot be 0"
            st.session_state.result = None

with tab2:
    st.subheader("What is X% of A?")
    val_a2 = st.number_input("Total Value (A)", value=0.0, step=1.0, key="a2")
    perc2 = st.number_input("Percentage (%)", value=0.0, step=1.0, key="p2")

    if st.button("Calculate", key="calc2"):
        res = (perc2 / 100) * val_a2
        st.session_state.display_text = f"{res:.2f}"
        st.session_state.result = st.session_state.display_text

with tab3:
    st.subheader("Percentage Increase/Decrease")
    orig = st.number_input("Original Value", value=0.0, step=1.0, key="d1")
    new_v = st.number_input("New Value", value=0.0, step=1.0, key="d2")

    if st.button("Calculate", key="calc3"):
        if orig != 0:
            diff = ((new_v - orig) / orig) * 100
            prefix = "+" if diff > 0 else ""
            st.session_state.display_text = f"{prefix}{diff:.2f}%"
            st.session_state.result = f"{diff:.2f}"
        else:
            st.session_state.display_text = "Error: Original value cannot be 0"
            st.session_state.result = None

# Display Result
st.divider()
st.write("### Result")
st.code(st.session_state.display_text, language=None)

if st.session_state.result:
    st.info("Tip: Hover/Tap the box above to copy the value!")

# Sidebar for Theme Info
with st.sidebar:
    st.write("### Settings")
    st.write("Streamlit follows your system's Dark/Light mode automatically. You can change this in the top-right Settings menu.")
