# -*- coding: utf-8 -*-

' reference wrapper module '

__author__ = 'Jack Sun'

from util import xlsx_loader
from const import const

# 处理引用用例
def refenceProsser(refPath):
    return xlsx_loader.xlsxProsser(refPath, const.CASESHEETNAME)


if __name__ == '__main__':
    refenceProsser()