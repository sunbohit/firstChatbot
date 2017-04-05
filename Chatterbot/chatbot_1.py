from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot('sean')

# Get a response to the input text 'How are you?'
response = chatbot.get_response('老板布置的任务要赶紧做啊。')

print(response)