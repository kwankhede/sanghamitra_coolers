import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV data
df = pd.read_csv("Test data.csv")

# Streamlit app
st.title("Air Cooler Performance Experiment")

# Introduction
st.write("In the experiment, the performance of an air cooler was evaluated under various conditions of temperature and humidity.")
st.write("The experiment was conducted in an isolated room to maintain a controlled environment.")

# Experiment Details
st.subheader("Experiment Details:")
st.write("The experiment was conducted for half an hour, and data was collected for every minute change.")
st.write("The parameters recorded during the experiment are as follows:")

    # Parameters List

st.write("- Time: The time elapsed in Minutes.")
st.write("- Dry Bulb Temp of Room: The temperature of the room measured with a Digital Thermometer that does not take into account the relative humidity.")
st.write("- Wet Bulb Temp: The temperature measured with a Digital Thermometer that takes into account the relative humidity.")
st.write("- Humidity: The relative humidity of the room.")        
st.write("- Output of Cooler: The temperature of the outlet air from the cooler.")
st.write("- Input of Cooler: The temperature of the inlet air to the cooler.")
st.write("- Change in Inlet and Outlet: The difference between the input and output temperature of the cooler. The difference between the outlet temperature of the cooler and the room temperature.")


# 1. Humidity Trend Over Time
st.subheader("1. Humidity Trend Over Time")
chart1 = alt.Chart(df).mark_line().encode(
    x='Time:T',
    y = alt.Y('Humidity:Q', scale=alt.Scale(domain=[45, max(df['Humidity']) + 0.1])),
    tooltip=['Time:T', 'Humidity:Q']
).properties(width=600, height=300)
st.altair_chart(chart1, use_container_width=True)

st.subheader("Observation on Humidity Trend:")
st.write("""The experiment demonstrates the effectiveness of the cooler in reducing room temperature and increasing humidity. 
         The cooler was able to decrease the dry bulb temperature of the room from 27.4° C to 23.7° C, The wet bulb temperature of
         the room remained relatively stable throughout the experiment, ranging from 18.1° C to 19.6° C.""")
st.subheader("")


# 2. Change in Inlet and Outlet Trend Over Time
st.subheader("2. Change in Inlet and Outlet Trend Over Time")
chart2 = alt.Chart(df).mark_line().encode(
    x='Time:T',
    y=alt.Y('Change:Q', scale=alt.Scale(domain=[3, max(df['Change']) + 0.1])),
    tooltip=['Time:T', 'Change:Q']
).properties(width=600, height=300)
st.altair_chart(chart2, use_container_width=True)

st.subheader("Observation on Change in Inlet and Outlet:")
st.write("""The change in the inlet and outlet temperature of the cooler remained fairly consistent throughout the
        experiment, ranging from 5.7° C to 7.3° C. This suggests that the cooler was able to maintain a relatively
        constant output despite fluctuations in ambient temperature and humidity.""")
st.subheader("")


# 3. Dry Bulb Temp of Room VS Wet Bulb Temp Trend Over Time
st.subheader("3. Dry Bulb Temp of Room VS Wet Bulb Temp Trend Over Time")
chart3 = alt.Chart(df).mark_line().encode(
    x='Time:T',
    y=alt.Y('dry bulb:Q', scale=alt.Scale(domain=[18, max(df['dry bulb']) + 0.1])),
    color=alt.value('blue'),
    tooltip=['Time:T', 'dry bulb:Q']
) + alt.Chart(df).mark_line().encode(
    x='Time:T',
    y='wet bulb:Q',
    color=alt.value('green'),
    tooltip=['Time:T', 'wet bulb:Q']
).properties(width=600, height=300)
# Display a custom legend
st.subheader("")

st.markdown("- Dry Bulb Temperature: Blue")
st.markdown("- Wet Bulb Temperature: Green")

# Add a legend
chart3 = chart3.encode(color=alt.Color('legend:N', scale=alt.Scale(scheme='category10')))

st.altair_chart(chart3, use_container_width=True)
st.subheader("Observation on Dry bulb VS Wet bulb:")
st.write("""The dry bulb temperature declines gradually, reaching approximately 26° C by time 30. Similarly wet bulb tempreture decreased from 23 to 20° C""")
st.subheader("")

# 4. Wet Bulb Temp of Room VS Output Trend Over Time
st.subheader("4. Wet Bulb Temp of Room VS Output Trend Over Time")
st.markdown("- Output Temperature: Blue")
st.markdown("- Wet Bulb Temperature: Green")
chart4 = alt.Chart(df).mark_line().encode(
    x='Time:T',
    y=alt.Y('wet bulb:Q', scale=alt.Scale(domain=[18, max(df['wet bulb']) + 5])),
    color=alt.value('blue'),
    tooltip=['Time:T', 'wet bulb:Q']
) + alt.Chart(df).mark_line().encode(
    x='Time:T',
    y='Output:Q',
    color=alt.value('green'),
    tooltip=['Time:T', 'Output:Q']
).properties(width=600, height=300)
st.altair_chart(chart4, use_container_width=True)

st.subheader("Observation on Wet Bulb VS Output:")
st.write("""Both parameters temperature decreased and graphs shows the output sinks with the wet bulb tempreture.""")
