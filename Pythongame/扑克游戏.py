#定义类需要做两件事情，数据抽象（属性）和行为抽象（方法）
# 定义类需要做两件事情：数据抽象（属性）和行为抽象（方法）
import random
from enum import Enum


class Suite(Enum):
    """花色"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        return self.show()

    def show(self):
        """显示"""
        suites = ['♠︎♠︎♠♠︎', '♥♥︎', '♦♣︎', '♣♦︎']
        faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return '%s%s' % (suites[self.suite.value], faces[self.face - 1])


class Poker:
    """扑克"""

    def __init__(self):
        self.index = 0
        self.cards = [Card(suite, face)
                      for face in range(1, 14)
                      for suite in Suite]

    def shuffle(self):
        """洗牌"""
        self.index = 0
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.index]
        self.index += 1
        return card

    def has_more(self):
        """是否有牌可以发出"""
        return self.index < len(self.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_card(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        """玩家整理手上的牌"""
        # self.cards.sort(key=lambda card: card.face)
        self.cards.sort()


poker = Poker()
poker.shuffle()
names = ['东邪', '西毒']
players = [Player(name) for name in names]
for _ in range(1):
    for player in players:
        if poker.has_more():
            player.get_card(poker.deal())
for player in players:
    player.arrange()
    print(player.name)
    print(player.cards)

#class Gender(Enum):
#    FMALE, MALE,UNKNOWN = 0,1,2
#class Direction(Enum):
#    UP,RIGHT,DOWN,LEFT = range(4)