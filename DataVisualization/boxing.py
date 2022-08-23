
import numpy as np
import matplotlib.pylab as mp
import matplotlib.animation as ma

mp.figure("Signal", facecolor='lightgray')
mp.title('Signal', fontsize=20)
mp.xlabel('Time', fontsize=14)  # 横纵坐标标签
mp.ylabel('Signal', fontsize=14)

ax = mp.gca()  # 获取坐标轴
ax.set_ylim(-3, 3)  # 垂直坐标范围
ax.set_xlim(0, 10)
mp.tick_params(labelsize=10)  # 精度值
mp.grid(linestyle=':')  # 网格线

# 创建一个plot空对象（只是没有数据，仍然是一个完整的图像）
pl = mp.plot([], [], c="orangered")[0]  # 有很多个元素，此处取一个处理
pl.set_data([], [])  # 设置数据，此处给的空数据，以便于之后将生成器的数据传入

# 接收生成器数据的更新函数
def update(data):
    t, v = data  # 时间，生成器的值
    x, y = pl.get_data()  # 获取生成器数据
    # 追加数据
    x.append(t)
    y.append(v)

    # 移动坐标轴位置，以便持续观察数据
    # 获取当前坐标轴的最小值与最大值，即坐标系的左右边界
    x_min, x_max = ax.get_xlim()
    if t >= x_max:
        # 平移坐标轴：将最小值变为当前位置减去窗口宽度，最大值变为当前值
        ax.set_xlim(t - (x_max - x_min), t)
        # 坐标系起点终点都改变了，需要重新画一个画布
        ax.figure.canvas.draw()
    # 修改数据
    pl.set_data(x, y)
#手机频谱上位机

# 生成器函数
def generator():
    t = 0  # 时间
    while True:
        # 用正弦函数来生成数据
        v = np.sin(2 * np.pi * t) * np.exp(
            np.sin(0.2 * np.pi * t)
        )  # 振幅呈正弦规律变化的正弦函数
        yield t, v  # yield的会保存状态的返回，与return不同
        t += 0.05


# 生成动画

anim = ma.FuncAnimation(mp.gcf(), update, generator, interval=0.1)

mp.show()

