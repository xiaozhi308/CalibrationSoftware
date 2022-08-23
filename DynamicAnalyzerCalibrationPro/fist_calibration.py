import sys

from CalibrationSoftware.public_class import PublicClass
import numpy as np
import time
import tkinter as tk
from tkinter import LEFT

class Test(PublicClass):
    standard = 90
    err_count = 0
    my_ca3xx_number = 0
    sio_number = 1
    result_str = ""
    list_range = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49,
                           128, 206, 284, 362, 440, 518, 596, 674, 752, 830, 908, 986, 1064, 1142, 1220, 1298, 1376, 1454, 1532, 1610, 1688, 1766, 1844, 1922, 2000,
                           5.12, 8.24, 11.36, 14.48, 17.6, 20.72, 23.84, 26.96, 30.08, 33.2, 36.32, 39.44, 42.56, 45.68, 48.8, 51.92, 55.04, 58.16, 61.28, 64.4, 67.52, 70.64, 73.76, 76.88, 80,
                           88, 96, 104, 112, 120, 128, 136, 144, 152, 160, 168, 176, 184, 192, 200]

    def __int__(self, standard, err_count, my_ca3xx_number, sio_number, list_range,result_str):
        self.standard = standard
        self.err_count = err_count
        self.my_ca3xx_number = my_ca3xx_number
        self.list_range = list_range  # sio的数据,量程
        self.result_str = result_str  # 返回的信息

    def my_adcmt_6146_query(self):
        # result = self.my_adcmt_6146.query("*IDN?")
        result = "GPIB0::6::INSTR"
        return result

    def my_ca3xx_query(self):
        # result = self.my_ca3xx.query("*IDN?")
        result = "ASRL3::INSTR"
        return result

    def my_34401_query(self):
        # result = self.my_34401a.query("*IDN?")
        result = "GPIB0::12::INSTR"
        return result

    def my_adcmt_6146_configure(self):
        """my_adcmt_6146的配置"""
        self.my_adcmt_6146.write("SBY")
        self.my_adcmt_6146.write("IF")
        self.my_adcmt_6146.write("SIRX1")

    def my_adcmt_6146_calibration(self):
        """my_adcmt_614开始校准"""
        my_ca3xx_start_result = self.my_ca3xx_start()
        if my_ca3xx_start_result == "ALLOK_1":
            self.my_ca3xx_start_allok()
        elif my_ca3xx_start_result == "OK":
            while self.my_ca3xx_number < self.standard:
                my_ca3xx_result = self.my_ca3xx_cnt(self.my_ca3xx_number)
                if my_ca3xx_result == "CNT-OK":
                    sio_number_str = str(self.list_range[self.my_ca3xx_number])
                    self.my_ca3xx_number = self.my_ca3xx_number + 1
                    # print(sio_number_str)
                    self.my_adcmt_6146.write("SOI" + sio_number_str +"E-6")
                    my_ca3xx_finall_result_str = self.my_34401_send_myca3xx()
                    if my_ca3xx_finall_result_str == "CAIL-OK":
                        my_ca3xx_number_str = str(self.my_ca3xx_number)
                        self.result_str = "第" + my_ca3xx_number_str + "点已校准"
                        print(self.result_str)
                    else:
                        while self.err_count < 10:
                            self.my_34401_send_myca3xx()
                            self.err_count = self.err_count + 1
                        self.result_str = "添加错误计数，超过10次，退出校准"
                        sys.exit()
                else:
                    while self.err_count < 10:
                        self.my_ca3xx_send()
                        self.err_count = self.err_count + 1
                    self.result_str = "添加错误计数，超过10次，退出校准"
                    print()
                    sys.exit()
            self.my_ca3xx_over()
        else:
            self.result_str = "程序异常,退出程序"
        self.result_str = "设备校准完成"
        return self.result_str

    def my_ca3xx_start(self):
        result = self.my_ca3xx.query("AT+CAIL START=1?")
        my_ca3xx_str_result = self.str_handle(result)
        return my_ca3xx_str_result

    def my_ca3xx_start_allok(self):
        self.result_str = "设备已经校准"
        newresult = self.my_ca3xx.query("AT+CAIL_DATA?")
        return newresult

    def my_ca3xx_cnt(self, my_ca3xx_number):
        """电流分析仪的判断返回值"""
        self.my_adcmt_6146.write("OPR")
        my_ca3xx_str = str(my_ca3xx_number)
        my_ca3xx_result = self.my_ca3xx.query("AT+CAIL_CNT=" + my_ca3xx_str)
        my_ca3xx_result_str = self.str_handle(my_ca3xx_result)
        return my_ca3xx_result_str

    def my_ca3xx_over(self):
        my_ca3xx_over_result = self.my_ca3xx.query("AT+CAIL OVER1")
        my_ca3xx_over_result_str = self.str_handle(my_ca3xx_over_result)
        if my_ca3xx_over_result_str == "All-OK":
            self.my_ca3xx.query("AT+CAIL_DATA?")
            return "提交校准成功"
        else:
            return "提交校准失败"

    def my_34401_send_myca3xx(self):
        my_ca3xx_finall_result = self.my_34401_calculate()
        my_ca3xx_finall_result_float = self.scientific_notation_handle(my_ca3xx_finall_result) * 1000
        my_ca3xx_finall_result_str = str(my_ca3xx_finall_result_float)
        my_ca3xx_finall_result = self.my_ca3xx.query("AT+CAIL COEFF=" + my_ca3xx_finall_result_str)
        my_ca3xx_finall_result_str = self.str_handle(my_ca3xx_finall_result)
        return my_ca3xx_finall_result_str

    def my_34401_calculate(self):
        """34401计算平均数"""
        my_34401a_one = self.my_34401a.query("MEAS:CURR:DC?")
        my_34401a_two = self.my_34401a.query("MEAS:CURR:DC?")
        my_34401a_three = self.my_34401a.query("MEAS:CURR:DC?")
        finall_result_one = self.scientific_notation_int(my_34401a_one)
        finall_result_two = self.scientific_notation_int(my_34401a_two)
        finall_result_three = self.scientific_notation_int(my_34401a_three)
        finall_result = (finall_result_one + finall_result_two + finall_result_three) / 3

        return finall_result

    def my_ca3xx_clear(self):
        self.my_ca3xx.query("CAIL-RESET?")
        self.result_str = "设备已清除"
        return self.result_str

if __name__ == '__main__':
    #初始化
    m = Test()
    root = tk.Tk()
    root.geometry('600x400')
    root.title("动态分析仪校准程序")
    on_hit = False

    #函数

    def my_adcmt_6146_show(my_adcmt_6146_value):
        my_adcmt_6146_var.set(my_adcmt_6146_value)


    def my_34401a_show(my_34401a_value):
        my_34401a_var.set(my_34401a_value)


    def my_ca3xx_show(my_ca3xx_value):
        my_ca3xx_var.set(my_ca3xx_value)

    def interface_query():
        #接口查询
        # 接受值
        my_adcmt_6146_show(m.my_adcmt_6146_query())
        my_34401a_show(m.my_34401_query())
        my_ca3xx_show(m.my_ca3xx_query())

    def begin():
        global on_hit
        if on_hit == False:
            t = time.time()
            """要执行的代码块"""
            m.my_adcmt_6146_configure()
            result = m.my_adcmt_6146_calibration()
            spend_time = f'coast:{time.time() - t:.4f}s'
            var.set("{result}\n \n 花费时间为：{time}".format(result=result,time=spend_time))
        else:
            on_hit = False
            var.set("加载失败，请重新启动")


    def re_begin():
        m.my_ca3xx_clear()
        var.set("设备已清除校准")


    # def stop_calibration():
    #程序暂停,先搁置
    #     sys.exit()

    #几个模块
    frame1 = tk.Frame(root,  height = 20, width = 600)
    frame2 = tk.Frame(root,  height = 20, width = 600)
    frame3 = tk.Frame(root,  height = 20, width = 600)
    frame4 = tk.Frame(root,  height = 20, width = 600)

    frame1.pack(padx=10, pady=10)
    frame2.pack(padx=10, pady=10)
    frame3.pack(padx=10, pady=10)
    frame4.pack(padx=10, pady=10)

    label = tk.Label(frame1, text="ADCMT 6146 :  ", justify=LEFT, font=("Times",15))
    label.pack(side=LEFT)
    label = tk.Label(frame2, text="HEWLETT PACKARD 34401a :  ", justify=LEFT, font=("Times", 15))
    label.pack(side=LEFT)
    label = tk.Label(frame3, text="动态电流分析仪 :   ", justify=LEFT, font=("Times", 15))
    label.pack(side=LEFT)

    # 显示标签
    my_adcmt_6146_var = tk.StringVar()
    my_34401a_var = tk.StringVar()
    my_ca3xx_var = tk.StringVar()

    my_adcmt_6146_label = tk.Label(frame1, text="GPIB", justify=LEFT, textvariable=my_adcmt_6146_var)
    my_adcmt_6146_label.pack(side=LEFT)

    my_34401a_label = tk.Label(frame2, text="GPIB", justify=LEFT, textvariable=my_34401a_var)
    my_34401a_label.pack(side=LEFT)

    my_ca3xx_label = tk.Label(frame3, text="GPIB", justify=LEFT, textvariable=my_ca3xx_var)
    my_ca3xx_label.pack(side=LEFT)

    b = tk.Button(frame4, text='开始校准', font=('Arial', 12), width=10, height=1, command=begin)
    b.pack(side=LEFT)

    b = tk.Button(frame4, text='清除校准', font=('Arial', 12), width=10, height=1, command=re_begin)
    b.pack(side=LEFT)

    b = tk.Button(frame4, text='接口查询', font=('Arial', 12), width=10, height=1, command=interface_query)
    b.pack(side=LEFT)

    var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
    l = tk.Label(root, textvariable=var, bg='grey', fg='white', font=('Arial', 12), width=60, height=10)
    l.pack()

    root.mainloop()





