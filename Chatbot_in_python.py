import random

responses = {
    'hello': "Hey there!",
            'how are you': "I'm doing well, how about you?",
            'goodbye': "See you later!",
            'what is your work':"My work is to provide feedback to you",
            'oh nice':"yehh",
            'nice':"okk..Then Do you want to ask me something?",
            'no':"That's great!!",
            'bye':"Thanks for your time (for final exit type 'exit')",
            'thanks': "You're welcome!",
            'when you have developed':"On 23th June 2024 I have been made ",
            'what is the creasiest thing you have hear of yourself':"That I can answer any question 0_0 0_0 0_0",
            'can you tell me about yourself':"*****Thank you for asking the question.I am A Chat bot which is develop to interact with people and answer there queries*****"
   
}


def respond(message):
    message = message.lower()  
    response = responses.get(message) 
    return response

def chat():
    print("Bot: Hi! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input ==  "exit" or user_input ==  "Exit" or user_input ==  "EXIT":
            print("Bot: GoodBye!!")
            break
        else:
            print("Bot:", respond(user_input))

chat()
