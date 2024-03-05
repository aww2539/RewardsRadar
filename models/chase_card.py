class ChaseCard():
    def __init__(self, card_id="", name="", reward_1="", reward_2="", reward_3="", reward_4="", reward_5="", reward_6=""):
        self.card_id = card_id
        self.name = name
        self.reward_1 = reward_1
        self.reward_2 = reward_2
        self.reward_3 = reward_3
        self.reward_4 = reward_4
        self.reward_5 = reward_5
        self.reward_6 = reward_6

    def __iter__(self):
        yield self.card_id
        yield self.name
        yield self.reward_1
        yield self.reward_2
        yield self.reward_3
        yield self.reward_4
        yield self.reward_5
        yield self.reward_6