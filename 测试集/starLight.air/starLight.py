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
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco(text="星光模式").click()
        sleep(2)
        poco("com.bosma.smarthome:id/uisb_nightvision_model").click()
        poco("转到上一层级").click()
        sleep(2)
        poco(text="星光模式").click()
        sleep(2)
        assert_exists(Template(r"tpl1542178624421.png", record_pos=(0.322, -0.556), resolution=(1080, 1920)),"星光模式开启成功")
        #再恢复为关闭状态，方便再次执行测试
        poco("com.bosma.smarthome:id/uisb_nightvision_model").click()
        poco("转到上一层级").click()

    else:
        poco("转到上一层级").click()


    
#如果还没登录，先执行登录，再执行格式化SDCard操作
else:
    login()
    poco("com.bosma.smarthome:id/fl_mainblock_livevideo").click() 
    sleep(3)
    if exists(Template(r"tpl1541051036321.png", record_pos=(0.424, -0.61), resolution=(1080, 1920))):
         #进入设备设备页面
        poco("com.bosma.smarthome:id/iv_livelist_right_setting").click()
        poco(text="星光模式").click()
        sleep(2)
        poco("com.bosma.smarthome:id/uisb_nightvision_model").click()
        poco("转到上一层级").click()
        sleep(2)
        poco(text="星光模式").click()
        sleep(2)
        assert_exists(Template(r"tpl1542178624421.png", record_pos=(0.322, -0.556), resolution=(1080, 1920)),"星光模式开启成功")
        #再恢复为关闭状态，方便再次执行测试
        poco("com.bosma.smarthome:id/uisb_nightvision_model").click()
        poco("转到上一层级").click()


    else:
        poco("转到上一层级").click()
