# -*- coding: utf-8 -*-
"""ai.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I3Oepz-XIln3xzm7cZOk1EIT9s1O-8lk

Artificial Intelligence: Chatbot with Sentiment Analysis
"""

from textblob import TextBlob

def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    return "positive" if analysis.sentiment.polarity > 0 else "negative" if analysis.sentiment.polarity < 0 else "neutral"

def chatbot():
    print("Hi! I'm ChatBot. Let's chat! (type 'exit' to end)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        sentiment = analyze_sentiment(user_input)
        if sentiment == "positive":
            response = "That's wonderful to hear! 😊"
        elif sentiment == "negative":
            response = "I'm sorry to hear that. 😔"
        else:
            response = "Hmm, interesting. Tell me more!"

        print(f"ChatBot: {response}")

chatbot()