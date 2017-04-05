from chatterbot import ChatBot
chatbot = ChatBot("sunbohit")

from chatterbot.trainers import ListTrainer

conversation = [
    "你好！",
    "嗨，你好",
    "最近在忙什么?",
    "也没做什么。",
    "老板布置的任务要赶紧做啊。",
    "多谢提醒，正要去做呢。",
    "你忙吧，我先走了。"
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("最近在忙什么?")
print(response)