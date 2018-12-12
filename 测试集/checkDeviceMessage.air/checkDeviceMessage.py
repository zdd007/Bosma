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

    
#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
    sleep(2)
    assert_exists(Template(r"tpl1543803129496.png", record_pos=(0.054, -0.503), resolution=(1440, 2560)),"设备ID获取正确")
    assert_exists(Template(r"tpl1542362748350.png", record_pos=(-0.068, -0.453), resolution=(1080, 1920)),"版本获取正常")
    
    
else:
    commom_login()
    sleep(2)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    assert_exists(Template(r"tpl1543803129496.png", record_pos=(0.054, -0.503), resolution=(1440, 2560)),"设备ID获取正确")

    assert_exists(Template(r"tpl1542362748350.png", record_pos=(-0.068, -0.453), resolution=(1080, 1920)),"版本获取正常")
