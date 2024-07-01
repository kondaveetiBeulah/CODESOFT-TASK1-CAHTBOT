data = {
    "Hi":"Hi there! I'm a friendly chat bot here to assist you ?",
    "Hello":"Hello ! How can i help you today?",
    "What is your name":"I'm just a chat bot , so i dont have any name, but you can call me Chat Bot",
    "where are you from?":"I'm from digital world, always ready to chat!",
    "Do you have any hobbies or interests?":"I'm always busy helping users, so my hobby is chatting with people like you!",
    "What did you eat today?":"I don't eat, but i can help you find deliciuos recipes and food related information.",
    "what is favourite color?":"I'm a chat bot so i dont have any personal preferances for color.",
    "what is the day today?":"Wednesday",
    "how can chatbots helps humans?":"Chatbots help humans by providing instant, 24/7 customer support, handling repetitive tasks, and offering personalized recommendations. They enhance efficiency, streamline workflows, and assist in areas like education, healthcare, and e-commerce.",
    "Bye":"Bye! Take care and have a great day!",
}

def get_responses(user_input):
    for pattern,response in data.items():
            if pattern in user_input:
                    return response
    return "I'm sorry, I didn't understand that. Can you please rephrase your sentance?"

print("Chatbot: Hi! I'm a simple chat bot , I'm here to assist you!")
while True:
       user_input = input("Me: ")
       if user_input=="bye":
            print("chatbot: Goodbye! Have a great day!")
            break
       response = get_responses(user_input)
       print("Chatbot:",response)