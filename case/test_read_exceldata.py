# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 14:57
# @Author  : lishanshan

import os
import time
import unittest
curpath = os.path.dirname(os.path.realpath(__file__))
import xlrd
from ddt import ddt, data
from common import HTMLTestRunner
def excel_data():
    data_path=curpath + r'\data\case.xlsx'
    file = xlrd.open_workbook(data_path)
    sheet = file.sheets()[0]  # sheet[0]打开第一个sheet页面
    nrows = sheet.nrows  # 获取行数
    case_list = [
        {'case_name': sheet.cell(i, 0).value, 'input_1': sheet.cell(i, 1).value, 'input_2': sheet.cell(i, 2).value} for
        i in range(1, nrows)]
    return case_list
    return case_list

case_list=excel_data()
@ddt
class Testexcel(unittest.TestCase):
    def setUp(self):
        pass

    @data(*case_list)
    def test_jiafa(self, a):
        SJ=int(a['input_1'])+int(a['input_2'])
        YQ=10
        self.assertEqual(SJ, YQ)

if __name__=='__main__':
    unittest.main()
