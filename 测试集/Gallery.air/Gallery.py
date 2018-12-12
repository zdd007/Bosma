# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *
from airtest.core.api import using
using("commomLogin.air")
from commomLogin import commom_login

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(5)

def cloud():
    poco(text="云").click()
    assert_exists(Template(r"tpl1544085595752.png", record_pos=(0.008, -0.585), resolution=(1440, 2560)),"点击云相册页面切换正常")
    sleep(1)
       
if poco(text="博冠智能").exists():
    poco("com.bosma.smarthome:id/fl_mainblock_gallery").click()
    cloud()
    
else:
    commom_login()
    poco("com.bosma.smarthome:id/fl_mainblock_gallery").click()