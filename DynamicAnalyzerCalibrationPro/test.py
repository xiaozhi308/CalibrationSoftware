
class test:
    def __init__(self):
        self.set_value = 0
        self.beign_number = 90  # 循环板块
        self.stander = 100   # 标准

    #第二步
    def my_e3632a_configure(self):
        self.my_e3632.write("OUTP OFF")
        self.my_e3632.write("VOLT:RANG P15V")
        self.my_e3632.write("VOLT:PROT 10")
        self.my_e3632.write("VOLT:PROT:STAT ON")
        self.my_e3632.write("CURR:PROT 2.5")
        self.my_e3632.write("CURR:PROT:STAT ON")

    #循环部分的逻辑判断
    def logical_judgment(self):
        self.my_e3632a_configure()
        my_cx3_begin_result = self.my_cx3.write("AT+CAIL START=2")
        if my_cx3_begin_result == "OK":
            while self.begin < self.stander:
                my_e3632_result_int = self.my_e3632_judge()
                while  -0.5 + self.set_value < my_e3632_result_int < 0.5 + self.set_value:
                    self.my_e3632.write("OUTP ON")
                    my_34401_cx3_result = self.my_34401_judgment()
                    if my_34401_cx3_result == "CAIL-OK":
                        self.my_e3632_judge()
                    else:
                        self.logical_judgment()
        elif my_cx3_begin_result == "ALLOK":
            print("设备已经校准")
            self.my_cx3.query("AT+CAIL_DATA=2?")


    def my_e3632_judge(self):
        #设定值
        self.my_e3632.write("VOLT " + self.set_value)
        my_e3632_result = self.my_e3632.query("MEAS:VOLT?")
        return my_e3632_result

    def my_34401_cx3_judgment(self):
        #平均值
        my_34401_average_result = self.my_34401.write("MEAS:CURR:DC?")
        my_cx3_result = self.my_cx3.write("AT+CAIL COEFF="+ my_34401_average_result)
        return my_cx3_result

    def my_cx3_over(self):
        my_cx3_over_result = self.my_cx3.write("AT+CAIL OVER2")
        if my_cx3_over_result == "ALL-OK":
            self.my_cx3.query("AT+CAIL_DATA=2?")
            print("校准成功")
