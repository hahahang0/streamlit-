import streamlit as st
st.title("Chapter 2, Widgets(Chai-maker app)")
if st.button("Make chai"):
    st.success("Your chai is brewed!")

add_masala = st.checkbox("Add Masala.")
if add_masala:
    st.success("Masala added to your chai.")

tea_type = st.radio("Pick your chai base:",["milk","Sugar","Water","honey","cinnamon"])
st.write(f"{tea_type} selected.")
flavour = st.selectbox("Pick your flavour",["Adrak","Kesar","Tulsi"])
st.write(f"{flavour} selected")

sugar = st.slider("Sugar level",0,10,2)
st.write(f"selected sugar level {sugar}")

cups = st.number_input("How many cups",min_value=1,max_value=10,step=2)
st.write(f"Total {cups}")

name = st.text_input("Enter your name :")
if name:
    st.write(f"Welcome to our club,{name}")

dob = st.date_input("select your date.")
st.write(f"dob : {dob}")