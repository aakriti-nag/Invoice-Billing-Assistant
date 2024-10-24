from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from datetime import datetime  # For timestamps

# Configure Google Generative AI with the API key
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get a response from the AI model
def get_gemini_response(input_text, image, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_text, image[0], prompt])
    return response.text

# Function to process uploaded images
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app with wide layout
st.set_page_config(page_title="Invoice/Bill Chat", layout="wide")

# Initialize chat history and input field in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Store (user_input, ai_response) tuples

if "user_input" not in st.session_state:
    st.session_state.user_input = ""  # Track the input text

# Header Section with Optional Logo
st.markdown("<h1 style='text-align: center; color: #f5f5f5;'>📄 Invoice/Bill Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #a5a5a5;'>Upload your invoice and ask me anything!</p>", unsafe_allow_html=True)

# Adjust layout: Equal space for both columns
left_col, right_col = st.columns(2)  # Equal proportions for both sections

# Left Column: Upload Image Section
with left_col:
    st.subheader("Upload Invoice")
    uploaded_file = st.file_uploader("Upload an invoice...", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Invoice", use_column_width=True)

# Right Column: Chat Interface
with right_col:
    st.subheader("Ask me!")
    st.markdown("Ask questions about the uploaded invoice below:")

    # Chat message input and send button
    col1, col2 = st.columns([4, 1])
    with col1:
        input_text = st.text_input(
            "Your question:",
            value=st.session_state.user_input,
            key="input_field",
            label_visibility="collapsed",
        )
    with col2:
        send = st.button("Send", key="send_button")

    # Process the chat interaction
    if send and input_text:
        if uploaded_file:
            # Prepare the image and prompt
            image_data = input_image_setup(uploaded_file)
            prompt = """
                You are an expert in understanding invoices.
                You will receive input images as invoices &
                you will have to answer questions based on the input image, and if
                asked about any calculation, show the calculation.
            """
            # Get the AI response
            ai_response = get_gemini_response(input_text, image_data, input_text)

            # Add the conversation with timestamp to chat history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.chat_history.append((input_text, ai_response, timestamp))

            # Clear the input field
            st.session_state.user_input = ""  # Reset the input field value
        else:
            st.warning("Please upload an image before asking questions.")

    # Display the chat history with timestamps
    st.markdown("### History")
    chat_container = st.container()
    with chat_container:
        for user_input, bot_response, timestamp in st.session_state.chat_history:
            st.markdown(
                f"<div style='background-color: #1e1e1e; padding: 15px; "
                f"border-radius: 12px; margin-bottom: 10px; color: #cfcfcf;'>"
                f"<b>You:</b> {user_input} <span style='float: right; font-size: 12px;'>{timestamp}</span></div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='background-color: #2a2a2a; padding: 15px; "
                f"border-radius: 12px; margin-bottom: 20px; "
                f"box-shadow: 2px 2px 5px rgba(0,0,0,0.2); color: #f5f5f5;'>"
                f"<b>Gemini:</b> {bot_response}</div>",
                unsafe_allow_html=True,
            )

# Footer Section
#st.markdown("<p style='text-align: center; color: #a5a5a5;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)


st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center;'>
        <p style='color: #a5a5a5;'>Made with ❤️ by Aakriti Nag</p>
        <a href='mailto:aakritinag04@gmail.com' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png' alt='Email' width='30' style='margin-right: 15px;'>
        </a>
        <a href='https://www.linkedin.com/in/aakriti-nag/' target='blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn' width='30'>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
