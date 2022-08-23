"""数据存储成CSV文件"""
from CalibrationSoftware.DataHandle.data_collection import DataCollection
import time


class DataSave(DataCollection):
    def __int__(self,):
        super().__int__()

    def my_mhz_save(self):
        """mhz10保存csv格式"""
        datas = self.custom_data()
        form_data_list_new = [x for x in range(-6, -1, 2)]
        for i in form_data_list_new:
            file_name_str = str(i)
            file_path = r'G:\pycharm_project\CalibrationSoftware\Datasave\Mhz' + file_name_str + '.csv'
            self.data_collection_csv(datas, file_path)
            print("{}储存成功".format(i))


if __name__ == '__main__':
    m = DataSave()
    time_start = time.time()