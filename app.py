import streamlit as st
import joblib
model=joblib.load("spam-ham")
st.title("SPAM-HAM CLASSIFIER")
IP=st.text_input("ENTER YOUR MESSAGE")
op=model.predict([ip])
if st.button("Predict"):
  st.title(op[0])
