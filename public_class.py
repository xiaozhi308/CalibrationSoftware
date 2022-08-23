"""

公共类
配置

"""
import pyvisa
import sys
import math
import csv
import time


class PublicClass(Exception):

    def __init__(self):
        self.rm = pyvisa.ResourceManager()
        print(self.rm.list_resources())
        try:
            pass
            # self.my_e3632a = self.rm.open_resource('GPIB0::13::INSTR')
            # self.my_34401a = self.rm.open_resource('GPIB0::12::INSTR')
            # self.my_ca3xx = self.rm.open_resource('ASRL3::INSTR')
            self.my_spect = self.rm.open_resource("ASRL3::INSTR")

            # self.my_vrmod = self.rm.open_resource('ASRL8::INSTR')
            # self.my_E4418A = self.rm.open_resource("GPIB0::13::INSTR")
            # self.my_8648D = self.rm.open_resource("GPIB0::17::INSTR")
            # self.my_dso6052a = self.rm.open_resource("GPIB0::7::INSTR")
            # self.my_8648D = self.rm.open_resource('GPIB0::17::INSTR')
            # self.my_adcmt_6146 = self.rm.open_resource("GPIB0::6::INSTR")
            # self.status = 0
            # self.begin = 1
        except Exception as e:
            raise Exception("设备连接异常,请检查")


    def exit_program(self):
        """
        退出程序：新需求，不能全部退出整个程序，而是推出当前类
        """
        sys.exit(0)

    def prepare_calibration_finish(self):
        """
        准备校准完成
        """
        print("准备校准完成")

    def str_handle(self, processed_str):
        """
        字符串的处理
        """
        handle_result = str.strip(processed_str)
        return handle_result

    def scientific_notation_handle(self, processed_number):
        """
        科学计数法的处理:转化成浮点数
        """
        handle_result = float(processed_number)
        return handle_result

    def data_collection(self, processed_result):
        """数据采集txt文件"""
        with open("test.txt", "w") as f:
            f.write(processed_result)

    def data_collection_csv(self, data, file_path):
        new_file_path = file_path
        with open(new_file_path, 'w', encoding="utf-8-sig", newline="") as f:
            csv_writer = csv.writer(f, dialect="excel")
            #名字后期也可以封装一下
            csv_writer.writerow(["生成数据", "校准数据", "频率", "幅值", "误差数据"])
            for i in data:
                csv_writer.writerow(i)
        f.close()
        print("存储完毕")

    def data_str_handle(self, processed_data_str):
        """数据字符串的处理"""
        result_number_one = processed_data_str.lstrip("#800012999")  # 删除某个字符串中的字符
        result_number = self.scientific_notation_handle(result_number_one)
        return result_number

    def scientific_notation_int(self, data):
        """科学计数法的数据处理成int类型"""
        before_e = float(data.split('E')[0])
        sign = data.split('E')[1][:1]
        after_e = int(data.split('E')[1][1:])
        if sign == '+':
            float_num = before_e * math.pow(10, after_e)
        elif sign == '-':
            float_num = before_e * math.pow(10, -after_e)
        else:
            float_num = None
            print('error: unknown sign')
        return float_num

    def error_value_calculation(self, subtraction_data, minuend_data):
        """相对误差值计算"""
        subtraction = subtraction_data
        minuend = minuend_data
        fin_result = (subtraction - minuend) / minuend
        return fin_result

    def printf(self, mes):
        """显示内容到textBrowser"""
        self.textBrowser.append(mes)
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)

    def loaddataset(self):
        """将txt中的数据按照固定格式输出"""
        dataset = []
        infile = 'G:\pycharm_project\CalibrationSoftware\\test.txt'
        f = open(infile, 'r')
        sourceInLine = f.readlines()
        for line in sourceInLine:
            temp1 = line.strip('\n')
            print(temp1, end=", ")
            # dataset.append(temp1)
        return dataset
    def time_difference(self,to_be_tested):
        """计算函数的时间差,待测试的物体"""
        t = time.time()
        print(f'coast:{time.time() - t:.4f}s')

if __name__ == '__main__':
    m = PublicClass()
    # m.time_difference(m.printf())
    m.loaddataset()
