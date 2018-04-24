# -*- coding: utf-8 -*-

' selenium wrapper module '

__author__ = 'Jack Sun'

import logging
import time
from selenium import webdriver
from const import const
from util.ref_loader import refenceProsser


# 主调用入口，按条执行case的内容
def entranceSeq(excelAction, self):
    element = findElement(excelAction, self)
    excuteAction(excelAction, element, self)

# 指定驱动
def driverSet(driverType, self, driverPath):
    if driverType == const.DRIVER_TYPE_CHROME:
        if driverPath is not None :
            self.driver = webdriver.Chrome(executable_path=driverPath)
        else:
            self.driver = webdriver.Chrome(executable_path=const.CHROME_DRIVER_PATH)
    elif driverType == const.DRIVER_TYPE_FIREFOX:
        if driverPath is not None:
            self.driver = webdriver.Firefox(executable_path=driverPath)
        else:
            self.driver = webdriver.Firefox(executable_path=const.FIREFOX_DRIVER_PATH)
    elif driverType == const.DRIVER_TYPE_IE:
        if driverPath is not None:
            self.driver = webdriver.Firefox(executable_path=driverPath)
        else:
            self.driver = webdriver.Firefox(executable_path=const.IE_DRIVER_PATH)

# 锁定DOM
def findElement(eachExcelAction, self):
    if eachExcelAction[const.ELEMENT] is not None:
        try:
            if eachExcelAction[const.IDTYPE] == const.IDTYPE_ID:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_NAME:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_CLASS_NAME:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_TAG_NAME:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_LINK_TEXT:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_PARTIAL_LINK_TEXT:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_XPATH:
                foundElement = self.driver.find_element_by_xpath(eachExcelAction[const.ELEMENT])
                return foundElement
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_CSS_SELECTOR:
                pass
            elif eachExcelAction[const.IDTYPE] == const.IDTYPE_REFERENCE:
                refActionList = refenceProsser(eachExcelAction[const.ELEMENT])
                for eachRefAction in refActionList:
                    refElement = findElement(eachRefAction, self)
                    excuteAction(eachRefAction, refElement, self)
        except Exception as e:
            logging.exception(e)
    else:
        logging.exception('Missing element column' + eachExcelAction[const.DESCRIPTION])

# 对DOM进行操作
def excuteAction(eachExcelAction, element, self):
    if eachExcelAction[const.IDTYPE] != const.IDTYPE_REFERENCE and element is None:
        logging.exception('No element has been find, detail: ' + eachExcelAction[const.ELEMENT])
    else:
        # try:
            if eachExcelAction[const.ACTION] == const.ACTION_KEYIN and eachExcelAction[const.VALUE]:
                element.send_keys(eachExcelAction[const.VALUE])
            elif eachExcelAction[const.ACTION] == const.ACTION_CLICK:
                element.click()
                time.sleep(3)
            elif eachExcelAction[const.ACTION] == const.ACTION_ASSERT:
                assertAction(eachExcelAction, element, self)
        # except Exception as e:
            # logging.exception(e)

def assertAction(eachExcelAction, element, self):
    if eachExcelAction[const.ASSERT_ELEMENT_TYPE] == const.ELEMENT_TYPE_TABLE:
        allRow = element.find_elements_by_tag_name(const.ELEMENT_TYPE_TR)

        targetRow = allRow[eachExcelAction[const.ASSERT_T_ROW]]

        textDetail = targetRow.text.split("\n")

        self.assertEqual(textDetail[eachExcelAction[const.ASSERT_T_COLUMN]], eachExcelAction[const.ASSERT_EXPERT],
                             msg="Assert Fail! Please check:"+eachExcelAction[const.DESCRIPTION]+" 期望---"
                                 +eachExcelAction[const.ASSERT_EXPERT]+" 实际---"+textDetail[eachExcelAction[const.ASSERT_T_COLUMN]])

    elif eachExcelAction[const.ASSERT_ELEMENT_TYPE] == const.ELEMENT_TYPE_TEXT:
        orgVale = element.text
        self.assertEqual(orgVale, eachExcelAction[const.ASSERT_EXPERT],
                         msg="Assert Fail! Please check:" + eachExcelAction[const.DESCRIPTION] + " 期望---"
                             + eachExcelAction[const.ASSERT_EXPERT] + " 实际---" + orgVale)