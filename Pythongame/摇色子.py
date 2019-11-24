import random
def roll_dice(num=1):
    total = 0
    for _ in range(num):
        total += random.randint(1,6)
    return total
def main():
    money = 1000
    while money >0 :
        print("你的总资产为: %d" % money)
        debt = 0
        while debt <=0 or debt > money:
            debt = int(input("请下注:"))
        first_point = roll_dice(2)
        print('玩家摇出了%d点' % first_point)
        go_on = False
        if first_point in (7,11):
            print("玩家胜")
            money += debt
        elif first_point in (2,3,12):
            print("庄家胜")
            money -= debt
        else:
            go_on = True
        while go_on:
            current_point = roll_dice(2)
            print('玩家摇出了%d点' % current_point)
            if current_point =="7":
                print("庄家胜！")
                money -= debt
                go_on = False
            elif current_point == first_point:
                print("玩家胜")
                money += debt
                go_on = False
    print("你已经破产啦,游戏结束啦")

if __name__ == "__main__":
    main()
