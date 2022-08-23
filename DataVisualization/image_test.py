import matplotlib.pyplot as plt
import numpy as np
import time
import math


# 画sin 和 cos 的图
# from math import *
#
# plt.ion() #开启interactive mode 成功的关键函数
# plt.figure(1)
# t = [0]
# t_now = 0
# m = [sin(t_now)]
#
# for i in range(2000):
# 	# plt.clf() # 清空画布上的所有内容。此处不能调用此函数，不然之前画出的点，将会被清空。
#     t_now = i*0.1
#     """
#     由于第次只画一个点，所以此处有两种方式，第一种plot函数中的样式选
#     为点'.'、'o'、'*'都可以，就是不能为线段'-'。因为一条线段需要两
#     个点才能确定。第二种方法是scatter函数，也即画点。
#     """
#     plt.plot(t_now,sin(t_now),'.') # 第次对画布添加一个点，覆盖式的。
#     # plt.scatter(t_now, sin(t_now))
#
#     plt.pause(0.1)
#     plt.show()

# import math
# import random
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# # % matplotlib
# # inline
# #
# # set up matplotlib
# is_ipython = 'inline' in matplotlib.get_backend()
# if is_ipython:
#     from IPython import display
#
# plt.ion()
#
#
#sin 和 cos 的图像

# def plot_durations(i, y1, y2):
#     plt.figure(2)
#     #     plt.clf() 此时不能调用此函数，不然之前的点将被清空。
#     plt.subplot(211)
#     plt.plot(i, y1, '.')
#     plt.subplot(212)
#     plt.plot(i, y2, '.')
#
#     plt.pause(0.001)  # pause a bit so that plots are updated
#     # if is_ipython:
#     #     display.clear_output(wait=True)
#     #     display.display(plt.gcf())
#
#
# x = np.linspace(-10, 10, 500)
# y = []
# for i in range(len(x)):
#     y1 = np.cos(i / (3 * 3.14))
#     y2 = np.sin(i / (3 * 3.14))
#     #     y.append(np.array([y1,y2])) #保存历史数据
#     plot_durations(i, y1, y2)

#散点图
#

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.axis([0, 100, 0, 1])
# plt.ion()
#
# xs = [0, 0]
# ys = [1, 1]
#
# for i in range(100):
#     y = np.random.random()
#     xs[0] = xs[1]
#     ys[0] = ys[1]
#     xs[1] = i
#     ys[1] = y
#     plt.plot(xs, ys)
#     plt.pause(0.1)


# def Method(point):
#    es_time = np.zeros([point])
#    fig=plt.figure()
#    ax=fig.add_subplot(1,1,1)
#    ax.axis("equal") #设置图像显示的时候XY轴比例
#    ax.set_xlabel('Horizontal Position')
#    ax.set_ylabel('Vertical Position')
#    ax.set_title('Vessel trajectory')
#    plt.grid(True) #添加网格
#    plt.ion()  #interactive mode on
#    IniObsX=0000
#    IniObsY=4000
#    IniObsAngle=135
#    IniObsSpeed=10*math.sqrt(2)   #米/秒
#    print('开始仿真')
#    for t in range(point):
#        t0 = time.time()
#        #障碍物船只轨迹
#        obsX=IniObsX+IniObsSpeed*math.sin(IniObsAngle/180*math.pi)*t
#        obsY=IniObsY+IniObsSpeed*math.cos(IniObsAngle/180*math.pi)*t
#        ax.scatter(obsX,obsY,c='b',marker='.')  #散点图
#        #下面的图,两船的距离
#        plt.pause(0.001)
#        es_time[t] = 1000*(time.time() - t0)
#    return es_time

# if __name__ == '__main__':
#     # xs = [0, 1]
#     # for i in range(1,100):
#     #     Method(i)
#     x = 100
#     Method(x)

import matplotlib.pyplot as plt
i=0
x=[]
y=[]
while i<100000:

    plt.clf()  #清除上一幅图像

    x.append(i)
    y.append(i**3)
    plt.plot(x,y)
    i=i+1
    plt.pause(0.01)  # 暂停0.01秒
    plt.ioff()  # 关闭画图的窗口

