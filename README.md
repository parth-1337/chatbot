# AI Chatbot

This is a simple chatbot that uses AI to give you answers. It detects what kind of question you're asking and responds in different styles.

## What it does

1. You type a message
2. The chatbot figures out what type of question it is (Academic, Entertainment, Technical, Personal, or Shopping)
3. You pick how the AI should respond (like a Genius, Nervous Intern, Sarcastic Reviewer, or Calm Professor)
4. The chatbot gives you an answer in that style

## Setup

### 1. Install Python packages

```
pip install pandas scikit-learn google-generativeai streamlit
```

### 2. Add your API key

Edit `config.py` and add your Google Gemini API key:

```python
GENAI_API_KEY = "your-api-key-here"
```

Get your API key from: https://makersuite.google.com/app/apikey

### 3. Run the app

```
streamlit run app.py
```

It will open in your browser automatically.

## Files

- `app.py` - The frontend (what you see)
- `backend.py` - The chatbot logic
- `config.py` - Your API key (don't share this!)
- `data.csv` - Training data for the classifier

## How to use

1. Type your message in the text box
2. Click "Send"
3. Select a response style
4. Click "Generate answer in this style"
5. Get your answer!

## Don't forget

- Never upload `config.py` to GitHub (it's in .gitignore)
- The `.venv` folder is also ignored (Python virtual environment)
