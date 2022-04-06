import random as ran

import matplotlib.font_manager
import matplotlib.pyplot as plt
import numpy as np

""" 5组数据 """
for j in range(5):
    """ 生成x,y轴数据 """
    i = 0
    rang = int(input("Times: "))  # 玩几轮
    zh = matplotlib.font_manager.FontProperties(fname=".\\font\\SourceHanSansSC-Bold.otf")
    x = y = 0
    r = ran.randint(1, 3)  # 正确的门(随机)
    # 错误的门(根据正确的门排除剩下的)
    if r == 1:
        n1 = 2
        n2 = 3
    elif r == 2:
        n1 = 1
        n2 = 3
    else:
        n1 = 1
        n2 = 2

    for i in range(rang):
        c = ran.randint(1, 3)  # 你选的门(随机)
        if c == n1:
            c = r
        elif c == n2:
            c = r
        else:
            c = n1

        # 默认为换
        if c == r:
            x += 1  # 选对(车)
        else:
            y += 1  # 选错(山羊)

    """ 设置x,y轴数据 """
    a = np.array(["Goat", "Car"])  # 柱形图x轴数据
    b = np.array([y, x])  # 柱形图y轴数据

    """ 显示柱形图 """
    plt.title(f"测试了{i + 1}次. 猜对了:{x}次, 猜错了:{y}次.", fontproperties=zh)
    plt.bar(a, b, color=['red', 'green'])  # 设置柱形图的两轴和颜色

    plt.show()  # 显示柱形图
