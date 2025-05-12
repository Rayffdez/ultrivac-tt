
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Ultrivac TT 3D", layout="wide")
st.title("Ultrivac TT - 3D Tank Preview")
st.caption("Interactive prototype showing transparent tank wall, fuel volume, and mic placement")

# Tank dimensions
length = 30  # ft
diameter = 8  # ft
radius = diameter / 2
fuel_percent = 0.6
fuel_type = st.selectbox("Fuel Type", ["Gasoline", "Diesel", "Water"])

fuel_color = {"Gasoline": "yellow", "Diesel": "green", "Water": "blue"}[fuel_type]

# Cylinder points
z = np.linspace(0, length, 50)
theta = np.linspace(0, 2 * np.pi, 50)
z, theta = np.meshgrid(z, theta)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Outer transparent wall
tank_wall = go.Surface(
    x=x, y=y, z=z,
    opacity=0.3,
    colorscale=[[0, 'saddlebrown'], [1, 'saddlebrown']],
    showscale=False,
    name="Tank Wall"
)

# Fuel layer
z_fuel = z * fuel_percent
fuel = go.Surface(
    x=x, y=y, z=z_fuel,
    opacity=0.8,
    colorscale=[[0, fuel_color], [1, fuel_color]],
    showscale=False,
    name="Fuel"
)

# Mic in center
mic = go.Scatter3d(
    x=[0],
    y=[0],
    z=[length / 2],
    mode='markers+text',
    marker=dict(size=6, color='red'),
    text=['Mic'],
    textposition='top center',
    name="Mic"
)

layout = go.Layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Length (ft)',
        aspectratio=dict(x=1, y=1, z=3)
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

fig = go.Figure(data=[tank_wall, fuel, mic], layout=layout)
st.plotly_chart(fig, use_container_width=True)
