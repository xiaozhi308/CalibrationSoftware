"""

开始校准

"""
from CalibrationSoftware.public_class import PublicClass


class BeginCalibration(PublicClass):
    def __init__(self):
        super(BeginCalibration, self).__init__()

    def my_e3632a_ready_calibration(self):
        """
        安捷伦E3632设备准备校准
        """
        self.my_e3632a.write("OUTP ON")  # 输出开启
        print("安捷伦E3632准备校准完成")

    def my_ca3xx_ready_calibration(self):
        """
         ca3xx_设备准备校准
        """
        my_ca3xx_result = self.my_ca3xx.query("C3X?")  # 清除过流保护
        handle_result = self.str_handle(my_ca3xx_result)
        if handle_result == "ACK3X":
            print("电流分析仪准备校准完成")
            print("准备校准完成")
        else:
            self.exit_program()

    # 准备-2FX
    def my_ca3xx_ready_calibration_two(self):
        """
           电流分析仪CA3XX设备准备校准
        """
        my_ca3xx_result = self.my_ca3xx.query("C2FX?")
        my_ca3xx_result_handle = self.str_handle(my_ca3xx_result)
        if my_ca3xx_result_handle == "ACK2FX":
            print("电流分析仪准备完成：准备-2FX准备完成")
        elif my_ca3xx_result_handle != "ACK2FX":
            pass

    # 校准-3x1
    def my_e3632a_begin_calibration(self):
        self.my_e3632a.write("OUTP ON")
        self.my_e3632a.write("VOLT 5.991")  # 清除过流保护
        result = self.my_e3632a.query("MEAS:VOLT?")
        new_result = float(result)
        if new_result < 5.8:
            self.exit_program()
        elif new_result >= 5.8:
            self.my_34401a_begin_calibration()

    def my_34401a_begin_calibration(self):
        """
            34401a设备开始校准
        """
        my_34401a_result = self.my_34401a.query("MEAS:CURR:DC?")
        self.my_ca3xx_begin_calibration(my_34401a_result)

    def my_ca3xx_begin_calibration(self, my_34401a_result):
        """
        电流分析仪CA3XX设备开始校准
        """
        result = my_34401a_result
        rs = self.my_ca3xx.query(result)
        handle_rs = self.str_handle(rs)
        # handle_rs = "1"
        if handle_rs != "OK-3X1":
            self.my_34401a_begin_calibration()
            print("ces")
        elif handle_rs == "OK-3X1":
            self.my_vrmod_begin_calibration()


    def my_vrmod_begin_calibration(self):
        """
          可变电阻模块VRNOD设备开始校准　　
        """
        result = self.my_vrmod.query("MCAIL-5?")
        handle_result = self.str_handle(result)
        if handle_result == "MOK-5":
            print("校准-3X1校准完成")
        else:
            print("可变电阻模块异常，退出校准程序")
            self.exit_program()

    # 校准-3x2
    def my_e3632a_begin_calibration_two(self):
        self.my_e3632a.write("VOLT 1.075")
        my_ca3xx_result = self.my_ca3xx.query("3X2?")
        my_ca3xx_result_handle = self.str_handle(my_ca3xx_result)
        if my_ca3xx_result_handle == "OK":
            my_e3632_result_voltage = self.my_e3632a.query("MEAS:VOLT?")  # 电压值
            my_e3632_result_voltage_handle = self.scientific_notation_handle(my_e3632_result_voltage)
            if my_e3632_result_voltage_handle >= 0.9:
                self.my_34401a_begin_calibration_two()
            elif my_e3632_result_voltage_handle < 0.9:
                #不清除要干嘛
                pass
        elif my_ca3xx_result_handle != "OK":
            pass

    def my_34401a_begin_calibration_two(self):
        """
            34401a设备开始校准
        """
        # 转化
        my_34401a_result_voltage = self.my_34401a.query("MEAS:CURR:DC?")
        my_ca3xx_result_return = self.my_ca3xx.query(my_34401a_result_voltage)
        my_ca3xx_result_return_convert = self.str_handle(my_ca3xx_result_return)
        if my_ca3xx_result_return_convert == "OK-3X2":
            print("标准-3X2校准完毕")
        elif my_ca3xx_result_return_convert != "OK-3X2":
            pass
        return my_34401a_result_voltage

    #校准-2FX1
    def my_e3632a_begin_calibration_three(self):
        self.my_e3632a.write("VOLT 1.954")
        my_e3632a_result = self.my_e3632a.query("MEAS:VOLT?")
        my_e3632a_result_convert = self.scientific_notation_handle(my_e3632a_result)
        if my_e3632a_result_convert > 1.8:
            self.my_34401a_begin_calibration_three()
        elif my_e3632a_result_convert <= 1.8:
            pass

    def my_34401a_begin_calibration_three(self):
        my_34401a_result = self.my_34401a.query("MEAS:CURR:DC?")
        my_ca3xx_return = self.my_ca3xx.query(my_34401a_result)
        my_ca3xx_return_convern = self.str_handle(my_ca3xx_return)
        if my_ca3xx_return_convern == "OK-2F1":
            print("校准-2FX1校准完成")
        elif my_ca3xx_return_convern != "OK-2F1":
            pass

    # 校准-2FX2
    def my_e3632a_begin_calibration_four(self):
        self.my_e3632a.write("VOLT 2.584")
        my_ca3xx_result = self.my_ca3xx.query("2F2?")
        my_e3632a_result_convert = self.str_handle(my_ca3xx_result)
        if my_e3632a_result_convert == "OK":
            my_e3632a_result = self.my_e3632a.query("MEAS:VOLT?")
            my_e3632a_result_convert_next = self.scientific_notation_handle(my_e3632a_result)
            if my_e3632a_result_convert_next > 2.4:
                end_result = self.my_34401a.query("MEAS:CURR:DC?")
                print("校准-2FX2校准完成")
        elif my_e3632a_result_convert != "OK":
            pass
    # @staticmethod
    # def calibration_finish(self):
    #     """
    #     校准完成
    #     """
    #     print("校准完成")

    def ready_calibration(self):
        """
        准备校准
        """
        self.my_e3632a_ready_calibration()
        self.my_ca3xx_ready_calibration()

    def begin_calibration_one(self):
        """
        开始校准
        """
        print("-----------------------")
        # 校准-3x1
        self.my_e3632a_begin_calibration()
        print("-----------------------")
        # 校准-3x2
        self.my_e3632a_begin_calibration_two()
        print("-----------------------")
        # 准备-2FX
        self.my_ca3xx_ready_calibration_two()
        print("-----------------------")
        # 校准-2FX1
        self.my_e3632a_begin_calibration_three()
        print("-----------------------")
        # 校准-2FX2
        self.my_e3632a_begin_calibration_four()



    # def device_verification(self):
    #     while self.begin == 1:
    #         if self.status == 0:
    #             self.my_3
    #     return "开始校准"



if __name__ == '__main__':
    m = BeginCalibration()
    # return_result = m.device_verification()
    return_result = m.ready_calibration()
    return_result2 = m.begin_calibration_one()
    # print(return_result)
    # print(return_result2)