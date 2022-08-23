"""示波器的可视化 """
import random

import numpy as np
import matplotlib.pyplot as plt


from CalibrationSoftware.public_class import PublicClass

# 	# =========================================================
# 	# 数据转换  十进制 -- 二进制
# 	# =========================================================

class InstrumentVisal(PublicClass):
    def __init__(self):
        pass
        # super(InstrumentVisal, self).__init__()

    def true2complement(self, str_bin):
        str_new = ""
        if str_bin[0] == "0":
            str_flash = str_bin
        else:
            for i in str_bin[1:]:
                if i == "0":
                    str_new += "1"
                else:
                    str_new += "0"
            str_flash = '0' + str_new  # 反码
        return str_flash

    def number_read(self):
        infile = r'../DataVisualization/test.txt'
        with open(infile) as f:
            s = f.read()
        return s

    # 	# =========================================================
    # 	# 数据处理
    # 	# =========================================================
    def convertDectoHex(self):
        bin_int_handle_list = []
        self.number_read()
        s = self.number_read()
        for number in range(30, len(s) - 24, 6):
            # 字符串的处理
            m = s[number:number + 6]
            new_str_two = str.strip(m)
            new_str = new_str_two.split(" ")
            new_str = new_str[1] + new_str[0]
            # 转化成
            complement_binary = int(new_str, 16) - 1
            com_str = bin(complement_binary)
            com_bin_str = com_str[2:]
            bin_handle = self.true2complement(com_bin_str)
            bin_int_handle = int(bin_handle, 2) / 10
            bin_int_handle = - bin_int_handle
            bin_int_handle_list.append(bin_int_handle)
        return bin_int_handle_list



    # 	# =========================================================
    # 	# x轴数据
    # 	# =========================================================
    # def x_number(self):
    #     pass

    # 	# =========================================================
    # 	# y轴数据
    # 	# =========================================================
    def y_number(self):
        pass

    # 	# =========================================================
    # 	# 图形绘制
    # 	# =========================================================
    def picture_show(self):
        # t = random.randrange(1000, 3000)
        # t = np.arange(1765, 3235.5, 0.5)
        # t = np.arange(0, 5, 1)
        y = self.convertDectoHex()
        i = 0
        while i < 500:
            plt.clf()  # 清除上一幅图像
            # plt.plot(t, y)
            plt.plot(i, i ** 2)
            # plt.pause(0.2)
            i = i + 1
            plt.show()
            plt.ioff()  # 关闭画图的窗口

if __name__ == '__main__':
    m = InstrumentVisal()
    # m.convertDectoHex()
    m.picture_show()


