
"""数据采集"""
from CalibrationSoftware.public_class import PublicClass
import time


class DataCollection(PublicClass):
    def __int__(self):
        super(DataCollection, self).__int__()

    def custom_data(self):
        """自定义数据源"""
        form_data_list = [x for x in range(-6, -1, 2)]  # 列表生成式
        datas = []
        for i in form_data_list:
            form_data = i
            form_data_str = str(form_data)
            for j in range(1, 2500+1):
                my_e4418a_intnumber = j
                my_8648d_str_number = str(my_e4418a_intnumber)
                self.my_E4418A.write("FREQ:CW " + my_8648d_str_number + "MHZ")
                self.my_8648D.write("FREQ:CW " + my_8648d_str_number + "MHZ")
                self.my_8648D.write("POW:AMPL " + form_data_str + "DBM")
                self.my_8648D.write("OUTP:STAT ON")
                my_8648d_mysql_data = self.my_E4418A.query("FETC?")
                my_8648d_mysql_data_fin = self.scientific_notation_int(my_8648d_mysql_data)
                error_data = self.error_value_calculation(form_data, my_8648d_mysql_data_fin)
                tuple_data = [my_e4418a_intnumber, my_8648d_mysql_data_fin, my_e4418a_intnumber, form_data, error_data]
                datas.append(tuple_data)  # 数据存储
                output_string = "生成数据:{}   校准数据:{}  频率:{}   幅值:{}   误差数据:{}".format(my_e4418a_intnumber, my_8648d_mysql_data_fin, my_e4418a_intnumber, form_data, error_data)
                print(output_string)
            file_name_str = str(i)
            file_path = r'G:\pycharm_project\CalibrationSoftware\Datasave\Mhz' + file_name_str + '.csv'
            self.data_collection_csv(datas, file_path)
            datas.clear()
            print("{}储存成功".format(i))
            print("------------------")
        return datas


if __name__ == '__main__':
    m = DataCollection()
    print("MHZ-10")
    print("---------------------------------------------")
    m.custom_data()

