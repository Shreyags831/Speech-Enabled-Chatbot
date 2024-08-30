import speech_recognition as sr
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from googlesearch import search  # Import from google instead of googlesearch

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Function to process user voice input
def process_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error fetching results; {e}")
        return ""

# Function to tokenize and stem text
def tokenize_and_stem(text):
    tokens = word_tokenize(text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens

# Function to search Google and retrieve information
def search_google(query):
    try:
        result = next(search(query, num=1, stop=1, pause=2, tld="com"), None)
        return result
    except StopIteration:
        return None

# Main function to handle user interaction
def chatbot():
    print("Hello! I'm your speech-enabled chatbot.")
    user_name = None
    
    while True:
        # Capture user's voice input
        user_input = process_voice_input()
        
        # Check if user input is empty
        if not user_input:
            continue
        
        # Process user's input
        tokens = tokenize_and_stem(user_input)
        query = " ".join(tokens)
        
        # Check if user greeted the bot
        if any(word in query.lower() for word in ['hello', 'hi', 'hey']):
            if not user_name:
                # Respond to the greeting and prompt for name
                print("Bot: Hello! What's your name?")
                user_name_input = process_voice_input()
                user_name = user_name_input.strip() if user_name_input else "Guest"
                print(f"Bot: Nice to meet you, {user_name}!")
            else:
                print(f"Bot: Hello again, {user_name}! How can I assist you?")
        
        # Check if user asks about the bot
        elif any(word in query.lower() for word in ['who are you', 'what are you', 'tell me about yourself']):
            print("Bot: I am a speech-enabled chatbot created to assist you with information retrieval.")
        
        elif 'exit' in query.lower():
            print("Bot: Goodbye!")
            break
        else:
            # Perform Google search based on user's query
            search_result = search_google(query)
            
            if search_result:
                print("Bot: Here's what I found:")
                print(f"Answer: {search_result}")
            else:
                print("Bot: No results found for your query.")
        
        print()  # Add a newline for clarity

# Start the chatbot
if __name__ == "__main__":
    chatbot()
