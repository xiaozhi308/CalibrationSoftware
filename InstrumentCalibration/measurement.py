"""

测量类

"""

from PyQt5.QtWidgets import *
from CalibrationSoftware.public_class import PublicClass


class Measurement(PublicClass):
    def __init__(self):
        super(Measurement, self).__init__()

    def pop_up_warning(self):
        """
        弹窗警告!!!!！!
        现在存在的问题：弹窗一直没有退出，是为啥?是进程的问题吗？是msg_box的问题吗？
        """
        print("未查询到设备,请退出校准程序，感谢您的使用！")
        # reply = QMessageBox.question(self, u'警告', u'确认退出?', QMessageBox.Yes,
        #                                        QMessageBox.No)
        # if reply == QMessageBox.Yes:
        #     event.accept()  # 关闭窗口
        # else:
        #     event.ignore()  # 忽视点击X事件

        # reply = QMessageBox.warning(None, '警告', '这是警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # if
        # QMessageBox.warning(self, '警告', '这是警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # msg_box = QMessageBox()
        msg_box = QMessageBox(QMessageBox.Warning, '警告', '未查询到设备,请退出校准程序，感谢您的使用！')
        msg_box.exec_()

    def my_e3632a_test(self):
        """
        安捷伦E3632设备测试
        """
        return_verify_str = self.my_e3632a.query("*IDN?")
        verify_str = "E3632"
        if verify_str in return_verify_str:
            self.status = 1
        else:
            self.pop_up_warning()
            return "安捷伦E3632设备异常"
            
    def my_34401a_test(self):
        """
        安捷伦34401设备测试
        """
        return_verify_str = self.my_34401a.query("*IDN?")
        verify_str = "34401A"
        if verify_str in return_verify_str:
            self.status = 2
        else:
            self.pop_up_warning()
            return "安捷伦34401设备异常"
            
    def my_ca3xx_test(self):
        """
        电流分析仪CA3XX设备测试
        """
        return_verify_str = self.my_ca3xx.query("*IDN?")  # int类型转化成字符串的类型
        verify_str = "CA"
        if verify_str in return_verify_str:
            self.status = 3
        else:
            self.pop_up_warning()
            
    def my_vrmod_test(self):
        """
        可变电阻模块VRNOD设备测试
        """
        return_verify_str = self.my_vrmod.query("*IDN?")
        verify_str = "VR"
        if verify_str in return_verify_str:
            self.status = 5
            self.begin = 0
            self.my_34401a.query("MEAS:CURR:DC?")
        else:
            self.pop_up_warning()
            return "可变电阻模块VRNOD设备"
            
    def device_verification(self):
        """
        设备验证
        """
        while self.begin:
            if self.status == 0:
                self.my_e3632a_test()
                print("安捷伦E3632设备无误，可正常通信")
            elif self.status == 1:
                self.my_34401a_test()
                print("安捷伦34401设备无误，可正常通信")
            elif self.status == 2:
                self.my_ca3xx_test()
                print("电流分析仪CA3XX设备无误，可正常通信")
            elif self.status == 3:
                self.my_vrmod_test()
                print("可变电阻模块VRNOD设备无误，可正常通信")
        return_str = "安捷伦E3632设备无误，可正常通信\n\n"\
                     "安捷伦34401设备无误，可正常通信\n\n"\
                     "电流分析仪CA3XX设备无误，可正常通信\n\n"\
                     "可变电阻模块VRNOD设备无误，可正常通信"
        return return_str


if __name__ == '__main__':
    m = Measurement()
    return_result = m.device_verification()






