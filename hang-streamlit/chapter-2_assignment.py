import streamlit as st
from datetime import date

def calculate_age(today,dob):
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

today = date.today()
st.write("Current Date, {today}")
dob = st.date_input("Enter your DOB:")
st.write(f"Your DOB is:{dob}")
age = calculate_age(today,dob)
st.write(f"Your age is : {age}.")
