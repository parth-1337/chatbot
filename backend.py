import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import google.generativeai as genai
from config import GENAI_API_KEY

genai.configure(api_key=GENAI_API_KEY)

# multinomial db is a model for text
#vectorizer coverts words ot numbers
vectorizer = CountVectorizer()
model = MultinomialNB()

def train_model():
    print("Loading data from CSV...")
    #use pandas to read dataset of intent
    df = pd.read_csv("data.csv")
    
    #vectorize words
    X = vectorizer.fit_transform(df['text'])
    
    #train
    model.fit(X, df['intent'])
    print("Training complete!")

def get_intent(user_text):
    # Turn the new text into numbers using the SAME vectorizer
    text_vector = vectorizer.transform([user_text])
    
    # Predict the category
    prediction = model.predict(text_vector)
    return prediction[0]

def get_ai_response(user_input, intent, style):
    # This dictionary decides the AI's "Role" based on the intent
    roles = {
        "Academic": "You are a Teacher. Explain this simply.",
        "Entertainment": "You are a Comedian. Be funny.",
        "Technical": "You are a Tech Support Guy. Fix the code.",
        "Personal": "You are a Friend. Be supportive.",
        "Shopping": "You are a Salesman. Suggest good products."
    }
    
    # This dictionary decides the "Tone" / Personality
    tones = {
        "Overconfident Genius": "Act like you are smarter than everyone. Be cocky.",
        "Nervous Intern": "Act very nervous and apologize a lot.",
        "Sarcastic Reviewer": "Be sarcastic and use witty humor.",
        "Calm Professor": "Be very calm and patient."
    }
    
    # Get the specific instructions (Default to "Helper" if not found)
    role_instruction = roles.get(intent, "You are a Helper.")
    tone_instruction = tones.get(style, "Be polite.")
    
    # Combine them into one prompt for Gemini
    final_prompt = f"""
    SYSTEM INSTRUCTIONS:
    1. {role_instruction}
    2. {tone_instruction}
    
    USER SAYS: "{user_input}"
    """
    
    
    ai = genai.GenerativeModel('gemini-3-flash-preview')
    response = ai.generate_content(final_prompt)
    return response.text

def show_style_menu():
    # Show available styles to choose from
    styles = ["Overconfident Genius", "Nervous Intern", "Sarcastic Reviewer", "Calm Professor"]
    return styles


