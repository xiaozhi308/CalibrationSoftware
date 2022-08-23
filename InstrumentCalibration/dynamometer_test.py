"""仪器测试板块"""
from CalibrationSoftware.public_class import PublicClass


class DynamiteTest(PublicClass):

    def __init__(self):
        super(DynamiteTest, self).__init__()


    def my_e4418b_test(self):
        """安捷伦E4418B功率计"""
        m4 = self.my_E4418A.write("FREQ:CW 200MHZ")
        # m1 = self.my_E4418A.query("READ? ")
        m2 = self.my_E4418A.query("FETC?")  # 查询当前功率测得值
        # m3 = self.my_E4418A.query("MEAS?")  # 设置当前连续波频点
        print(m2)

    def my_8648d_test(self):
        """安捷伦8648D"""
        # m1 = self.my_8648D.write("FREQ:CW 500MHZ")
        m2 = self.my_8648D.write("POW:AMPL -10DBM")  # 设置输出功率
        m4 = self.my_8648D.write("FREQ:CW 500MHZ")  # 设置输出频率
        m3 = self.my_8648D.write("OUTP:STAT ON")  # 设置输出开启关闭

        print(m2, m3, m4)

    def my_33220a_sine_test(self):
        """安捷伦33220A正弦波采集"""
        m1 = self.my_34401a.write("FUNC SIN")  # 设置输出功率
        m2 = self.my_34401a.write("FREQ 200")  # 设置输出频率
        m3 = self.my_34401a.write("VOLT 3")  # 设置输出开启关闭
        m4 = self.my_34401a.write("VOLT:OFFS 1")  # 设置输出开启关闭
        m5 = self.my_34401a.write("OUTP ON")  # 设置输出开启关闭
        print(m1, m2, m3, m4, m5)


    def my_33220a_square_test(self):
        """安捷伦33220A方波采集"""
        m10 = self.my_34401a.write("FUNC PULS")  # 设置输出功率
        m11 = self.my_34401a.write("FREQ 200")  # 设置输出频率
        m12 = self.my_34401a.write("VOLT 3")  # 设置输出开启关闭
        m13 = self.my_34401a.write("VOLT:OFFS 1")  # 设置输出开启关闭
        m14 = self.my_34401a.write("OUTP ON")  # 设置输出开启关闭
        print(m10, m11, m12, m13, m14)

    def my_dso6052a_test(self):
        self.my_dso6052a.write("WAV:FORM ASCII")
        my_dso6052a_result = self.my_dso6052a.query("WAVEFORM:DATA?")
        print(my_dso6052a_result)
        my_dso6052a_str_result = self.data_str_handle(my_dso6052a_result)
        print(my_dso6052a_str_result)
        self.data_collection(my_dso6052a_result)


if __name__ == '__main__':
    m = DynamiteTest()
    return_result = m.my_33220a_sine_test()
    return_result = m.my_33220a_square_test()
    return_result_two = m.my_dso6052a_test()






