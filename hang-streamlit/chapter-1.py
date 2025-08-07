import streamlit  as st 

st.title("Hello Hangthim Limbu")
st.subheader("How are you ?")
st.text("Hope you are fine. This is st.text command")
st.write("And this is write command. So, choose your favorite food")

selected_food = st.selectbox("Your fav foods: ",["Oats","momo","millet roti","Brown bread","chicken"])
st.write(f"You choose  {selected_food}. Excellent Choice.")

st.success("Your Food has been served.")