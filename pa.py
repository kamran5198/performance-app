import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Employee Monthly Performance Dashboard')

# Dropdown menu for feedback
feedback_options = ["Good", "Very Good", "Excellent", "Satisfactory", "Unsatisfactory"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

with st.form("employee_data_form", clear_on_submit=True):
    st.write("Enter Employee Data")
    name = st.text_input("Employee Name")
    position = st.text_input("Job Position")
    feedback = st.selectbox("Feedback", feedback_options)
    target_performance = st.number_input("Target Units Sold for the Year", min_value=1, max_value=1200)

    # Monthly performance inputs
    monthly_performance = {month: st.number_input(f"Units Sold in {month}", min_value=0, max_value=100, key=month) for month in months}

    submit_button = st.form_submit_button(label='Submit')

# Placeholder for the analysis
analysis_placeholder = st.empty()

# Global dataframe to store the data
data_records = []

def save_data_to_csv(data, filename='employee_performance_data.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if submit_button:
    total_actual_performance = sum(monthly_performance.values())
    employee_data = {
        'Name': name,
        'Position': position,
        'Feedback': feedback,
        'Target Performance': target_performance,
        'Total Actual Performance': total_actual_performance,
        **monthly_performance  # Unpacking monthly data
    }

    # Adding data to global list
    data_records.append(employee_data)
    
    # Save data to CSV
    save_data_to_csv(data_records)

    # Descriptive Analysis and Graphical Representation
    df = pd.DataFrame(data_records)
    df.set_index('Name', inplace=True)
    df[['Target Performance', 'Total Actual Performance']].plot(kind='bar')
    analysis_placeholder.pyplot(plt)

    # Showing descriptive statistics
    analysis_placeholder.write(df.describe())

