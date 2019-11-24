import random
def random_lottery_numbers():
    #列表生成式（推导式）语法
    red_balls = [num for num in range(1,34)]
    selected_balls = random.sample(red_balls,6)#抽样6个
    selected_balls.sort()#排序
    blue_balls = random.randint(1,16)
    selected_balls.append(blue_balls)
    return selected_balls

def display_numbers(balls):
    for index, ball in enumerate(balls):
        print('%02d' % ball, end=' ')
    print()
for _ in range(10):
    display_numbers(random_lottery_numbers())
    paixu = _+1