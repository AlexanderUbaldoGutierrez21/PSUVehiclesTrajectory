import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE SETUP
st.set_page_config(page_title="Vehicles Trajectory Viewer", layout="wide")

st.image("PSU_Logo1.png", width=300)
st.title("PSU Vehicle Trajectories Viewer")
st.markdown("CE 525: Transportation Operations")

# FIXED FILE PATH
file_path = "/Users/alexanderubaldogutierrez/Documents/GitHub DEVELOPER/Vehicle_TrajectoriesDGM/Trajectories_Data.txt"

# READ THE FILE
df = pd.read_csv(file_path, delim_whitespace=True, header=None)
df.columns = ["time", "vehicle_id", "vehicle_type", "location"]

# SIDE BAR FOR FILTERING
st.sidebar.image("PSU_Logo2.png", width=125)
st.sidebar.header("⚪ Display Options")
selected_ids = st.sidebar.multiselect(
    "Select Vehicle IDs to Display",
    options=sorted(df["vehicle_id"].unique()),
    default=sorted(df["vehicle_id"].unique()) if st.sidebar.checkbox("Select All", value=True) else []
)

# FILTER DATA
filtered_df = df[df["vehicle_id"].isin(selected_ids)]

# TRAJECTORIES COLORS
custom_colors = [
    "#0D1B2A", "#1B263B", "#415A77", "#778DA9", "#E0E1DD",
    "#0F4C81", "#2A6F97", "#4FB0C6", "#7AD0D9", "#BEE3DB"
]

# CREATE INTERACTIVE PLOT
fig = px.line(
    filtered_df,
    x="time",
    y="location",
    color="vehicle_id",
    color_discrete_sequence=custom_colors,
    title="💻 Time-Space Diagram",
    labels={"time": "Time (seconds)", "location": "Location (feet)", "vehicle_id": "Vehicle ID"}
)

fig.update_layout(
    legend=dict(title="Vehicle ID"),
    hovermode="x unified"
)

# DISPLAY IN STREAMLIT
st.plotly_chart(fig, use_container_width=True)