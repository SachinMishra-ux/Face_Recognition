# Inorder to access Frontend web app, Run "streamlit run Streamlit_app.py"
import streamlit as st
import requests
import json
from io import StringIO,BytesIO
from PIL import Image
import base64
import ast
import pandas as pd

def decode_and_parse_data(data):
    decoded_data = [base64.b64decode(item[2:-1]).decode("utf-8") for item in data]
    parsed_data = ast.literal_eval(decoded_data[0])
    return parsed_data


# Function to update the probability scores
def update_probability_scores(prediction_data):
    return prediction_data[0]['class_probability']

# Create the table
def create_table(prediction_data):
    player_names = ['maria_sharapova', 'virat_kohli', 'lionel_messi', 'serena_williams', 'roger_federer']
    probability_scores = update_probability_scores(prediction_data)

    data = {'PlayerName': player_names, 'Probability Score': probability_scores}
    df = pd.DataFrame(data)

    return df
       
def run():
    st.title("Political Leaders Image Classification")
    # Create a sidebar for image upload
    st.sidebar.title("Upload Image")
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=['png', 'jpg'])

    st.header("Results")
    if uploaded_file is not None:
        # Open the image file
        pil_image = Image.open(uploaded_file)
        # Convert the PIL Image to a base64-encoded string
        buffered = BytesIO()
        pil_image.save(buffered, format="PNG")  # You can change the format to "JPEG" if you prefer
        encoded_image = base64.b64encode(buffered.getvalue()).decode()
        # Display the uploaded image
        st.image(pil_image, caption="Uploaded Image", use_column_width=True)
        # Display the base64-encoded string
        st.text("Base64 Encoded Image:")
        st.text(encoded_image)
        data= {'image_base64_data': encoded_image}


    
    if st.button("Predict"):
        response = requests.post("http://0.0.0.0:8000/predict", json= data)
        data= (list(response))
        st.write(data)
        print(data)
        # Decode bytes and get the first element (desired data)
        desired_data1 = data[0].decode("utf-8")
        desired_data2 = data[1].decode("utf-8")
        prediction_data= eval(desired_data1+desired_data2)
        df = create_table(prediction_data)
        st.table(df)
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()