import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

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
    #if st.button("Go to Sales Analysis Page"):
    #    st.session_state.page = "Cooler Sales Analysis"

    # Signature
    st.write("@sanghamitra_tech")


def page_two():
    # Load the Sales data
    df = pd.read_csv("Desert.csv")

    total = (df["Number of coolers"]).sum()
    df['Percentage'] = (df['Number of coolers'] / total) * 100

    # Title of the Streamlit app
    st.title("Sanghamitra Air Cooler Sales Dashboard")
    st.write(""" 
    This report offers an overview of cooler sales during the summer of 2022. Through 
             visualizations, our goal is to illustrate and analyze sales performance and 
             the revenue generated by our range of coolers. The objective of this analysis 
             is to gain insights into sales trends, enabling us to predict future sales and 
             make crucial decisions regarding raw material orders, inventory management, and 
             business investments. The information presented in these visualizations provides 
             insights into the best and least selling products, aiding in overall business
              process management and effective decision-making. 
    """)

    #subheading of the dataframe
    st.subheader("Price of Cooler Models")

    # Pricing data
    df_P = pd.read_csv("Pricing.csv")
    st.dataframe(df_P.set_index(df_P.columns[0]))
    st.write("""The table below represents the prices of cooler models, varying based on size,
              motor type, materials, and tank capacity. The costliest product, 'Duct 500', and
              the least expensive, 'Brio 250', differ in features. Pricing decisions were 
             informed by extensive market research and the production costs associated with
              each model. Determining economically viable yet premium prices posed a 
             challenge, but we successfully brought competitive products to market.""")

    #Bar chart
    st.subheader("Sales Percentage of coolers")
    fig = px.bar(df, x='Models', y='Percentage')

    # Display the chart using Streamlit
    st.plotly_chart(fig)

    # Observations
    st.subheader("Observations on Sales Percentage")
    st.write("""Our major audience, largely comprising the middle class, favored the 
             "Brio 300" due to its affordability and superior quality. It emerged as our 
             most popular product, followed by "Brio 450" and "Duct 500." We effectively 
             met market demands and competed with established businesses to capture a 
             significant share.""")

    # Time Series data
    st.subheader('Cooler Sales Per week')

    # Create a time series chart using Plotly Express
    dfs = pd.read_csv("Weekly sales.csv")

    total_count_s = dfs['Count'].sum()
    dfs['Sales Percentage'] = (dfs['Count'] / total_count_s) * 100
    fig_T = px.line(dfs, x='Weekly sale', y='Sales Percentage',
                    labels={'Count': 'Sales Percentage', 'Weekly sale': 'Weeks of Month'})
    # Set Y-axis limits
    fig_T.update_yaxes(range=[0, 35])
    # Display the chart using Streamlit
    st.plotly_chart(fig_T)
    st.subheader("Observations of Weekly Sales:")
    st.write("""Weekly sales exhibited fluctuations, with a slow start as customers did not
              immediately require coolers at the beginning of summer. Sales gained momentum 
             as temperatures rose, reaching peak levels from mid-March to early April. During 
             this period, the demand for cooling solutions was at its highest due to extreme temperatures.""")

    # Load the Max sales data
    data = pd.read_csv("Max sales.csv")

    # Pie chart for Revenue of Coolers
    st.subheader("Revenue made by Coolers")
    fig_revenue = px.pie(
        data,
        names="Size",
        values="Total",
        labels={"Size": "Cooler Size", "Total": "Revenue"},
    )
    st.plotly_chart(fig_revenue)
    st.subheader("Observations on Revenue:")
    st.write("""The pie chart illustrates that, despite "Brio 300" being the highest-selling
              model, "Duct 500" generated the maximum revenue of 34.6%. "Brio 300"
              followed closely with revenue of 27.7%, and "Brio 450" generated 17.3%. 
             The second Duct model, "Duct 300," the second most expensive cooler, 
             contributed 12.9% to the revenue. "Brio 150" and "Fibre" generated revenue of 4.5% and 2.94%, respectively.
    """)

    st.subheader("Conclusion")
    st.write("""The analysis has informed crucial decisions for the upcoming year's business
              processes. Based on the findings, we have adjusted our production quantities, 
             prioritizing the most popular product, "Brio 300." Additionally, we have increased
             production for "Brio 450" and "Duct 500," recognizing their popularity. This 
             strategic approach allows us to focus resources on meeting market demand efficiently. """)
    
    # Signature
    st.write("@sanghamitra_tech")


def main():
    st.sidebar.title("Sanghamitra Air Coolers")
    st.sidebar.write("Select a page to explore:")
    selection = st.sidebar.radio(
        "Go to",
        [
            "**Air Cooler Performance Experiment** - Explore the performance of an air cooler under various conditions of temperature and humidity.                           ",
            
        
            "**Cooler Sales Analysis** - Analyze sales performance and revenue generated by different cooler models.",
        ]
    )

    # Displaying the logo.png at the bottom of the sidebar
    st.sidebar.image("logo1.png", width=200, use_column_width=False)

    if "Air Cooler Performance Experiment" in selection:
        page_one()
    elif "Cooler Sales Analysis" in selection:
        page_two()


if __name__ == "__main__":
    main()
