# Inorder to access Frontend web app, Run "streamlit run Streamlit_app.py"
import streamlit as st
import requests
import json
from io import StringIO



        
def run():
    st.title("Political Leaders Image Classification")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

    
    if st.button("Predict"):
        response = requests.post("http://0.0.0.0:80/predict", json=data)
        #response = requests.post("http://172.18.0.3:30000/predict", json=data)
        prediction =response.text
        st.success(f"The prediction from model: {prediction}")
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()