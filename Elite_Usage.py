import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# Load your Excel data
df = pd.read_excel(
    io='Elite_Usage.xlsx',
    engine='openpyxl',
    skiprows=[],
    nrows=628716,
)

# Filter the DataFrame based on the 'elite_coach' column
coach_name = 'Austin McNicholas'
df_filtered = df[df['elite_coach'] == coach_name]

# Convert the 'date' column to a datetime object
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Filter records for the entire month of August
august_data = df_filtered[df_filtered['date'].dt.month == 8]

# Define a dictionary mapping usernames to email addresses
emails = {
    'ManjeetKumari': 'kumar@kumararchitecture.com',
    'MCapozzo': 'tomcapozzo@gmail.com',
    'MaxFried': 'maxsf08@gmail.com',
    'WW2buff': 'aprilcourt1@gmail.com',
}

def create_pitch_count_chart(data):
    # Group data by 'username' and calculate the total number of pitches for each user
    user_pitch_counts = data.groupby('username')['total_pitches'].sum().reset_index()

    # Sort the data in ascending order by 'total_pitches'
    user_pitch_counts_sorted = user_pitch_counts.sort_values(by='total_pitches', ascending=False)

    # Create a bar chart using Altair
    chart = alt.Chart(user_pitch_counts_sorted).mark_bar().encode(
        x=alt.X('username:N', title='Username'),
        y=alt.Y('total_pitches:Q', title='Total Pitches'),
        color=alt.Color('username:N', legend=None)  # Assigns colors to each bar
    ).properties(
        width=800,
        height=400
    )

    return chart, user_pitch_counts_sorted

def main():
    
        st.subheader(":baseball: Elite Roster Usage (August)")
        st.markdown("##")

        # Display the pitch count chart on the Main Menu page
        chart, user_pitch_counts_sorted = create_pitch_count_chart(august_data)

        st.altair_chart(chart)

        left_column, right_column = st.columns(2)

        with left_column:

            # Display the list in ascending order with top user ranked #1
            st.subheader("Top Users by Total Pitches:")
            user_pitch_counts_sorted['Rank'] = range(1, len(user_pitch_counts_sorted) + 1)
            st.dataframe(user_pitch_counts_sorted[['Rank', 'username', 'total_pitches']])

        with right_column:
            # Display the top user in blue with the largest text
            st.subheader("Giveaway Winners:")
            
            # Get the top user and Honorable Mentions
            top_user = user_pitch_counts_sorted.iloc[0]
            honorable_mentions = user_pitch_counts_sorted.iloc[1:4]

            # Style the top user and display email
            st.markdown(f"<div style='font-size: 18px; color: green;'><strong>Top User: {top_user['username']} - {top_user['total_pitches']} Pitches</strong></div>", unsafe_allow_html=True)
            st.write(f"Email: {emails.get(top_user['username'], 'Not Found')}")

            # Style the Honorable Mentions with smaller font and display emails
            for idx, mention in honorable_mentions.iterrows():
                username = mention['username']
                email = emails.get(username, 'Not Found')
                st.markdown(f"<div style='font-size: 14px; color: gray;'><strong>{mention['username']} - {mention['total_pitches']} Pitches</strong></div>", unsafe_allow_html=True)
                st.write(f"Email: {email}")


if __name__ == '__main__':
    main()
