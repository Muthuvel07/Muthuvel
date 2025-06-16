def chatbot():
    print("Hi! I am a ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Bot: I'm good. How about you?")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: I'm sorry, I didn't understand that.")

chatbot()
