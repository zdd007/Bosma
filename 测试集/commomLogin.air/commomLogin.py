# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def commom_login():
    sleep(3)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    sleep(2)
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    sleep(2)