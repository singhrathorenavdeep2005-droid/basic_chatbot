def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Bot: Hi there!")
        elif "how are you" in user_input:
            print("Bot: I'm doing great, thanks for asking!")
        elif "your name" in user_input:
            print("Bot: I'm CodeAlpha Bot 🤖")
        elif "bye" in user_input:
            print("Bot: Goodbye! Have a great day! 👋")
            break
        else:
            print("Bot: Sorry, I didn’t understand that.")

if __name__ == "__main__":
    chatbot()
