from chatterbot import ChatBot

bot = ChatBot(
    '特定回答',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': '洋河大曲',
            'output_text': '梦之蓝'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

response = bot.get_response('洋河大曲')
print(response)
