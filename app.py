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

# Create Tabs for different functions
tab1, tab2, tab3 = st.tabs(["Is what %?", "Find Value", "Change %"])

result = None
display_text = "0"

with tab1:
    st.subheader("What % of A is B?")
    val_a = st.number_input("Total Value (A)", value=0.0, step=1.0, key="a1")
    val_b = st.number_input("Sub-Value (B)", value=0.0, step=1.0, key="b1")
    
    if val_a != 0:
        res = (val_b / val_a) * 100
        display_text = f"{res:.2f}%"
        result = f"{res:.2f}"

with tab2:
    st.subheader("What is X% of A?")
    val_a2 = st.number_input("Total Value (A)", value=0.0, step=1.0, key="a2")
    perc2 = st.number_input("Percentage (%)", value=0.0, step=1.0, key="p2")
    
    res = (perc2 / 100) * val_a2
    display_text = f"{res:.2f}"
    result = display_text

with tab3:
    st.subheader("Percentage Increase/Decrease")
    orig = st.number_input("Original Value", value=0.0, step=1.0, key="d1")
    new_v = st.number_input("New Value", value=0.0, step=1.0, key="d2")
    
    if orig != 0:
        diff = ((new_v - orig) / orig) * 100
        prefix = "+" if diff > 0 else ""
        display_text = f"{prefix}{diff:.2f}%"
        result = f"{diff:.2f}"

# Display Result
st.divider()
st.write("### Result")
st.code(display_text, language=None)

# Streamlit's built-in "Copy to Clipboard" is available via the code block above, 
# but we can add a helper button for mobile users.
if result:
    st.info("Tip: Hover/Tap the box above to copy the value!")

# Sidebar for Theme Info
with st.sidebar:
    st.write("### Settings")
    st.write("Streamlit follows your system's Dark/Light mode automatically. You can change this in the top-right Settings menu.")
