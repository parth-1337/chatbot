import streamlit as st
from backend import train_model, get_intent, get_ai_response

st.set_page_config(page_title="Chatbot", page_icon="🤖")

# Solarized Light Theme CSS
st.markdown("""
    <style>
    /* Solarized Light Theme */
    .stApp {
        background-color: #fdf6e3;
        color: #657b83;
    }
    
    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #b58900 !important; /* Solarized Yellow */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Text */
    p, label, .stMarkdown {
        color: #657b83 !important; /* Solarized Base00 */
    }
    
    /* Inputs */
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #eee8d5; /* Solarized Base2 */
        color: #586e75; /* Solarized Base01 */
        border-radius: 5px;
        border: 1px solid #93a1a1;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #268bd2; /* Solarized Blue */
        color: #fdf6e3 !important; /* Solarized Base3 */
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #2aa198; /* Solarized Cyan */
        color: #fdf6e3 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background-color: #eee8d5;
        color: #586e75;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Chatbot")

# Train model 
train_model()

# User input
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    if user_input:
        # Get intent
        detected_intent = get_intent(user_input)
        st.write(f"Intent: {detected_intent}")
        
        # Store in session state
        st.session_state.detected_intent = detected_intent
        st.session_state.user_input = user_input
        st.session_state.show_style = True
    else:
        st.write("Please enter a message")


if "show_style" in st.session_state and st.session_state.show_style:
    #style sselection
    style = st.selectbox("Choose style:", ["Overconfident Genius", "Nervous Intern", "Sarcastic Reviewer", "Calm Professor"])
    
    if st.button("Generate answer in this style"):
        with st.spinner("Generating..."):
            response = get_ai_response(st.session_state.user_input, st.session_state.detected_intent, style)
        
        st.write("Response:")
        st.text_area("", value=response, height=200, disabled=True)


