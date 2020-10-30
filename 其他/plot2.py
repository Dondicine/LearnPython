# coding=utf-8
# import random
from matplotlib import pyplot as plt
# from matplotlib import font_manager
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['PingFang']
# my_font = font_manager.FontProperties(
#     fname="/System/Library/Fonts/PingFang.ttc")

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置刻度

# plt.xticks(range(0, 121, 10))

# _xtick_labels = ['10点{}分'.format(i) for i in range(60)]
# _xtick_labels += ['11点{}分'.format(i) for i in range(60)]

# plt.xticks(list(x)[::3],
#             _xtick_labels[::3],
#             rotation=45,
#             ontproperties=my_font)

_xtick_labels = ['{}岁'.format(i) for i in list(x)]
plt.xticks(list(x), _xtick_labels, rotation=0)

# 绘制网格  透明度 alpha=0.5
plt.grid()
# 保存
# plt.savefig("./t1.png")

plt.show()
