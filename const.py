# -*- coding: utf-8 -*-

' file load module '

__author__ = 'Jack Sun'

# 常量类
class _const:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value):
      if name in self.__dict__:
          raise self.ConstError("can't change const %s" % name)
      if not name.isupper():
          raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
      self.__dict__[name] = value

const = _const()

const.ENVPATH = "./envs/"
const.ENVSHEETNAME = "env"
const.CASEPATH = "./cases/test/"
const.CASESHEETNAME = "case"

const.PARAM_ENV = "envPath"
const.PARAM_CASE = "casePath"

const.DESCRIPTION = "Description"
const.DRIVER_TYPE = "Driver_type"
const.DRIVER_PATH = "Driver_path"
const.START_ENV = "Start_Env"

const.ELEMENT = "Element"
const.IDTYPE = "Idtype"
const.ACTION = "Action"
const.VALUE = "Value"

const.DRIVER_TYPE_CHROME = "Chrome"
const.DRIVER_TYPE_FIREFOX = "Firefox"
const.DRIVER_TYPE_IE = "Ie"

const.CHROME_DRIVER_PATH = "./drivers/chromedriver"
const.FIREFOX_DRIVER_PATH = "./drivers/geckodriver"
const.IE_DRIVER_PATH = "./drivers/IEDriverServer.exe"

const.IDTYPE_ID = "id"
const.IDTYPE_NAME = "name"
const.IDTYPE_CLASS_NAME = "class_name"
const.IDTYPE_TAG_NAME = "tag_name"
const.IDTYPE_LINK_TEXT = "link_text"
const.IDTYPE_PARTIAL_LINK_TEXT = "partial_link_text"
const.IDTYPE_XPATH = "xpath"
const.IDTYPE_CSS_SELECTOR = "css_selector"
const.IDTYPE_REFERENCE = "reference"
# const.REFERENCE_OVERFLAG = "overdue"

const.ACTION_KEYIN = "keyin"
const.ACTION_CLICK = "click"
const.ACTION_ASSERT = "assert"

const.ASSERT_ACTION = "AssertAction"
const.ASSERT_EXPERT = "AssertExpert"
const.ASSERT_ELEMENT_TYPE = "AssertElementType"
const.ASSERT_T_ROW = "AssertTableRow"
const.ASSERT_T_COLUMN = "AssertTableColumn"

const.ELEMENT_TYPE_TABLE = "table"
const.ELEMENT_TYPE_TR = "tr"
const.ELEMENT_TYPE_TEXT = "text"

const.BASIC_METHOD_NAME = "test_qbao"

const.REPORT_FOLDERNAME = "./UI_Result"