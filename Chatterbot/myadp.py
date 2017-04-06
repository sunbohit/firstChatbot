from chatterbot.logic import LogicAdapter
from chatterbot.logic import BestMatch
from chatterbot.conversation import Statement

class MyLogicAdapter_1(BestMatch):
    def __init__(self, **kwargs):
        super(MyLogicAdapter_1, self).__init__(**kwargs)

    def can_process(self, statement):
        if ("肝脏" in statement.text) or ("胰腺" in statement.text) or ("肾脏" in statement.text):
            return True
        else:
            return False
    '''
    def process(self, statement):
        import random

        #confidence = random.uniform(0.5, 1)
        confidence = 1

        selected_statement = Statement('生成器官描述')

        return confidence, selected_statement
    '''
    def process(self, statement):
        if ("肝脏" in statement.text) or ("胰腺" in statement.text) or ("肾脏" in statement.text):
            closest_match = Statement('生成器官描述')
            closest_match.confidence = 1
        else:
            closest_match = self.get(input_statement)
        
        return closest_match
