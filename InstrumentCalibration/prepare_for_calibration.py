"""
准备校准
"""
from CalibrationSoftware.public_class import PublicClass
import sys


class PrepareCalibration(PublicClass):
    def __init__(self):
        super(PrepareCalibration, self).__init__()
        self.prompt_statement = " "  # 提示语句

    def my_e3632a_calibration(self):
        """
        安捷伦E3632设备准备校准
        """
        self.my_e3632a.write("OUTP OFF")  # 输出关闭
        self.my_e3632a.write("CURR:PROT:CLE")  # 清除过流保护
        self.my_e3632a.write("CURR:PROT 3")  # 设置过流保护为3A
        self.my_e3632a.write("CURR:PROT:STAT ON")  # 过流保护开启

    def my_ca3xx_calibration(self):
        """
        电流分析仪CA3XX设备测试
        """
        result = self.my_ca3xx.query("CS?")    # 查询设备的校准状态
        handle_result = str.strip(result)  # 字符串的处理
        # handle_result = "OK"
        if handle_result == "OK":
            self.status = 1
            print("电流分析仪CA3XX设备测试结果返回的是OK")
        elif handle_result == "ALLOK":
            print("电流分析仪CA3XX设备测试结果返回的是ALLOK,调用失败")
            self.exit_program()
        else:
            print("返回结果不正确")

    def my_vrmod_calibration(self):
        """
        可变电阻模块VRNOD设备准备校准
        """
        result = self.my_vrmod.query("MCAIL-6?")
        handle_result = str.strip(result)
        if handle_result == "MOK-6":
            self.prompt_statement = "可变电阻模块VRNOD设备准备完毕"
            print(self.prompt_statement)
        else:
            self.prompt_statement = "可变电阻模块异常，退出校准程序"
            self.exit_program()
        return self.prompt_statement

    def device_verification(self):
        while self.begin == 1:
            if self.status == 0:
                self.my_e3632a_calibration()
                print("安捷伦E3632设备准备完毕")
                self.my_ca3xx_calibration()
                print("电流分析仪CA3XX准备完毕")
            elif self.status == 1:
                self.my_vrmod_calibration()
                self.prepare_calibration_finish()
                self.exit_program()
            else:
                self.prompt_statement = "校准异常退出"
                self.begin = 2
                print(self.prompt_statement)


if __name__ == '__main__':
    m = PrepareCalibration()
    return_result = m.device_verification()