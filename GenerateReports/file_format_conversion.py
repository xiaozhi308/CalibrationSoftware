"""实现文件格式的转化"""

import os
from win32com.client import DispatchEx, Dispatch, constants, gencache

class FileFormatConversion:

    def __int__(self):
        pass

    def excel_pdf(self):
        """Excel转化成pdf文件"""
        excel_path = "F:/test.xlsx"  # 这里是Excel文件的路径
        pdf_path = "F:/2.pdf"  # 这里是输出PDF的保存路径

        #出错的原因是没有安装最新版的office或者是wps的问题！！！！！！！！！！
        xlApp = DispatchEx("Ket.Application")
        xlApp.Visible = False
        xlApp.DisplayAlerts = 0
        books = xlApp.Workbooks.Open(excel_path, False)
        books.ExportAsFixedFormat(0, pdf_path)
        books.Close(False)
        xlApp.Quit()

    def word_pdf(self, word_file, pdf_file):
        """word转化成pdf文件"""
        # 出错的原因是没有安装最新版的office或者是wps的问题！！！！！！！！！！
        new_word_file = word_file
        new_pdf_file = pdf_file
        word = Dispatch('Kwps.Application')
        doc = word.Documents.Open(new_word_file)
        doc.SaveAs(new_pdf_file, FileFormat=17)
        doc.Close()
        word.Quit()


if __name__ == '__main__':
    #测试用例
    word_file = r"F:\test.xlsx"
    pdf_file = r"F:\testxlsx.pdf"
    m = FileFormatConversion()
    print(m.word_pdf(word_file, pdf_file))