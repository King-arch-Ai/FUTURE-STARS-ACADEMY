import random

def get_greeting_reply():
    replies = [
        "Hey there! ⚽ How can I assist you today?",
        "Hello! 👋 What can I do for you?",
        "Hi! Ready to help!",
        "Yo! What's up? Need anything?",
    ]
    return random.choice(replies)
from googletrans import Translator

translator = Translator()
def translate_input(user_input, target_lang='en'):
    translated = translator.translate(user_input, dest=target_lang)
    return translated.text

from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # -1 (negative) to 1 (positive)

def handle_command(input_text: str) -> str:
    if "weather in" in input_text:
        city = input_text.split("weather in")[-1].strip()
        return f"Fetching weather for {city}..."
    elif "joke" in input_text:
        return "Why don't football players get hot? Because they have fans. 😄"
    else:
        return "Command not recognized."
from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def get_reply(user_input: str) -> str:
    lower_input = user_input.lower()

    # Greeting keywords
    greetings = ["hello", "hi", "hey", "greetings", "yo"]
    if any(greet in lower_input for greet in greetings):
        return "Hey there! ⚽ How can I assist you today?"

    # Joke command
    if "joke" in lower_input or "make me laugh" in lower_input:
        return random.choice([
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.' 😴",
            "Why did the stadium get hot after the game? Because all the fans left! 😂",
            "I'm reading a book on anti-gravity. It's impossible to put down!"
        ])

    return "I'm not sure I understand. Try asking for a joke or saying hello!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    reply = get_reply(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "")
    reply = f"You said: {user_input}"  # Replace this with chatbot logic
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
pip install flask flask-cors
