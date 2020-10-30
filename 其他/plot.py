# coding=utf-8
import random
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(
    fname="/System/Library/Fonts/PingFang.ttc")
# x = range(2, 26, 2)
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
x = range(120)
y = [random.randint(20, 35) for i in range(120)]
# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘图
plt.plot(x, y)
# 设置刻度
# plt.xticks(range(0, 121, 10))
_xtick_labels = ['10点{}分'.format(i) for i in range(60)]
_xtick_labels += ['11点{}分'.format(i) for i in range(60)]

plt.xticks(list(x)[::3],
           _xtick_labels[::3],
           rotation=45,
           fontproperties=my_font)

# 保存
# plt.savefig("./t1.png")

plt.show()
