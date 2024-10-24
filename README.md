# Invoice/Billing Assistant

📄 Gemini Invoice Assistant
A streamlit-based web application that allows users to upload invoices and ask questions about them using the Gemini AI model. This app provides a chat interface where users can interact with the AI to extract insights from uploaded invoices, such as totals, terms, and other specific details.

🔍 Features
Invoice Upload: Upload JPG, PNG, or JPEG invoices.
Interactive Chat Interface: Ask detailed questions about the uploaded invoice, such as totals, terms, and individual items.
AI-Powered Responses: Powered by Gemini AI, providing quick and accurate answers.
Responsive Layout: Clean, user-friendly interface with an attractive gradient background.
History Tracking: See your chat history with timestamps for easy reference.
Footer Links: Connect with the author through email and LinkedIn.
🛠️ Technology Stack
Python
Streamlit: For building the web app interface
Google Generative AI: Gemini model for AI-powered interactions
PIL (Python Imaging Library): To handle image uploads
CSS: For custom styling
🚀 Getting Started
Prerequisites
Make sure you have the following installed:

Python 3.x
Streamlit
PIL (Python Imaging Library)
dotenv (for environment variable management)
You can install the necessary libraries using:

bash
Copy code
pip install streamlit pillow python-dotenv google-generativeai
🔧 Setup and Configuration
Clone the Repository

bash
Copy code
git clone <your-repo-url>
cd <your-repo-folder>
Create a .env File
Add your Google Generative AI API key in a .env file:

makefile
Copy code
GOOGLE_API_KEY=your-google-api-key-here
Configure Streamlit Theme
Create a .streamlit/config.toml file with the following content:

toml
Copy code
[theme]
primaryColor = "#4A90E2"
backgroundColor = "#F0F4F8"
secondaryBackgroundColor = "#D9E6F2"
textColor = "#333333"
font = "sans serif"
Run the Application
Use the following command to start the app:

bash
Copy code
streamlit run app.py
🎨 Customization
Gradient Background: The application uses a gradient background. You can customize it further in the app.py file by changing the CSS.
Footer Links: Replace the email or LinkedIn URLs in the footer section with your own if needed.
📸 Screenshots


📬 Contact
Made with ❤️ by Aakriti Nag.

Email: aakritinag04@gmail.com
LinkedIn: Aakriti Nag
📜 License
This project is licensed under the MIT License. See the LICENSE file for more details.

💡 Future Enhancements
Add OCR capabilities to extract text from scanned invoices.
Integrate multi-file uploads for batch processing.
Add voice-based interaction to enhance usability.
This README provides clear instructions on setup, functionality, and customization while giving your project a professional touch. Feel free to tweak it further to match your preferences! 😊






