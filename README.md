
# Game Analytics: Unlocking Tennis Data with SportRadar API

## Project Overview
The **SportRadar Event Explorer** project aims to develop a comprehensive solution for managing, visualizing, and analyzing sports competition data, specifically in tennis, extracted from the **Sportradar API**. The application parses JSON data, stores structured information in a relational database, and provides intuitive insights into tournaments, competition hierarchies, and event details.

This project is designed to assist sports enthusiasts, analysts, and organizations in understanding competition structures, trends, and exploring detailed event-specific information interactively.

## Skills Acquired
- **Python scripting** for data extraction and transformation.
- **API Integration** with Sportradar for retrieving sports data.
- **SQL** for data management and creating relational databases.
- **Streamlit** for interactive visualizations.

## Domain
- Sports Analytics
- Data Analytics

## Problem Statement
The objective is to build a system that:
1. Extracts data from the Sportradar API.
2. Transforms the raw JSON data into a usable format.
3. Stores the data in a structured relational database (SQL).
4. Provides interactive analysis tools and visualizations.

## Business Use Cases
1. **Event Exploration**: Navigate through competition hierarchies (e.g., ATP Vienna events).
2. **Trend Analysis**: Visualize the distribution of events by type, gender, and competition level.
3. **Performance Insights**: Analyze player participation across singles and doubles events.
4. **Decision Support**: Provide data-driven insights to event organizers or sports bodies for better resource allocation.

## Approach
### 1. **Data Extraction**
   - Parse and extract data from Sportradar JSON responses using the Sportradar API.
   - Flatten nested JSON structures into a relational schema that is suitable for analysis.

### 2. **Data Storage**
   - Create a **SQL database** with a well-designed schema.
   - Define appropriate data types, primary keys, and relationships.
   - Store extracted data (e.g., tournaments, events, players, matches) in structured tables.

### 3. **Data Analysis and Visualization**
   - Develop interactive visualizations and analytics dashboards using **Streamlit**.
   - Provide insights into trends like event distribution, player participation, and tournament structures.

## Data to be Collected
The following data points are collected from the Sportradar API:
- **Tournaments**: Information about various sports tournaments (e.g., ATP events).
- **Events**: Specific events within each tournament (e.g., singles and doubles matches).
- **Participants**: Players and their details (e.g., names, rankings).
- **Match Details**: Information about match results and performance.
- **Competition Structure**: Hierarchies within the tournaments (e.g., round-robin, knockout).

## Requirements
- Python 3.x
- Streamlit
- SQL Database (e.g., MySQL, PostgreSQL)
- Sportradar API key

## Setup Instructions
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/tennis-data-analytics.git
   cd tennis-data-analytics
   ```

2. **Install Dependencies**:
   Use `pip` to install the necessary libraries.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Sportradar API key**:
   Obtain an API key from Sportradar and add it to your project configuration.

4. **Set up the Database**:
   - Create a new SQL database and configure the connection.
   - Run the schema setup script to create necessary tables.

5. **Run the Application**:
   Use Streamlit to run the application and visualize the data.
   ```bash
   streamlit run app.py
   ```

## Project Structure
```
.
├── app.py                  # Streamlit app for interactive visualizations
├── data_extraction.py      # Script to extract and parse data from Sportradar API
├── database.py             # Database connection and schema setup
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
└── schema.sql              # SQL schema for the database
```

