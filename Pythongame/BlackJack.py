"""
说明: 其基本功能沿用了Github上作者为:HelloValue的代码
      但我对其功能和界面进行了小的优化
"""
"""
                    21点游戏规则
①  2到10的牌的点数就是其牌面的数字
②  J、Q、K的点数是10分
③  A有两种算法，1或者11
④  如果A算为11时总和大于21，则A算为1
⑤  爆牌：玩家手中牌的总点数超过21点。
⑥  黑杰克（BlackJack）：一张A带一张10点的牌，比其他21点的牌大，例如（A,Q）。闲家获得黑杰克，可以获得所下注的1.5倍。
⑦  停牌：玩家不再要牌，等待其他玩家操作。
⑧  要牌：玩家根据自己手上的点数决定是否要牌，如果要牌，则系统再发一张牌给玩家。
          如果要牌后总点数超过21，则算爆牌，玩家输掉本轮游戏；若要牌后点数为21点，则不能再要；
          如果要牌后总点数不到21点，则玩家可以继续“要牌”“停牌”“加倍”。
          庄家持牌总点数少于17，则必须要牌，直到超过16，如果庄家的总点数等于或多于17点，则必须停牌。
          如果庄家手中有A，且A作11点时大于16点，做1点时小于或等于16点，则由庄家自己选择是否要牌。
⑨   加倍：双倍下注(Double)如果您已经抽取了两张纸牌，在这两张牌不是“黑杰克”的前提下，
    如果认为第三张牌可以让您赢过庄家的手牌，您可以要求「双倍押注」。您的赌注将增加双倍，而您只可以再抽取一张额外纸牌。
"""


import random,time


# 牌
class Card():
    def __init__(self, poker_type, poker_label, poker_value):
        self.poker_label = poker_label
        self.poker_value = poker_value
        self.poker_type = poker_type


# 扑克
class Poker():
    def __init__(self):
        self.pokers = []
        suites = ["♠", "♥", "♣", "♦"]
        faces = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        values = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]

        """
        self.pokers = [
            (suite,face,values[index])
            for suite in suites
            for face,values in enumerate(faces)
            
        ]
        """

        for suite in suites:
            for index, face in enumerate(faces):
                poker = Card(suite, face, values[index])
                self.pokers.append(poker)

        # 洗牌
        random.shuffle(self.pokers)

    # 发牌
    def send_poker(self, player, number=1):
        for index in range(number):
            poker = self.pokers.pop()
            player.current_pokers.append(poker)


# 玩家
class Player():
    def __init__(self, name):
        self.current_pokers = []
        self.name = name
    #清除手牌
    def clear_pokers(self):
        self.current_pokers.clear()
    #展示手牌
    def show_pokers(self):
        print(self.name + '的当前手牌:')
        for card in self.current_pokers:
            print(card.poker_type, card.poker_label, sep='', end='')
        print('')
    #获取点数
    def get_point(self):
        sum2 = 0
        """表示牌面中A的数量"""
        A = 0
        for card in self.current_pokers:
            """累计相加所有点数"""
            sum2 += card.poker_value
            """累加A的数量"""
            if card.poker_label == 'A':
                A += 1
        """如果A算为11时总和大于21"""
        if sum2 > 21 and A > 0:
            for i in range(A):
                """则A算为1"""
                sum2 = sum2 - 10

        return sum2
    #爆点
    def burst(self):
        return self.get_point() > 21

# 游戏入口
class GameManager():
    def __init__(self, player1, computer):
        manager = Poker()
        player1.clear_pokers()
        computer.clear_pokers()
        manager.send_poker(player1, 2)
        manager.send_poker(computer, 1)
        # 3.游戏开始
        end_flag = False
        computer.show_pokers()
        player1.show_pokers()
        print("================================================")
        choice = input("亲,您是否再要一张牌呢？【y/n】")
        while True:
            if choice == 'y':
                manager.send_poker(player1, 1)
                computer.show_pokers()
                player1.show_pokers()
                if player1.burst():
                    print("玩家爆牌，您输了")
                    end_flag = True
                    break
                else:
                    choice = input("亲,您是否再要一张牌呢？【y/n】")
                    print("系统正在结算...")
                    time.sleep(2)
            elif choice == 'n':
                print("===============玩家停止要牌=====================")
                break
            else:
                print("提示:您的输入有误,请重新输入~~~")
                choice = input("是否再要一张牌呢？【y/n】")
        if end_flag == False:
            while True:
                print('庄家发牌中>>>>')
                time.sleep(1)
                manager.send_poker(computer, 1)
                computer.show_pokers()
                if computer.get_point() <= 17:
                    print('')
                else:
                    if computer.burst():
                        print("系统正在结算...")
                        time.sleep(2)
                        print('庄家爆牌，您赢了')
                        end_flag = True
                        break
                    else:
                        break
        # 4.结算本局游戏
        if end_flag == False:
            player_value = player1.get_point()
            computer_value = computer.get_point()

            print("系统正在结算...")
            time.sleep(2)
            if player_value > computer_value:
                print("庄家:" + str(computer_value) + "点,闲家:" + str(player_value) + "点,您赢了")
            elif player_value == computer_value:
                print("庄家:" + str(computer_value) + "点,闲家:" + str(player_value) + "点,和棋")
            else:
                print("庄家:" + str(computer_value) + "点,闲家:" + str(player_value) + "点,您输了")



# 主程序
def main():
    print('==============游戏开始啦~~~祝您好运===============')
    player1 = Player(input("请输入您的名字:"))
    print("==============开始第1轮游戏=======================")
    print("系统正在发牌...")
    time.sleep(2)
    computer = Player('电脑')
    GameManager(player1, computer)

    index  = 2
    while True:
        print('===============================================')
        choice = input("输入是否还要继续游戏？【y/n】")
        if choice == "y":
            print(f"=============开始第{index}轮游戏===================")
            index += 1
            print("系统正在发牌...")
            time.sleep(2)
            GameManager(player1, computer)
        elif choice == "n":
            print("再见,期待您下次再来~~~~")
            break
        else:
            print("提示:您的输入有误,请重新输入~~~")


if __name__ == '__main__':
    main()