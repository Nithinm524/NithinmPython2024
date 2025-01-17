# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jTga6H58ngO558xZmLgxtGyjfAlFA4rJ
"""

def chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a program, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created in Python.",
        "bye": "Goodbye! Have a great day!"
    }

    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            if user_input == "bye":
                break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()