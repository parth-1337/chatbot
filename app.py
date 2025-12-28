import streamlit as st
from backend import train_model, get_intent, get_ai_response

st.title("AI Chatbot")

# Train model once
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
    #style seleection
    style = st.selectbox("Choose style:", ["Overconfident Genius", "Nervous Intern", "Sarcastic Reviewer", "Calm Professor"])
    
    if st.button("Generate answer in this style"):
        with st.spinner("Generating..."):
            response = get_ai_response(st.session_state.user_input, st.session_state.detected_intent, style)
        
        st.write("Response:")
        st.text_area("", value=response, height=200, disabled=True)


