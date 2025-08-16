# Basic Chatbot

def chatbot():
    print("Chatbot: Hi! I'm your basic chatbot. Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run chatbot
chatbot()