# -*- coding: utf-8 -*-

' main test module '

__author__ = 'Jack Sun'

import unittest
import logging

from wrapper import selenium_wrapper
from util import xlsx_loader
from const import const


class BaseCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(BaseCase, self).__init__(methodName)
    #     self.param = param
    #
    # @staticmethod
    # def parametrize(testcase_klass, param=None):
    #     testloader = unittest.TestLoader()
    #     testnames = testloader.getTestCaseNames(testcase_klass)
    #     suite = unittest.TestSuite()
    #     for name in testnames:
    #         if name != const.BASIC_METHOD_NAME:
    #             suite.addTest(testcase_klass(name, param=param))
    #     return suite

class TestCase(BaseCase):

    def setUp(self):
        currentEnvDetail = xlsx_loader.xlsxProsser(self.param[const.PARAM_ENV], const.ENVSHEETNAME)
        selenium_wrapper.driverSet(currentEnvDetail[0][const.DRIVER_TYPE], self, currentEnvDetail[0][const.DRIVER_PATH])
        self.envDetail = currentEnvDetail

    def test_qbao(self):
        # excuteTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # try:
            currentTestCase = xlsx_loader.xlsxProsser(self.param[const.PARAM_CASE], const.CASESHEETNAME)
            self.driver.get(self.envDetail[0][const.START_ENV])
            for eachTestAction in currentTestCase:
                selenium_wrapper.entranceSeq(eachTestAction, self)
        # except Exception as e:
            # logging.exception(e)

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    def getTestFunc():
        def func(self):
            self.test_qbao()
        return func


if __name__ == '__main__':
    unittest.main()


