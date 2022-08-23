#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import win32com.client
#数据分析报告
def ConvertByWps(sourceFile, targetFile):
    """做一些异常情况的处理"""
    if not os.path.exists(sourceFile):
        print(sourceFile + "不存在，无法继续！")
        return False
    typemap = {
        'doc': 'word',
        'docx': 'word',
        'ppt': 'ppt',
        'pptx': 'ppt',
        'xls': 'excel',
        'xlsx': 'excel',
    }
    name_arr = sourceFile.split(".")
    suffix = name_arr[len(name_arr) - 1]
    wpstype = typemap.get(suffix)

    if (wpstype is None):
        return False

    os.system('taskkill /im wps.exe')  # 使用wps文档的方式进行处理
    # 如果文件存在就删除
    if os.path.exists(targetFile):
        os.remove(targetFile)
    if wpstype == 'word':
        ConvertDocToPdf(sourceFile, targetFile)
    elif wpstype == 'ppt':
        ConvertPptToPdf(sourceFile, targetFile)
    elif wpstype == 'excel':
        ConvertXlsToPdf(sourceFile, targetFile)
    if os.path.exists(targetFile):
        return True
    else:
        return False


"""真正的转化过程"""
# 转换 Word文件档到pdf
def ConvertDocToPdf(src, dst):
    wps = win32com.client.Dispatch("Kwps.Application")
    wps.Visible = False
    doc = wps.Documents.Open(src)
    doc.ExportAsFixedFormat(dst, 17)
    doc.Close()
    wps.Quit()


# 转换 PPT文件档到pdf
def ConvertPptToPdf(src, dst):
    wps = win32com.client.Dispatch("Kwpp.Application")
    wps.Visible = False
    ppt = wps.Presentations.Open(src)
    ppt.SaveAs(dst, 32)
    ppt.Close()
    wps.Quit()


# 转换 XLS文件档到pdf
def ConvertXlsToPdf(src, dst):
    wps = win32com.client.Dispatch("Ket.Application")
    excel = wps.Workbooks.Open(src)
    excel.ExportAsFixedFormat(0, dst)
    excel.Close()
    wps.Quit()


if __name__ == '__main__':
    # 当前目录
    d = os.path.dirname(__file__)
    abspath = os.path.abspath(d)

    # 测试用例-docx文件
    src = r"F:/test.docx"
    dst = r"F:/test.pdf"
    r = ConvertByWps(src, dst)
    print(r)

    # 测试用例-excel文件
    src = r"F:/test.docx"
    dst = r"F:/test.pdf"
    r = ConvertByWps(src, dst)
    print(r)

    # # 测试用例
    # src = abspath + r"/Doc/test.docx"
    # dst = abspath + r"/Doc/test.pdf"
    # r = ConvertByWps(src, dst)
    # print(r)

