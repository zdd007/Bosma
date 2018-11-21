# -*- encoding=utf8 -*-
__author__ = "zhongdd"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

stop_app("com.bosma.smarthome")
sleep(2)
start_app("com.bosma.smarthome")
sleep(5)

def login():
    sleep(2)
    poco("com.bosma.smarthome:id/et_account").set_text("1451953028@qq.com")
    poco("com.bosma.smarthome:id/et_pwd").set_text("zdd123456")
    poco("com.bosma.smarthome:id/btn_login").click()
    
#如果已经登录，执行格式化SDCard操作
if poco(text="博冠智能").exists():
    sleep(1)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    assert_exists(Template(r"tpl1542362621050.png", record_pos=(0.104, -0.515), resolution=(1080, 1920)),"设备ID获取正确")
    assert_exists(Template(r"tpl1542362748350.png", record_pos=(-0.068, -0.453), resolution=(1080, 1920)),"版本获取正常")
    
    
else:
    login()
    sleep(2)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    assert_exists(Template(r"tpl1542362621050.png", record_pos=(0.104, -0.515), resolution=(1080, 1920)),"设备ID获取正确")
    assert_exists(Template(r"tpl1542362748350.png", record_pos=(-0.068, -0.453), resolution=(1080, 1920)),"版本获取正常")
