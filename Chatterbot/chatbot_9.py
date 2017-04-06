from chatterbot import ChatBot
import myadp

bot = ChatBot(
    'DefaultBot',
    storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'myadp.MyLogicAdapter_1'
        },
        #{
        #    'import_path': 'chatterbot.logic.BestMatch',    
        #}
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
response = bot.get_response("多谢提醒，正要去做呢。")
print(response)
response = bot.get_response("肝脏怎么样了？")
print(response)
response = bot.get_response("肝脏")
print(response)