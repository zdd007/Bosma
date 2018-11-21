# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(2)
#输入登录信息
poco("com.bosma.smarthome:id/et_account").set_text('1451953028@qq.com')
sleep(2)
poco("com.bosma.smarthome:id/et_pwd").set_text('qwert123456')
sleep(2)
poco("com.bosma.smarthome:id/btn_login").click()
sleep(2)
#判断是否登录成功
