
# Ultrivac TT - With Tank Render
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Ultrivac TT", layout="wide")

st.title("Ultrivac TT")
st.subheader("Tank Testing Intelligence")

with st.expander("Tank Info"):
    length = st.number_input("Tank Length (ft)", min_value=0.0, value=30.0)
    diameter = st.number_input("Tank Diameter (ft)", min_value=0.0, value=8.0)
    fuel_volume = st.number_input("Fuel Volume (gal)", min_value=0.0, value=5000.0)
    mic_position = st.selectbox("Mic Position", ["End", "Center", "Top", "Bottom"])

# Calculate tank volume in gallons (cylinder formula)
tank_volume = np.pi * (diameter/2)**2 * length * 7.48  # 7.48 gal/ft³
fuel_percent = min(fuel_volume / tank_volume, 1.0)

# Draw tank
fig, ax = plt.subplots(figsize=(8, 2))
ax.set_xlim(0, length)
ax.set_ylim(0, diameter)
ax.set_aspect('equal')
ax.set_facecolor('#0f1117')
ax.axis('off')

# Draw tank outline
tank = plt.Rectangle((0, 0), length, diameter, linewidth=2, edgecolor='white', facecolor='none')
ax.add_patch(tank)

# Draw fuel level
fuel_height = diameter * fuel_percent
fuel = plt.Rectangle((0, 0), length, fuel_height, color='deepskyblue', alpha=0.6)
ax.add_patch(fuel)

# Mic position marker
mic_x = {"End": 0.5, "Center": length/2, "Top": length/2, "Bottom": length/2}.get(mic_position, length/2)
mic_y = {"Top": diameter - 0.2, "Bottom": 0.2, "End": diameter/2, "Center": diameter/2}.get(mic_position, diameter/2)
ax.plot(mic_x, mic_y, 'ro', markersize=10)
ax.text(mic_x, mic_y + 0.3, 'Mic', color='red', ha='center')

st.pyplot(fig)

