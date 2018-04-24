# -*- coding: utf-8 -*-

' main test module '

__author__ = 'Jack Sun'

from wrapper import ut_wrapper
from util import file_loader
from const import const

import HtmlTestRunner
import unittest


def startUiTest():

    #主入口，创建测试集合
    suite = unittest.TestSuite()

    # 组装自定义的测试类
    orgEnvDetail = file_loader.envProsser()
    envFilePath = const.ENVPATH + orgEnvDetail[0]
    filePath = file_loader.caseProsser()
    for eachCaseFilePath in filePath:
        setattr(ut_wrapper.TestCase, 'test_UiAuto_%s' % eachCaseFilePath, ut_wrapper.TestCase.getTestFunc())
        # suite = ut_wrapper.BaseCase.parametrize(ut_wrapper.TestCase, param=preParament)

    # 加载测试方法
    testloader = unittest.TestLoader()
    testnames = testloader.getTestCaseNames(ut_wrapper.TestCase)

    # 按测试方法生产测试对象
    for eachTestName in testnames:
        if eachTestName != const.BASIC_METHOD_NAME:
            eachCase = ut_wrapper.TestCase(eachTestName)
            preParament = {}
            filePath = eachTestName.split("_")[2]
            preParament[const.PARAM_CASE] = const.CASEPATH + filePath
            preParament[const.PARAM_ENV] = envFilePath
            # 每个测试实例传参
            setattr(eachCase, "param", preParament)
            # 将测试实例加入测试集合
            suite.addTest(eachCase)

    # 设置HTML报告
    runner = HtmlTestRunner.HTMLTestRunner(const.REPORT_FOLDERNAME, report_title="ui_auto")

    # 开始执行测试集合
    runner.run(suite)
    # suite.addTest(ut_wrapper.BaseCase('setUp')
    # unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    startUiTest()
