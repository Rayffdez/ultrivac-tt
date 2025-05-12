
# Ultrivac TT - Basic Streamlit App Structure
import streamlit as st

st.set_page_config(page_title="Ultrivac TT", layout="wide")

st.title("Ultrivac TT")
st.subheader("Tank Testing Intelligence")

with st.expander("Tank Info"):
    length = st.number_input("Tank Length (ft)", min_value=0.0)
    diameter = st.number_input("Tank Diameter (ft)", min_value=0.0)
    fuel_volume = st.number_input("Fuel Volume (gal)", min_value=0.0)
    mic_position = st.selectbox("Mic Position", ["End", "Center", "Top", "Bottom"])

st.success("This is the base version of Ultrivac TT running!")
