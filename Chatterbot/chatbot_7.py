from chatterbot import ChatBot

bot = ChatBot(
    'DefaultBot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': '抱歉，我不太明白你们在说什么。'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)


bot.train([
    "你好！",
    "嗨，你好",
    "最近在忙什么?",
    "也没做什么。",
    "老板布置的任务要赶紧做啊。",
    "多谢提醒，正要去做呢。",
    "你忙吧，我先走了。"
])


response = bot.get_response("床前明月光")
print(response)
