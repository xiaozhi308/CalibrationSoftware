"""测试单元"""
import profile
from pyinstrument import Profiler

class Performance_Testing:

    def instrument_test_unit(self):
        # 把结果写到日志中
        profile.run("m.my_33220a_square_test()", "testprof")
        profile.run("m.my_dso6052a_test()", "testprof")
        # profile.run("profileTest()","testprof")
        # profile.run(“profileTest()”, ”testprof”)
        # profile.run(return_result_two)


if __name__ == '__main__':
    profile = Profiler()
    profile.start()
    profile.stop()
    profile.print()