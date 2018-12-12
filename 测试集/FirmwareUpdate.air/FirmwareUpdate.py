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
    sleep(1)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco.swipe([100/1920,900/1080],[100/1920,300/1080])#这一条执行没错啊
        poco(text="设备固件更新").click()
        sleep(2)
        if exists(Template(r"tpl1542614481067.png", record_pos=(0.0, 0.324), resolution=(1080, 1920))):
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1543976346649.png", record_pos=(-0.001, -0.742), resolution=(1440, 2560)),"没有最新固件")
        else:
            poco(text="立刻更新").click()
            sleep(150)
            poco("com.bosma.smarthome:id/btnSingle").click()
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1542614997728.png", record_pos=(-0.007, 0.448), resolution=(1080, 1920)),"升级成功")
            
  
    else:
        poco("转到上一层级").click()

    
    
else:
    commom_login()
    sleep(2)
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click()  
    sleep(1)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
        #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco.swipe([100/1920,900/1080],[100/1920,300/1080])
        poco(text="设备固件更新").click()
        sleep(2)
        if exists(Template(r"tpl1542614481067.png", record_pos=(0.0, 0.324), resolution=(1080, 1920))):
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1543976346649.png", record_pos=(-0.001, -0.742), resolution=(1440, 2560)),"没有最新固件")

        else:
            poco(text="立刻更新").click()
            sleep(150)
            poco("com.bosma.smarthome:id/btnSingle").click()
            poco("转到上一层级").click()
            assert_exists(Template(r"tpl1542614997728.png", record_pos=(-0.007, 0.448), resolution=(1080, 1920)),"升级成功")

