import random
from datetime import datetime


user_name = None


def get_greeting_by_time():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"


def get_response(message):
    global user_name
    message = message.lower().strip()

    # Keyword lists for flexible matching
    greetings = ["hello", "hi", "hey", "salam", "assalamualaikum"]
    how_are_you = ["how are you", "kaise ho", "kya haal"]
    bye_words = ["bye", "goodbye", "exit", "quit", "khuda hafiz", "allah hafiz"]
    thanks_words = ["thanks", "thank you", "shukriya"]
    name_ask = ["what is your name", "who are you", "your name"]
    help_words = ["help", "what can you do", "commands"]
    mood_words = ["i am sad", "i am happy", "i feel", "mood"]
    weather_words = ["weather", "mausam", "temperature"]
    time_words = ["what time", "current time", "time now"]
    joke_words = ["joke", "funny", "laugh"]

    # Set name
    if "my name is" in message:
        user_name = message.split("my name is")[-1].strip().split()[0]
        return f"Nice to meet you, {user_name.capitalize()}! 😊"

    if any(word in message for word in greetings):
        greeting = get_greeting_by_time()
        if user_name:
            return f"{greeting} {user_name.capitalize()}! How can I help you?"
        return f"{greeting} How can I help you today?"

    elif any(word in message for word in how_are_you):
        responses = [
            "I'm doing great, thanks for asking!",
            "I'm just a bunch of code, but I'm feeling good today!",
            "Alhamdulillah, main theek hoon! Aap sunao?"
        ]
        return random.choice(responses)

    elif any(word in message for word in bye_words):
        name_part = f", {user_name.capitalize()}" if user_name else ""
        return f"Goodbye{name_part}! Take care. 👋"

    elif any(word in message for word in thanks_words):
        return random.choice(["You're welcome!", "No problem!", "Anytime!"])

    elif any(word in message for word in name_ask):
        return "I'm ChatBuddy, your friendly rule-based chatbot!"

    elif any(word in message for word in help_words):
        return ("I can chat about greetings, your mood, tell jokes, "
                "talk about weather/time, and remember your name if you tell me!")

    elif any(word in message for word in mood_words):
        if "sad" in message:
            return "I'm sorry to hear that. Want to talk about it?"
        elif "happy" in message:
            return "That's awesome! Keep smiling! 😄"
        else:
            return "Tell me more about how you're feeling."

    elif any(word in message for word in weather_words):
        return "I can't check live weather right now, but I hope it's nice outside! ☀️"

    elif any(word in message for word in time_words):
        now = datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."

    elif any(word in message for word in joke_words):
        jokes = [
            "Why don't programmers like nature? Too many bugs!",
            "Why did the computer go to the doctor? It had a virus!",
            "I told my computer I needed a break, and it froze."
        ]
        return random.choice(jokes)

    elif "?" in message:
        return "That's an interesting question! I'm not sure, but I'll try to learn about it."

    else:
        fallback = [
            "Hmm, I didn't quite get that. Can you rephrase?",
            "Sorry, I'm not sure what you mean.",
            "Can you explain that a bit differently?"
        ]
        return random.choice(fallback)


def chat():
    print("Chatbot: Hi! I'm ChatBuddy 🤖. Type 'bye' or 'exit' anytime to end the chat.")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Chatbot:", response)

        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit", "quit"]):
            break


if __name__ == "__main__":
    chat()