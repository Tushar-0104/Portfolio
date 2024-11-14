import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from PIL import Image
import requests

# Page configuration
st.set_page_config(layout='wide')

# Load Images and Lottie Animations
image = Image.open("./img1.jpg")
image1 = Image.open("./img2.jpg")
image2 = Image.open("./img3.jpg")
image3 = Image.open("./img4.jpg")
image4 = Image.open("./img5.jpg")








# def load_lottie(path: str):
#     with open(path, "r") as file:
#         return json.load(file)

def load_lottie(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coder = load_lottie("https://lottie.host/0e7a9a3b-92bd-4b05-a0bd-8924826f179d/9dAJht16O1.json")
lottie_contact = load_lottie("https://lottie.host/e8946150-5943-4619-9566-8c7bf003b984/w9ZMkG1MX8.json")

# CSS for custom styling
st.markdown(
    """
    <style>
    /* General Body Styling */
    body {
        background-color: #f4f4f4;
        font-family: Arial, sans-serif;
        color: #333;
    }

    /* Header */
    .stApp .main .block-container {
        padding-top: 2em;
    }
    .header-text {
        font-size: 2.5em;
        color: #2b2b2b;
        font-weight: bold;
        text-align: center;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #ffffff;
        padding: 1em;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }

    /* Option Menu Styling */
    .stApp header {
        background-color: #ffffff;
        border-bottom: 1px solid #e0e0e0;
    }
    .stApp .option-menu div div div div {
        font-size: 1.2em;
        font-weight: 600;
    }

    /* Portfolio Section */
    .portfolio-item {
        border: 1px solid #ddd;
        border-radius: 8px;
        background-color: #ffffff;
        padding: 1.5em;
        margin-bottom: 1.5em;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .portfolio-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }

    /* Contact Form Styling */
    form {
        max-width: 100%;
        margin: 0 auto;
    }
    input[type="text"], input[type="email"], textarea {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
    button[type="submit"] {
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        font-size: 1em;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    button[type="submit"]:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header and Introduction
st.write("##")
st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")
st.write("""
       I'm working on this website to showcase my projects and skills. Check back for more updates!
""")
st.write("---")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=['About', 'Projects', 'Contact'],
    icons=['person', 'code-slash', 'chat-left-text-fill'],
    orientation='horizontal'
)

# About Section
if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Tushar Sharma")
            st.title("Undergrad at SKIT")
        with col2:
            st_lottie(lottie_coder, height=250)
            
    st.write("---")
    
    # Education and Experience
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("Education")
            st.markdown("""
            - **SKIT**  
                - Bachelor of Engineering in Computer Science, specializing in Artificial Intelligence  
                - Grade: 83%
            - **Bhartiya Public School**  
                - Senior Secondary, PCM  
                - Grade: 92.40%
            - **Bhartiya Public School**  
                - Secondary  
                - Grade: 79.69%
            """)
        with col4:
            st.subheader("Experience")
            st.markdown("""
            - **TensaX Innovation Lab**  
                - Artificial Intelligence Intern  
                - Duration: Present  
                - Location: Jaipur
            - **Celebal Technologies**  
                - Data Science Intern  
                - Duration: 1-6-2024 to 1-8-2024  
                - Location: Jaipur
            """)

# Projects Section
if selected == "Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")

        # FinanceFox Project
        col1, col2 = st.columns((1, 2))
        with col1:
            st.image(image, use_column_width=False, width=150)  # Set a specific width to reduce the size
        with col2:
            st.subheader("FinanceFox :moneybag:")
            st.write("""
                     This project involves using the RAG algorithm to create a conversational financial chatbot.
                     More details will be added soon.
                     """)
            st.markdown("[Visit GitHub Repo](https://github.com/Tushar-0104/Financial-ChatBot-With-every-kind-of-Financial-Advice)")
            st.markdown("[Visit my app](https://finance-chatbot-7zp8thhwazc9gncegh9hpe.streamlit.app/)")

        st.write("##")  # Spacer between projects

        # Ayurvedic ChatBot Project
        col3, col4 = st.columns((1, 2))
        with col3:
            st.image(image1, use_column_width=False, width=150)  # Set a specific width to reduce the size
        with col4:
            st.subheader("Ayurvedic ChatBot")
            st.write("""
                    This is a chatbot that helps you with health issues by offering Ayurvedic remedies to address various diseases.
                    """)
            st.markdown("[Visit GitHub Repo](https://github.com/Tushar-0104/Ayurvedic-chatBot)")
            st.markdown("[Visit my app](https://ayurvedic-chatbot-bbdujpnqdbjtck8rggus7n.streamlit.app)")
            
        st.write("##")  # Spacer between projects
        
        
                # Movie Recommendation System
        col5, col6 = st.columns((1, 2))
        with col5:
            st.image(image2, use_column_width=False, width=150)  # Set a specific width to reduce the size
        with col6:
            st.subheader("Movies Recommendation System")
            st.write("""
                    This is a movie recommendation system which helps you find similar Hollywood movies of your interest.
                    """)
            st.markdown("[Visit GitHub Repo](https://github.com/Tushar-0104/Movies_Recommandation_System)")
            st.markdown("[Visit my app](https://moviesrecommandationsystem-g8dsq8inuudubkw8cagbif.streamlit.app/)")

        st.write("##")  # Final spacer
        
        
        
        col7, col8 = st.columns((1, 2))
        with col7:
            st.image(image3, use_column_width=False, width=150)  # Set a specific width to reduce the size
        with col8:
            st.subheader("Text to Math Problem Solver")
            st.write("""
                    This is a your maths problem solver you can give me any kind of problem in the text form and my owrk is to solve that problem for you.
                    """)
            st.markdown("[Visit GitHub Repo](https://github.com/Tushar-0104/Text-to-Math-Problem-Solver/tree/main)")
            st.markdown("[Visit my app](https://text-to-math-problem-solver-v4j5hjb42xdtmspekabzbt.streamlit.app/)")

        st.write("##")  # Final spacer
        
        
        col9, col10 = st.columns((1, 2))
        with col9:
            st.image(image4, use_column_width=False, width=150)  # Set a specific width to reduce the size
        with col10:
            st.subheader("Multilingual Assistant")
            st.write("""
                    This is a your multilingual Assistant which can assist you regarding your query in multiple languages.
                    """)
            st.markdown("[Visit GitHub Repo](https://github.com/Tushar-0104/Multilingual-Assistant)")

        st.write("##")  # Final spacer


# Contact Section
if selected == "Contact":
    st.header("Get in Touch!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/tusharsharma7024@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="False">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact, height=250)
