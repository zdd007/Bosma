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
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco.swipe([100/1920,900/1080],[100/1920,300/1080])
        poco(text="设备固件更新").click()
        if exists(Template(r"tpl1542614481067.png", record_pos=(0.0, 0.324), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:
            poco(text="设备固件更新").click()
            sleep(5)
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1542614997728.png", record_pos=(-0.007, 0.448), resolution=(1080, 1920)),"升级成功")
            
  
    else:
        poco("转到上一层级").click()

    
    
else:
    login()
    sleep(2)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco.swipe([100/1092,300/1008],[100/1092,900/1008])
        poco(text="设备固件更新").click()
        if exists(Template(r"tpl1542614481067.png", record_pos=(0.0, 0.324), resolution=(1080, 1920))):
            poco("转到上一层级").click()
        else:
            poco(text="设备固件更新").click()
            sleep(5)
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1542614997728.png", record_pos=(-0.007, 0.448), resolution=(1080, 1920)),"升级成功")

