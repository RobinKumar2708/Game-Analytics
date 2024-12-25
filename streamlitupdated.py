import streamlit as st
import mysql.connector
import pandas as pd

# Function to connect to MySQL
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Umaneethi@123",
        database="sportsradar"
    )

# Function to fetch data from the database
def fetch_data(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Fetch competitors and ranking data
def get_competitor_data():
    query = """
    SELECT c.name, r.competitor_rank, c.country, r.points, r.movement, r.competitions_played
    FROM competitors_table c
    JOIN competitor_ranking_table r
    ON c.competitor_id = r.competitor_id;
    """
    return fetch_data(query)

# Streamlit Dashboard
st.title("SportsRadar Competitor Dashboard")


# Add Image below the title with specific width (400px), height will adjust automatically
st.image("C:/Users/neeth/OneDrive/Desktop/Sportsradar.jpg", width=400)


# Get the data
competitor_data = get_competitor_data()

# Summary statistics
total_competitors = competitor_data.shape[0]
countries_represented = competitor_data['country'].nunique()
highest_points = competitor_data['points'].max()

st.subheader("Summary Statistics")
st.write(f"Total Number of Competitors: {total_competitors}")
st.write(f"Number of Countries Represented: {countries_represented}")
st.write(f"Highest Points Scored by a Competitor: {highest_points}")

# Search and Filter Section
st.sidebar.header("Search and Filter Competitors")

# Search by name
search_name = st.sidebar.text_input("Search Competitor by Name")
if search_name:
    filtered_data = competitor_data[competitor_data['name'].str.contains(search_name, case=False)]
else:
    filtered_data = competitor_data

# Rank range filter with default of 1 to 500
rank_min, rank_max = st.sidebar.slider(
    "Filter by Rank Range",
    min_value=1,
    max_value=500,
    value=(1, 500)  # Set default to 1 to 500
)
filtered_data = filtered_data[(filtered_data['competitor_rank'] >= rank_min) & (filtered_data['competitor_rank'] <= rank_max)]

# Filter by country
selected_country = st.sidebar.selectbox("Filter by Country", options=["All"] + list(competitor_data['country'].unique()))
if selected_country != "All":
    filtered_data = filtered_data[filtered_data['country'] == selected_country]

# Filter by points threshold
points_threshold = st.sidebar.slider(
    "Filter by Points Threshold",
    min_value=int(competitor_data['points'].min()),
    max_value=int(competitor_data['points'].max()),
    value=int(competitor_data['points'].min())
)
filtered_data = filtered_data[filtered_data['points'] >= points_threshold]

# Reset button to reset filters
if st.sidebar.button("Reset Filters"):
    search_name = ""
    rank_min, rank_max = 1, 500  # Reset rank range to 1-500
    selected_country = "All"
    points_threshold = int(competitor_data['points'].min())

    # Re-fetch the data without filters
    filtered_data = competitor_data

# Display filtered data
st.subheader("Filtered Competitors")
st.dataframe(filtered_data)

# Competitor Details Viewer
st.sidebar.header("Competitor Details Viewer")

# Dropdown to select a competitor
selected_competitor = st.sidebar.selectbox("Select a Competitor", options=filtered_data['name'].unique())

# Display details of the selected competitor
if selected_competitor:
    competitor_details = filtered_data[filtered_data['name'] == selected_competitor].iloc[0]
    
    st.subheader(f"Details for {selected_competitor}")
    st.write(f"**Rank**: {competitor_details['competitor_rank']}")
    st.write(f"**Movement**: {competitor_details['movement']}")
    st.write(f"**Competitions Played**: {competitor_details['competitions_played']}")
    st.write(f"**Country**: {competitor_details['country']}")
    st.write(f"**Points**: {competitor_details['points']}")

# Country-Wise Analysis
st.subheader("Country-Wise Analysis")

# Aggregate the data to get total competitors and average points by country
country_analysis = filtered_data.groupby('country').agg(
    total_competitors=('name', 'count'),
    average_points=('points', 'mean')
).reset_index()

# Display the country analysis as a table
st.write(country_analysis)

# Leaderboards
st.subheader("Leaderboards")

# Top-Ranked Competitors (Top 10 by rank)
top_ranked_competitors = filtered_data.sort_values(by='competitor_rank').head(10)
st.write("### Top Ranked Competitors")
st.dataframe(top_ranked_competitors[['name', 'competitor_rank', 'country', 'points']])

# Competitors with the Highest Points (Top 10 by points)
top_points_competitors = filtered_data.sort_values(by='points', ascending=False).head(10)
st.write("### Competitors with Highest Points")
st.dataframe(top_points_competitors[['name', 'competitor_rank', 'country', 'points']])
