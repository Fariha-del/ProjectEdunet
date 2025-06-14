import streamlit as st
import joblib

# Load the saved model
model = joblib.load('movie_genre_model.joblib')

st.title("Movie Genre Classifier AI")
st.write("Type a short movie plot description and get the predicted genre!")

# User input text box
user_input = st.text_area("Enter movie plot here:")

if st.button("Predict Genre"):
    if user_input.strip() == "":
        st.write("Please enter a movie plot description.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"Predicted Genre: {prediction}") 
