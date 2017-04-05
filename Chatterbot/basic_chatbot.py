from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot(
		'douzhishi',
		storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    	database='./douzhishi.json',
    	input_adapter='chatterbot.input.TerminalAdapter',
    	output_adapter='chatterbot.output.TerminalAdapter',
    	logic_adapters=[
        	'chatterbot.logic.MathematicalEvaluation',
        	'chatterbot.logic.TimeLogicAdapter'
    	])
bot.set_trainer(ListTrainer)
bot.train(['How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',])

while True:
	try:
		bot_input = bot.get_response(None)
		print(bot_input)
	except(KeyboardInterrupt, EOFError, SystemExit):
		break