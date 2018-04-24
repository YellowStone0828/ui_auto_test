# -*- coding: utf-8 -*-

' file load module '

__author__ = 'Jack Sun'

import os
import logging
from const import const


# 处理文件目录，将文件名的列表返回
def filePathProsser(Path):
    filePathResult = []
    try:
        for eachCase in os.listdir(Path):
            # 忽略mac自带的详细信息文件
            if eachCase != ".DS_Store" :
                filePathResult.append(eachCase)
        #print(filePathResult)
        return filePathResult
    except Exception as e:
        logging.exception(e)

# 处理环境
def envProsser():
    result = filePathProsser(const.ENVPATH)
    return result

# 处理用例
def caseProsser():
    result = filePathProsser(const.CASEPATH)
    return result


if __name__ == '__main__':
    filePathProsser()