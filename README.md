# Client-App-Usage-August-

This Python script utilizes the Streamlit, Pandas, and Altair libraries to create a data visualization tool for analyzing and presenting information related to elite coaching and pitch counts. The script performs the following key tasks:

Loads data from an Excel file and stores it in a Pandas DataFrame.
Filters the DataFrame to select data associated with a specific coach, identified as 'Austin McNicholas.'
Converts the 'date' column in the DataFrame to datetime objects.
Filters records for the entire month of August.
Defines a dictionary mapping usernames to email addresses for later use.
Defines a function create_pitch_count_chart to generate a bar chart using Altair, showing the total number of pitches for each user.
In the main function:
Creates a Streamlit web application with a subheader and markdown text.
Displays the pitch count chart using Altair.
Divides the layout into two columns.
In the left column, displays a table of top users ranked by total pitches.
In the right column, displays the top user in green with the largest text and email, along with honorable mentions in smaller font with their emails.
The script provides a user-friendly interface to analyze and visualize coaching data, particularly focusing on pitch counts for a specific coach during the month of August. It also highlights top performers and their email addresses for further communication.
