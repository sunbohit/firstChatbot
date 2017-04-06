from chatterbot import ChatBot

chatbot = ChatBot(
    'Export_Bot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)


chatbot.train('chatterbot.corpus.chinese')

chatbot.trainer.export_for_training('./my_export.json')