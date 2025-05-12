# Ultrivac TT - Pseudo 3D Tank Render
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="Ultrivac TT", layout="wide")
st.title("Ultrivac TT")
st.subheader("Tank Testing Intelligence")

with st.expander("Tank Info"):
    length = st.number_input("Tank Length (ft)", min_value=0.0, value=30.0)
    diameter = st.number_input("Tank Diameter (ft)", min_value=0.0, value=8.0)
    fuel_volume = st.number_input("Fuel Volume (gal)", min_value=0.0, value=5000.0)
    mic_position = st.selectbox("Mic Position", ["End", "Center", "Top", "Bottom"])

# Tank volume in gallons
tank_volume = np.pi * (diameter / 2) ** 2 * length * 7.48
fuel_percent = min(fuel_volume / tank_volume, 1.0)

# Pseudo 3D rendering
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(-1, length + 1)
ax.set_ylim(-diameter, diameter * 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Tank base shape (oval ends + rectangle body)
tank_body = patches.FancyBboxPatch(
    (0, 0), length, diameter,
    boxstyle="round,pad=0.02",
    linewidth=2, edgecolor="gray", facecolor="#eeeeee"
)
ax.add_patch(tank_body)

# Fuel level
fuel_height = diameter * fuel_percent
fuel_patch = patches.FancyBboxPatch(
    (0, 0), length, fuel_height,
    boxstyle="round,pad=0.02",
    linewidth=0, facecolor="deepskyblue", alpha=0.6
)
ax.add_patch(fuel_patch)

# Mic position logic
mic_x = {"End": 0.5, "Center": length / 2, "Top": length / 2, "Bottom": length / 2}.get(mic_position, length / 2)
mic_y = {"Top": diameter - 0.2, "Bottom": 0.2, "End": diameter / 2, "Center": diameter / 2}.get(mic_position, diameter / 2)

# Mic point
ax.plot(mic_x, mic_y, 'ro', markersize=12)
ax.text(mic_x, mic_y + 0.4, 'Mic', color='red', ha='center', fontsize=10)

st.pyplot(fig)

