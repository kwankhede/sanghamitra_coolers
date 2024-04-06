import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

def page_one():
    # Load the CSV data
    df = pd.read_csv("Test data.csv")

    # Streamlit app
    st.title("Air Cooler Performance Experiment")

    # Introduction
    st.write("In this experiment, the performance of an air cooler was evaluated under various conditions of temperature and humidity.")
    st.write("The experiment was conducted in an isolated room to maintain a controlled environment.")

    # Experiment Details
    st.subheader("Experiment Details:")
    st.write("The experiment was conducted for half an hour, and data was collected for every minute change.")
    st.write("The parameters recorded during the experiment are as follows:")

    # Parameters List
    st.write("- Time: The time elapsed in minutes.")
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
    st.write("The experiment demonstrates the effectiveness of the cooler in reducing room temperature and increasing humidity. "
            "The cooler was able to decrease the dry bulb temperature of the room from 27.4°C to 23.7°C. The wet bulb temperature of "
            "the room remained relatively stable throughout the experiment, ranging from 18.1°C to 19.6°C.")

    # 2. Change in Inlet and Outlet Trend Over Time
    st.subheader("2. Change in Inlet and Outlet Trend Over Time")
    chart2 = alt.Chart(df).mark_line().encode(
        x='Time:T',
        y=alt.Y('Change:Q', scale=alt.Scale(domain=[3, max(df['Change']) + 0.1])),
        tooltip=['Time:T', 'Change:Q']
    ).properties(width=600, height=300)
    st.altair_chart(chart2, use_container_width=True)

    st.subheader("Observation on Change in Inlet and Outlet:")
    st.write("The change in the inlet and outlet temperature of the cooler remained fairly consistent throughout the "
            "experiment, ranging from 5.7°C to 7.3°C. This suggests that the cooler was able to maintain a relatively "
            "constant output despite fluctuations in ambient temperature and humidity.")

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

    # Add a legend
    chart3 = chart3.encode(color=alt.Color('legend:N', scale=alt.Scale(scheme='category10')))
    st.altair_chart(chart3, use_container_width=True)

    st.subheader("Observation on Dry bulb VS Wet bulb:")
    st.write("The dry bulb temperature declines gradually, reaching approximately 26°C by time 30. Similarly, the wet bulb temperature decreased from 23°C to 20°C.")

    # 4. Wet Bulb Temp of Room VS Output Trend Over Time
    st.subheader("4. Wet Bulb Temp of Room VS Output Trend Over Time")
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
    st.write("Both parameters' temperatures decreased, and the graphs show the output sinking with the wet bulb temperature.")

    # Navigation to the second page
    if st.button("Go to Sales Analysis Page"):
        st.experimental_rerun()
        st.stop()

    # Signature
    st.write("@sanghamitra_tech")

def page_two():
    # Load the Sales data
    df_desert = pd.read_csv("Desert.csv")
    df_duct = pd.read_csv("Duct.csv")
    df_revenue = pd.read_csv("Max sales.csv")

    # Title of the Streamlit app
    st.title("Cooler Sales Analysis")
    st.write(""" 
    This report provides an overview of the cooler sales at Sanghamitra Business Incubator throughout the year 2022. Through a series of visualizations, we aim to illustrate and analyze the sales performance, as well as the revenue generated by our range of coolers.
    """)

    # Plot bar chart for Desert Cooler sales
    st.subheader("Sales of Desert Cooler (Bar Chart)")
    colors = ['#009bb3', '#6d4660', '#76483d']
    plt.figure(figsize=(10, 6))
    plt.bar(df_desert["Models"], df_desert["Number of coolers"], color=colors)
    plt.title("Count of Desert Cooler")
    plt.xlabel("Desert Model")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')  # Adjust rotation for better visibility
    st.pyplot(plt.gcf())

    st.subheader("Observation on Bar Chart:")
    st.write("In Desert Coolers, the 3.5 feet desert model was the best seller with sales of 10 coolers, followed by six '4 feet' desert coolers and three 2.5 feet desert coolers.")

    # Plot bar chart for Duct Cooler sales
    st.subheader("Sales of Duct Cooler (Bar Chart)")
    plt.figure(figsize=(10, 6))
    plt.bar(df_duct["Duct"], df_duct["Number of coolers"], color=colors)
    plt.title("Count of Duct Cooler")
    plt.xlabel("Duct Model")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')  # Adjust rotation for better visibility
    st.pyplot(plt.gcf())

    st.subheader("Observation on Bar Charts")
    st.write("The best-selling duct cooler was Duct 500 with six units sold, followed by 3 units of Duct 300.")

    # Pie chart for Revenue of Coolers
    st.subheader("Revenue made by Coolers")
    fig_revenue = px.pie(
        df_revenue,
        names="Size",
        values="Total",
        labels={"Size": "Cooler Size", "Total": "Revenue"},
    )
    st.plotly_chart(fig_revenue)

    st.subheader("Observation on Revenue Chart:")
    st.write("The pie chart shows that Duct 500 generated the highest revenue among all types of coolers, totaling 82,250 rupees. "
             "Even though people purchased more 3.5 feet desert coolers, the second-highest revenue was generated by it, which amounted to 65,950 rupees. "
             "This was followed by '4 feet desert' coolers, generating revenue of 41,200 rupees. The second model of Duct, 'Duct 300,' was the second most expensive cooler, "
             "generating revenue of 30,800 rupees, followed by '2.5 feet Desert' and 'Fibre' coolers, which generated revenues of 10,700 and 7,000 rupees respectively.")

    # Signature
    st.write("@sanghamitra_tech")

def main():
    pages = {
        "Air Cooler Performance Experiment": page_one,
        "Cooler Sales Analysis": page_two
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
