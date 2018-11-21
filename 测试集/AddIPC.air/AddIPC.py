# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
start_app("com.bosma.smarthome")
sleep(5)

def login():
    sleep(5)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
#如果已经登录，直接发送反馈
if poco(text="博冠智能").exists():
    sleep(2)
    #进入添加设备页面
    poco("com.bosma.smarthome:id/iv_toolbar_icon").click()
    poco(text="BOSMA X1").click()
    

    sleep(2)
    SendFeedback_normal()
    
#如果还没登录，先执行登录，再发送反馈
else:
    login()
    sleep(2)
    find_page()
    sleep(2)
    SendFeedback_normal()

    